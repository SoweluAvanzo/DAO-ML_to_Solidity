
import xml.etree.ElementTree as ET
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

        diagram_xml = etree.parse(file_name)
        validation = xmlschema.XMLSchema(schema_name)    
        if validation.is_valid(diagram_xml):
            print(f'The XML file structure complies with the DAO-ML schema')
            return True
        else:
            raise Exception("The XML file is not a valid DAO-ML diagram")

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
            print(f"the set of {name1} \n {self.split_and_add_to_list(id_list1)} is a subset of {name2}:\n {self.split_and_add_to_list(id_list2)}\n")
            return True
        else:
            raise Exception(f"invalid relation:{self.split_and_add_to_list(id_list1)} is not a subset of {self.split_and_add_to_list(id_list2)}\n")

            
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
                print(f"{elem.tag} with id {elem_id} does not have a level for {rel_name}")
                continue

            level = int(level)

            # Retrieve the relation elements based on the relation name
            relation = elem.xpath(f"{rel_name}/text()")
            if relation:
                for relator_id in relation:
                    # Find the related element based on the relation ID (either role_ID or committee_ID)
                    relator_elems = diagram.xpath(f'//*[@role_ID="{relator_id}"] | //*[@committee_ID="{relator_id}"]')
                    if not relator_elems:
                        print(f"No element found with id {relator_id}")
                        continue

                    relator_elem = relator_elems[0]

                    # Get the level of the related element
                    relator_level = relator_elem.get(rel_attribute)

                    if relator_level is None:
                        print(f"Relator with id {relator_id} does not have a {rel_attribute}")
                        continue

                    relator_level = int(relator_level)

                    # Logging information for debugging
                    print(f"Checking {elem.tag} with id {elem_id}")
                    print(f"{elem.tag} {rel_name} level: {level}")
                    print(f"Relator id: {relator_id}, Relator level: {relator_level}")

                    # Check the relation constraint (current element's level should be less than relator's level)
                    if level < relator_level:
                        print(f"{rel_name} relation is valid\n")
                        return True
                    else:
                        print(f"{rel_name} relation violation\n")
                        raise Exception(
                            f"{elem.tag} with id {elem_id} has a {rel_name} relation with a {relator_elem.tag} "
                            f"with id {relator_id} that has a higher or equal {rel_attribute} \n"
                            )

    # def validate_dao_references(self,diagram):
    # # Parse the XML file
    # tree = etree.parse(diagram_file)
        # Collect all the ID references (relations) inside the DAO element
        # # Iterate over all DAOs in the diagram
        # for dao in diagram.xpath('//DAO'):
        #     # Get all the ID references for the current DAO element
        #     associated_to_refs = dao.xpath('.//associated_to/text()')
        #     is_controlled_by_refs = dao.xpath('.//is_controlled_by/text()')
        #     federates_into_refs = dao.xpath('.//federates_into/text()')

        #     # Combine all references into one list
        #     all_id_refs = set(associated_to_refs + is_controlled_by_refs + federates_into_refs)

        #     # Collect all valid IDs from DAO descendants (Role, Committee, GovernanceArea, Permission)
        #     valid_role_ids = dao.xpath('.//Role/@role_ID')
        #     valid_committee_ids = dao.xpath('.//Committee/@committee_ID')
        #     valid_gov_area_ids = dao.xpath('.//GovernanceArea/@gov_area_ID')
        #     valid_permission_ids = dao.xpath('.//Permission/@permission_ID')

        #     valid_ids = set(valid_role_ids + valid_committee_ids + valid_gov_area_ids + valid_permission_ids)

        #     invalid_refs = [ref for ref in all_id_refs if ref not in valid_ids]

        #     if invalid_refs:
            #     raise Exception(f"Invalid ID references found: {invalid_refs}")
        #     else:
            #     print("All ID references are valid.")
                # return True    

    def validate_dao_ml_diagram(self):
        diagram_file = self.xmlname
        conditions =[]

        diagram = etree.parse(diagram_file)
        conditions.append(self.validate_against_schema())
        conditions.append(self.compare_subsets(diagram,"IDs that roles or committees are associated to", '//Role/associated_to/text()| //Committee/associated_to/text()',"Permission or Governance Area IDs", '//Permission/@permission_ID') )   
        conditions.append(self.compare_subsets(diagram,"IDs of elements that roles aggregate into", '//Role/aggregates/text()',"Roles' IDs", '//Role/@role_ID'))    
        conditions.append(self.compare_subsets(diagram,"IDs of elements that committees aggregate into", '//Committee/aggregates/text()',"Committee' IDs", '//Committee/@committee_ID'))
        conditions.append(self.compare_subsets(diagram,"IDs of control relations", '//Role/is_controlled_by/text()|//Committee/is_controlled_by/text()',"Role or Committee IDs", '//Role/@role_ID|//Committee/@committee_ID'))  
        #conditions.append(self.validate_dao_references(diagram))
        conditions.append(self.check_relation_graphs(diagram,"aggregation_level", "aggregates"))
        conditions.append(self.check_relation_graphs(diagram,"federation_level", "federates_into"))
        for condition in conditions:
            if condition != True:
                print(f"error at condition {conditions.index(condition)}")
                print(condition)
                raise Exception(f"Invalid diagram {diagram_file}")
        print(f"All conditions are valid for the diagram {diagram_file}")
        return True

