import os
from io import StringIO, TextIOBase, BufferedIOBase, RawIOBase, IOBase
import xml.etree.ElementTree as etree # ET
from lxml import etree
import xmlschema
import networkx as nx


import src.validators.base_validator as bv
import src.pipeline.pipeline_item as pi


DEFAULT_XML_SCHEMA = "data/XSD_DAO_ML.xsd"


# TODO: PUT THE ALREADY-READ-XML-(string) INTO THE CONSTRUCTOR !!!!!!!!!!!
class XMLDaoValidator(bv.BaseValidator):
    def __init__(self, pipeline_item_data: pi.PIData, xml_schema_filepath: str, constraint_validator=None):
        super().__init__(pipeline_item_data)
        self.xml_schema_filepath = xml_schema_filepath
        self.constraint_validator = constraint_validator
    
    def validate(self, input:str) -> bool:
        # if the input is a list/array, then collapse it to form a single string
        input_string_list=None
        if isinstance(input, list):
            input_string_list = input
            input = "\n".join(input)
        # check if the input is a file or a string-of-already-read-file
        if not isinstance(input, str):
            error_text = f"input is not a string: {input.__class__.__name__}"
            print(error_text)
            raise Exception(error_text)
        tree_root = None
        # try to obtain a parsed object of the XML file from the input:
        # is the input the file path, a File or the actual already-read content?
        if os.path.isfile(input):
            with open(input, 'r') as file_xml:
                tree_root = etree.parse(StringIO(file_xml))
                input_string_list = tree_root.itertext()
        elif (isinstance(input, TextIOBase) or \
            isinstance(input, BufferedIOBase) or \
            isinstance(input, RawIOBase) or \
            isinstance(input, IOBase) \
            ):
                tree_root = etree.parse(input)
                input_string_list = tree_root.itertext()
        else:
            input_string_list = input.split('\n')
            parser = etree.XMLParser(ns_clean=True, remove_comments=True, remove_blank_text=True)
            tree_root = etree.fromstring(input, parser)

        xml_schema_fp = DEFAULT_XML_SCHEMA if self.xml_schema_filepath is None else self.xml_schema_filepath
        cv = ConstraintValidator(xml_schema_fp, input) if self.constraint_validator is None else self.constraint_validator
        
        errors_ok = cv.validate_dao_ml_diagram(tree_root)
        ok:bool = errors_ok[0]
        errors:list[str] = errors_ok[1]

        return {
            "validation_result": ok,
            "errors": errors,
            "tree_parsed": tree_root,
            "input": input,
            "input_string_list": input_string_list
        }        

