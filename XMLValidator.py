import xml.etree.ElementTree as etree # ET
from lxml import etree
import xmlschema


class ConstraintValidator():
    def __init__(self, XMLFile, schemaFile):
        self.xmlname = XMLFile
        self.schemafile = schemaFile

    #diagram validation functions for the two DAOMod diagram types
    def validate_against_schema(self):
        file_name = self.xmlname
        schema_name = self.schemafile
        try: 
            diagram_xml = etree.parse(file_name)
            validation = xmlschema.XMLSchema(schema_name)    
            if validation.is_valid(diagram_xml):
                print(f'The XML file structure complies with the DAO-ML schema')
                return True
            else:
                # Validate the XML file and collect errors
                errors = list(validation.iter_errors(file_name))
                error_output = []
                print(f'The XML file is not valid. Found {len(errors)} error(s):')
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


    def validate_dao_ml_diagram(self):
        diagram_file = self.xmlname
        conditions =[]

        diagram = etree.parse(diagram_file)
        conditions.append(self.validate_against_schema())
        conditions.append(self.compare_subsets(diagram,"IDs that roles or committees are associated to", '//Role/associated_to/text()| //Committee/associated_to/text()',"Permission or Governance Area IDs", '//Permission/@permission_ID') )   
        conditions.append(self.compare_subsets(diagram,"IDs of elements that roles aggregate into", '//Role/aggregates/text()',"Roles' IDs", '//Role/@role_ID'))    
        conditions.append(self.compare_subsets(diagram,"IDs of elements that committees aggregate into", '//Committee/aggregates/text()',"Committee' IDs", '//Committee/@committee_ID'))
        conditions.append(self.compare_subsets(diagram,"IDs of control relations", '//Role/is_controlled_by/text()|//Committee/is_controlled_by/text()',"Role or Committee IDs", '//Role/@role_ID|//Committee/@committee_ID'))  
        conditions.append(self.check_relation_graphs(diagram,"aggregation_level", "aggregates"))
        conditions.append(self.check_relation_graphs(diagram,"federation_level", "federates_into"))
        conditions.append(self.check_relations_in_same_DAO(diagram, early_return=False))
        for condition in conditions:
            if isinstance(condition, list):  # Check if the condition contains a list of errors
                for sub_index, sub_condition in enumerate(condition):
                    print(f"Error at condition {conditions.index(condition)}, sub-condition {sub_index}")
                    print(sub_condition)
                    raise Exception(
                        f"Invalid diagram {diagram_file}, condition {conditions.index(condition)}, sub-condition {sub_index} failed: {sub_condition}"
                    )
            elif condition != True:
                print(f"Error at condition {conditions.index(condition)}")
                print(condition)
                raise Exception(
                    f"Invalid diagram {diagram_file}, condition {conditions.index(condition)} failed: {condition}"
                )

        print(f"All conditions are valid for the diagram {diagram_file}")
        return True
