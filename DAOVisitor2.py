
'''
"""
This module contains the implementation of the DAOVisitor2 class, which is a visitor for parsing XML files and extracting information related to DAOs, roles, committees, permissions, and relations.
The DAOVisitor2 class inherits from the XMLParserVisitor class and overrides its visit methods to handle specific XML elements.
The class has the following attributes:
- daos: a dictionary storing DAO objects, with DAO IDs as keys and DAO objects as values.
- roles: a dictionary storing Role objects, with role IDs as keys and Role objects as values.
- committees: a dictionary storing Committee objects, with committee IDs as keys and Committee objects as values.
- permissions: a dictionary storing Permission objects, with permission IDs as keys and Permission objects as values.
- control_graph: a directed graph (networkx.DiGraph) representing the control relations between roles and committees.
- aggregations: a defaultdict(list) storing the aggregation relations between roles/committees and other entities.
- associations: a defaultdict(list) storing the association relations between roles/committees and other entities.
- control_relations: a defaultdict(list) storing the control relations between roles/committees and other entities.
The DAOVisitor2 class provides methods for visiting different XML elements and extracting relevant information. It also performs assignments of permissions, controllers, and aggregated entities to roles, committees, and DAOs based on the extracted relations.
Additionally, the class generates a control graph based on the control relations and assigns it to the corresponding DAO object. It also utilizes a SolidityTranslator object to generate Solidity code based on the extracted information.
To use this class, create an instance of DAOVisitor2 and call its visit method, passing the root XML element as the argument.
'''
import networkx as nx
from collections import defaultdict
from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
if __name__ is not None and "." in __name__:
#    from .XMLLexer import XMLLexer
#    from .XMLParser import XMLParser
    from .XMLParserVisitor import XMLParserVisitor
else:
#    from XMLLexer import XMLLexer
#    from XMLParser import XMLParser
    from XMLParserVisitor import XMLParserVisitor
from DAOclasses import*
#from TranslationPolicies.translator import*
from DiagramManager import DiagramManager


class DAOVisitor2(XMLParserVisitor):
    def __init__(self):
        #self.daos = {}
        self.current_dao = None
        #self.roles = {} # roles_by_dao_name
        #self.committees = {} # roles_by_dao_name
        #self.permissions = {} # roles_by_dao_name
        #self.control_graph = nx.DiGraph()