class ConstraintValidator():
    def __init__(self, schemaFile, file_content):
        self.schemafile = schemaFile
        self.file_content = file_content

    #diagram validation functions for the two DAOMod diagram types
    def validate_against_schema(self, diagram):
        schema_name = self.schemafile
        try:
            validation = xmlschema.XMLSchema(schema_name)    
            if validation.is_valid(diagram):
                print(f'The XML file structure complies with the schema: {schema_name}')
                return True
            else:
                # Validate the XML file and collect errors
                errors = list(validation.iter_errors(self.file_content))
                error_output = []
                
                for error in errors:
                    #append error name
                    error_output.append(f"- {error} \n")
                return error_output
        except xmlschema.XMLSchemaException as e:
            print(f"Error with the schema file: {e}")
            return e
        
    def split_and_add_to_list(self,strings):
        result = []
        for string in strings:
            substrings = string.split()
            result.extend(substrings)
        result_set = set(result)
        return result_set

    def compare_subsets(self,diagram,name1, query1,name2, query2):
        id_list1 = diagram.xpath(query1)
        id_list2 = diagram.xpath(query2)
        if self.split_and_add_to_list(id_list1).issubset(self.split_and_add_to_list(id_list2)):
            return True
        else:
            errors = []
            errors.append(f"invalid relation:{name1} \n {self.split_and_add_to_list(id_list1)} is not a subset of {name2}:\n {self.split_and_add_to_list(id_list2)}\n")
            raise Exception(errors)

    #functions to check federation and aggregation relations in DO Diagrams
    def check_relation_graphs(self,diagram, rel_attribute, rel_name):
        for elem in diagram.xpath("//Role | //Committee"):
            # Check the type of the element (Role or Committee) and set the correct ID attribute
            if elem.tag == "Role":
                elem_id = elem.get("role_ID")
            elif elem.tag == "Committee":
                elem_id = elem.get("committee_ID")
            else:
                continue  # Skip if it's neither Role nor Committee
            
            level = elem.get(rel_attribute)
            if level is None:
                continue
            level = int(level)

            # Retrieve the relation elements based on the relation name
            relation = elem.xpath(f"{rel_name}/text()")
            if relation:
                for relator_id in relation:
                    # Find the related element based on the relation ID (either role_ID or committee_ID)
                    relator_elems = diagram.xpath(f'//*[@role_ID="{relator_id}"] | //*[@committee_ID="{relator_id}"]')
                    if not relator_elems:
                        continue

                    relator_elem = relator_elems[0]

                    # Get the level of the related element
                    relator_level = relator_elem.get(rel_attribute)

                    if relator_level is None:
                        continue

                    relator_level = int(relator_level)

                    # Check the relation constraint (current element's level should be less than relator's level)
                    if level <= relator_level:
                        return True
                    else:
                        print(f"{rel_name} relation violation\n")
                        raise Exception(
                            f"relation violation: {elem.tag} with id {elem_id} has a {rel_name} relation with a {relator_elem.tag} "
                            f"with id {relator_id} that has a higher or equal {rel_attribute} \n"
                            )

    def check_relations_in_same_DAO(self, diagram, early_return = False):
        possible_targets_by_dao_id: map[str, map[str, set]] = {} # { dao_id: TARGETS } ;; TARGETS-> { elem_id: set_of_targetsID }

        all_descendants_name = [ \
            "federates_into", \
            "aggregates", \
            "associated_to", \
            "is_controlled_by" \
        ]
        all_descendants_name_list = " | ".join([f"./{dn}/text()" for dn in all_descendants_name])

        empty_set = set([])

        # at first, gather all relations (with their respective targets)
        for dao in diagram.xpath('//DAO'):
            possible_targets = {} # of current dao
            dao_id = dao.get("DAO_ID")
            possible_targets_by_dao_id[dao_id] = possible_targets

            for elem in dao.xpath("./Role | ./Committee"):
                # Check the type of the element (Role or Committee) and set the correct ID attribute
                elem_id = ""
                if elem.tag == "Role":
                    elem_id = elem.get("role_ID")
                elif elem.tag == "Committee":
                    elem_id = elem.get("committee_ID")
                else:
                    continue  # Skip if it's neither Role nor Committee
                # scan through all possible descendants: federates, aggregates, associated and is_controlled_by ...
                possible_targets[elem_id] = set([target for target in elem.xpath(all_descendants_name_list)])
            
            for elem in dao.xpath("./Permission"):
                elem_id = elem.get('permission_ID')
                target = elem.get('ref_gov_area')
                possible_targets[elem_id] = set([target]) # each permission has only one single target/reletaion

            #also, add each "GovernanceArea" in order to allow Permission to fully target them
            for elem in dao.xpath("./GovernanceArea"):
                elem_id = elem.get('gov_area_ID')
                possible_targets[elem_id] = empty_set # empty set

        # then, check if each target exists somewhere AND exists ONLY in its respective DAO
        all_violations = []
        for dao_id in possible_targets_by_dao_id:
            elements_in_dao = possible_targets_by_dao_id[dao_id]
            for element_id in elements_in_dao: # for each element inside a Dao
                element = elements_in_dao[element_id] # TODO: CHECK IF IT's A SET
                for target_id in element: # for each possible target of current element -> start the check
                    # check against every other DAO
                    for other_dao_id in possible_targets_by_dao_id:
                        if other_dao_id != dao_id : # obviously, exclude current dao
                            other_dao = possible_targets_by_dao_id[other_dao_id]
                            if target_id in other_dao:
                                print(f"ERROR: found target {target_id} (originally from DAO __{dao_id}__) pointing insinde DAO --{other_dao_id}--")
                                if early_return:
                                    return False #ERROR
                                all_violations.append({"elementID_with_external_target": element_id, "incriminated_targetID": target_id, "daoID_of_element": dao_id, "other_daoID": other_dao_id})
            if len(all_violations)>0:
                violations_output = "\n".join(all_violations)
                print(f"all_violations:\n{violations_output}")
                return "\n".join(violations_output)
        return len(all_violations) == 0 # if no violations, then return True



    #functions to check if some cyclic dependencies exists within the federation or aggregation relations in DAO Diagrams
    def check_cyclic_dependencies(self, diagram, rel_name):
        daos_and_loops = []
        for dao in diagram.xpath('//DAO'):
            print(f"CHECKING {rel_name} LOOPS IN DAO: {dao}")
            dao_id = dao.get("DAO_ID")
            graph = nx.DiGraph()
            for elem in dao.xpath("./Role | ./Committee"):
                # Retrieve the relation elements based on the relation name
                element_type = elem.tag  # This will be either 'Role' or 'Committee'
                is_role = element_type == "Role"
                id = elem.get("role_ID") if is_role else elem.get("committee_ID")
                print(f"CHECKING {rel_name} LOOPS IN ELEMENT: {id}")
                relation = elem.xpath(f"{rel_name}/text()")
                if relation:
                    target = relation[0] # ID of the "neighbour"
                    graph.add_edge(id, target)
            cycles = [c for c in nx.simple_cycles(graph)]
            if len(cycles) > 0: # ERROR
                daos_and_loops.append((dao_id, cycles))
        if len(daos_and_loops) > 0:
            return [ \
                f"\tDAO {dal[0]} has the following loop for the ''{rel_name}'': {", ".join(dal[1])}" \
                for dal in daos_and_loops]
        return True # no error
                

    def validate_dao_ml_diagram(self, diagram=None):
        print("starting validate_dao_ml_diagram")
        #diagram_file = self.xmlname
        conditions =[]
        #if diagram is None:
        #    diagram = etree.parse(diagram_file)
        conditions.append(lambda s,d : s.validate_against_schema(d))
        conditions.append(lambda s,d : s.compare_subsets(d,"IDs that roles or committees are associated to", '//Role/associated_to/text()| //Committee/associated_to/text()',"Permission or Governance Area IDs", '//Permission/@permission_ID') )   
        conditions.append(lambda s,d : s.compare_subsets(d,"IDs of elements that roles aggregate into", '//Role/aggregates/text()',"Roles' IDs", '//Role/@role_ID'))    
        conditions.append(lambda s,d : s.compare_subsets(d,"IDs of elements that committees aggregate into", '//Committee/aggregates/text()',"Committee' IDs", '//Committee/@committee_ID'))
        conditions.append(lambda s,d : s.compare_subsets(d,"IDs of control relations", '//Role/is_controlled_by/text()|//Committee/is_controlled_by/text()',"Role or Committee IDs", '//Role/@role_ID|//Committee/@committee_ID'))  
        conditions.append(lambda s,d : s.check_relation_graphs(d,"aggregation_level", "aggregates"))
        conditions.append(lambda s,d : s.check_relation_graphs(d,"federation_level", "federates_into"))
        conditions.append(lambda s,d : s.check_cyclic_dependencies(d, "aggregates"))
        conditions.append(lambda s,d : s.check_cyclic_dependencies(d, "federates_into"))        
        conditions.append(lambda s,d : s.check_relations_in_same_DAO(d, early_return=False))
        i = 0
        error_texts = []
        print(f"validate_dao_ml_diagram with {len(conditions)} conditions")
        for condition_lambda in conditions:
            print(f"running condition lambda # {i}")
            condition = condition_lambda(self, diagram)
            if isinstance(condition, list):  # Check if the condition contains a list of errors
                for sub_index, sub_condition in enumerate(condition):
                    print(f"Error at condition {i}, sub-condition {sub_index}")
                    error_text = f"Invalid diagram diagram_file, condition {i}, sub-condition {sub_index} failed: {sub_condition}"
                    print(sub_condition)
                    #raise Exception(error_text)
                    error_texts.append(error_text)
            elif condition != True:
                print(f"Error at condition {i}")
                error_text = f"Invalid diagram diagram_file, condition {i} failed: {condition}"
                print(condition)
                #raise Exception(error_text)
                error_texts.append(error_text)
            i += 1

        #print(f"All conditions are valid for the diagram {diagram_file}")
        return (True, None) if len(error_texts) <= 0 else (False, error_texts) 