# dictionaries storing relations to be associated to roles and committees during the visit with role as key and list of related ids as values
        #self.aggregations = defaultdict(list)
        #self.associations = defaultdict(list)
        #self.control_relations = defaultdict(list)
        self.translation_results = []
        self.diagramManager = None
        #self.daos = {}

    def parseDiagramTree(self, tree, diagramManager: DiagramManager, reset=False):
        self.diagramManager = diagramManager
        if reset:
            diagramManager.reset()
        # at first, gather all the data (raw instances) through the "visitABC" methods into the "diagramManager" ...
        self.visit(tree)
        # ... then, process and "link" all the raw data
        diagramManager.processRawInstances()
        #for dao in diagramManager.daoByID.values():
        #    self.daos[dao.dao_id] = dao
        self.diagramManager = None # just to clean the memory

    def visitRole(self, ctx):
        role_id = ctx.role_id().STRING().getText().strip('"')
        role_name = ctx.role_name().STRING().getText().strip('"')
        role_assignment_method = ctx.role_assignment_method().STRING().getText().strip('"')
        agent_type = ctx.agent_type().STRING().getText().strip('"')
        role = Role(role_id, role_name, role_assignment_method, agent_type)

        self.diagramManager.addRole(self.current_dao, role)
        #self.roles[role_id] = role
        print(f'Role created with ID: {role_id}')
        return self.visitChildren(ctx)

    def visitCommittee(self, ctx):
        committee_id = ctx.committee_id().STRING().getText().strip('"')
        committee_description = ctx.committee_description().STRING().getText().strip('"')
        n_agent_min = ctx.n_agent_min().STRING().getText().strip('"') if ctx.n_agent_min() else None
        n_agent_max = ctx.n_agent_max().STRING().getText().strip('"') if ctx.n_agent_max() else None
        appointment_method = ctx.appointment_method().STRING().getText().strip('"')
        committee = Committee(committee_id, committee_description, n_agent_min, n_agent_max, appointment_method)
        #self.committees[committee_id] = committee
        print(f'Committee created with ID: {committee_id}')
        self.diagramManager.addCommittee(self.current_dao, committee)
        return self.visitChildren(ctx)

    def visitPermission(self, ctx):
        permission_id = ctx.permission_id().STRING().getText().strip('"')
        allowed_action = ctx.allowed_action().STRING().getText().strip('"')
        permission_type = ctx.permission_type().STRING().getText().strip('"')
        permission = Permission(permission_id, allowed_action, permission_type)
        self.diagramManager.addPermission(self.current_dao, permission)
        #self.permissions[permission_id] = permission
        #self.current_dao.add_permission(permission)
        print(f'Permission created with ID: {permission_id}')
        return self.visitChildren(ctx)

    def __extract_ID(self, node) -> str:
        beholderID = None
        if hasattr(node, 'role_id') and callable(getattr(node, 'role_id')):
            beholderID = node.role_id()
        if hasattr(node, 'committee_id') and callable(getattr(node, 'committee_id')):
            beholderID = node.committee_id()
        if beholderID is None:
            raise Exception("can't extract an id")
        return beholderID.STRING().getText().strip('"')


    def visitRelations(self, ctx):
    #visits associated to relations and stores them in the dictionary

        # TODO: usa "RelationType" nella invocazione
        # " addRelation(self.current_dao, RelationType.AGGREGATION, id, content) "
        # iterata nei vari cicli for
        # (qui il " RelationType.AGGREGATION" e' SOLO un ruolo di esempio)
        
        if ctx.associated_to():
            for assoc in ctx.associated_to():
                content = self.aggregate_texts(assoc.content().chardata())
                print("in associated_to: " + self.aggregate_texts(assoc.content().chardata(), separator=", "))
                #if hasattr(ctx.parentCtx, 'role_id') and callable(getattr(ctx.parentCtx, 'role_id')):
                #    id = ctx.parentCtx.role_id().STRING().getText().strip('"')
                #else:
                #    id = ctx.parentCtx.committee_id().STRING().getText().strip('"')
                id = self.__extract_ID(ctx.parentCtx)
                self.diagramManager.addRelation(self.current_dao, RelationType.ASSOCIATION, id, content)
        if ctx.controlled_by():
            for control in ctx.controlled_by():
                content = self.aggregate_texts(control.content().chardata())
                print("in controlled_by: " + self.aggregate_texts(control.content().chardata(), separator=", "))
                #if hasattr(ctx.parentCtx, 'role_id') and callable(getattr(ctx.parentCtx, 'role_id')):
                #    id = ctx.parentCtx.role_id().STRING().getText().strip('"')
                #else:
                #    id = ctx.parentCtx.committee_id().STRING().getText().strip('"')
                id = self.__extract_ID(ctx.parentCtx)
                self.diagramManager.addRelation(self.current_dao, RelationType.CONTROL, id, content)
        if ctx.aggregates():
            for aggregated in ctx.aggregates():
                content = self.aggregate_texts(aggregated.content().chardata())
                print("in aggregates: " + self.aggregate_texts(aggregated.content().chardata(), separator=", "))
                #if hasattr(ctx.parentCtx, 'role_id') and callable(getattr(ctx.parentCtx, 'role_id')):
                #    id = ctx.parentCtx.role_id().STRING().getText().strip('"')
                #else:
                #    id = ctx.parentCtx.committee_id().STRING().getText().strip('"')
                id = self.__extract_ID(ctx.parentCtx)
                self.diagramManager.addRelation(self.current_dao, RelationType.AGGREGATION, id, content)
        return self.visitChildren(ctx)
        # if ctx.associated_to():
        #     for assoc in ctx.associated_to():
        #         content = self.aggregate_texts(assoc.content().chardata())
        #         if hasattr(ctx.parentCtx, 'role_id') and callable(getattr(ctx.parentCtx, 'role_id')):
        #             id = ctx.parentCtx.role_id().STRING().getText().strip('"')
        #         else:
        #             id = ctx.parentCtx.committee_id().STRING().getText().strip('"')
        #         if content not in self.associations[id]:
        #             self.associations[id].append(content)
        #             print(f'Role {id} is associated with {content}')
        #         else:
        #             print(f'did not add {content} to Role {id}')
        # #visits control relations and stores them in the dictionary
        # if ctx.controlled_by():
        #     for control in ctx.controlled_by():
        #         content = self.aggregate_texts(control.content().chardata())
        #         if hasattr(ctx.parentCtx, 'role_id') and callable(getattr(ctx.parentCtx, 'role_id')):
        #             id = ctx.parentCtx.role_id().STRING().getText().strip('"')
        #         else:
        #             id = ctx.parentCtx.committee_id().STRING().getText().strip('"')
        #         if content not in self.control_relations[id]:
        #             self.control_relations[id].append(content)
        #             print(f'Role {id} is controlled by{content}')
        #         else:
        #             print(f'did not add the control {content} to Role {id}')
                    
        # #visits aggregation relations and stores them in the dictionary
        # if ctx.aggregates():
        #     for aggregated in ctx.aggregates():
        #         content = self.aggregate_texts(aggregated.content().chardata())
        #         if hasattr(ctx.parentCtx, 'role_id') and callable(getattr(ctx.parentCtx, 'role_id')):
        #             id = ctx.parentCtx.role_id().STRING().getText().strip('"')
        #         else:
        #             id = ctx.parentCtx.committee_id().STRING().getText().strip('"')
        #         if content not in self.aggregations[id]:
        #             self.aggregations[id].append(content)
        #             print(f'Role or Committee {id} aggregates into {content}')
        #         else:
        #             print(f'did not add the aggregation {content} to {id}')
        # return self.visitChildren(ctx)
    
    def visitDao(self, ctx):
        dao_id = ctx.dao_id().STRING().getText().strip('"')
        dao_name = ctx.dao_name().STRING().getText().strip('"')
        mission_statement = ctx.mission_statement().STRING().getText().strip('"')
        hierarchical_inheritance = ctx.hierarchical_inheritance().STRING().getText().strip('"')
        dao = DAO(dao_id, dao_name, mission_statement, hierarchical_inheritance)
        #self.daos[dao_id] = dao
        self.diagramManager.addDao(dao)
        print(f'DAO created with ID: {dao_id}')
        #recursively visits the children of the dao
        self.current_dao = dao
        self.visitChildren(ctx)
        self.current_dao = None
        return dao

    def aggregate_texts(self, chardata_list, separator = ""):
        return (separator if separator else "").join([node.getText().strip() for node in chardata_list])
    
    def __str__(self):
        '''
        result = ["DAOs:"]
        for dao in self.daos.values():
            result.append(str(dao))
        result.append("\nRoles:")
        for role in self.roles.values():
            result.append(str(role))
        result.append("\nCommittees:")
        for committee in self.committees.values():
            result.append(str(committee))
        result.append("\nPermissions:")
        for permission in self.permissions.values():
            result.append(str(permission))
        for aggregated in self.aggregations:
            result.append(f"{aggregated} aggregates into {self.aggregations[aggregated]}")
        return "\n".join(result)
        '''
        raise Exception("should not be invoked")

    def get_translation_summary(self):
        return str(self)

    # def get_control_graph(self):
    #     return self.control_graph
    
    




def traverse(tree, rule_names, indent=0):
    if tree.getText() == "<EOF>":
        return
    elif isinstance(tree, TerminalNodeImpl):
        print("{0}TOKEN='{1}'".format("\t" * indent, tree.getText()))
    else:
        print("{0}{1}".format("\t" * indent, rule_names[tree.getRuleIndex()]))
        for child in tree.children:
            traverse(child, rule_names, indent + 1)
'''
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = XMLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = XMLParser(stream)
    tree = parser.document()

    visitor = DAOVisitor2()
    traverse(tree, parser.ruleNames, 0)
    visitor.visit(tree)

    print("\n -----PRINTING VISITOR CONTENT----")
    print(visitor)
    print("\n -----PRINTING VISITOR CONTENT----")


if __name__ == '__main__':
    main(sys.argv)
'''