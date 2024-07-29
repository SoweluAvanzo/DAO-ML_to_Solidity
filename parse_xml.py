'''
import sys
from antlr4 import *
from collections import defaultdict
from antlr4.tree.Tree import TerminalNodeImpl
'''
import networkx as nx
import matplotlib.pyplot as plt
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
from translator import*


class DAO_ML_Visitor(XMLParserVisitor):
    def __init__(self):
        self.daos = {}
        self.roles = {}
        self.committees = {}
        self.permissions = {}
        self.control_graph = nx.DiGraph()

# dictionaries storing relations to be associated to roles and committees during the visit with role as key and list of related ids as values
        self.aggregations = defaultdict(list)
        self.associations = defaultdict(list)
        self.control_relations = defaultdict(list)

    def visitDao(self, ctx):
        dao_id = ctx.dao_id().STRING().getText().strip('"')
        dao_name = ctx.dao_name().STRING().getText().strip('"')
        mission_statement = ctx.mission_statement().STRING().getText().strip('"')
        hierarchical_inheritance = ctx.hierarchical_inheritance().STRING().getText().strip('"')
        dao = DAO(dao_id, dao_name, mission_statement, hierarchical_inheritance)
        self.daos[dao_id] = dao
        print(f'DAO created with ID: {dao_id}')
        return_var = self.visitChildren(ctx)

        # Assign permissions to roles and committees in DAO based on association relations
        for permission in self.permissions:
            for role in self.roles.values():
                if permission in self.associations[role.role_id]:
                    role.add_permission(self.permissions[permission])
                    print(f'Permission {permission} assigned to Role {role.role_id} \n')
            for committee in self.committees.values():
                if permission in self.associations[committee.committee_id]:
                    committee.add_permission(self.permissions[permission])
                    print(f'Permission {permission} assigned to Committee {committee.committee_id}\n')
       # print(f'End of permission assignment execution and visiting DAO \n')

        # Assign controllers to roles and committees in DAO based on control relations
        for role in self.roles.values():
            for controller in self.control_relations[role.role_id]:
                role.add_controller(controller)
                print(f'Controller {controller} assigned to Role {role.role_id} \n')
        for committee in self.committees.values():
            for controller in self.control_relations[committee.committee_id]:
                committee.add_controller(controller)
                print(f'Controller {controller} assigned to Committee {committee.committee_id} \n')

        #assignemnt of roles and committees defined to the DAO
        for role in self.roles.values():
            self.daos[dao_id].add_role(role)
            print(f'Role: {role.role_id} assigned to DAO {dao_id} \n')
        for committee in self.committees.values():
            self.daos[dao_id].add_committee(committee)
            print(f'Committee: {committee.committee_id} assigned to DAO {dao_id} \n')
        
        #control graph generation based on control relations stored
        for role in self.roles.values():
            for controller in role.controllers:
                self.control_graph.add_edge(role.role_id,controller)
        for committee in self.committees.values():
            for controller in committee.controllers:
                self.control_graph.add_edge(committee.committee_id,controller)
        print(f'Control graph generated for DAO {dao_id} \n')
        #assignment of control graph to DAO object
        self.daos[dao_id].dao_control_graph = self.control_graph
        #edges
        for node in self.daos[dao_id].dao_control_graph.nodes:
            print(f'Node: {node} \n')
        for edge in self.control_graph.edges:
            print(f'Edge: {edge} \n')
        #paths
        for node1 in self.daos[dao_id].dao_control_graph.nodes:
            for node2 in self.control_graph.nodes:
                for path in nx.all_simple_paths(self.daos[dao_id].dao_control_graph, source=node1, target=node2):
                    print(f'Path: {path} \n')
                for loop in nx.simple_cycles(self.daos[dao_id].dao_control_graph):
                    print(f'Loop: {loop} \n')
            #code generation
        translator = SolidityTranslator(self.daos[dao_id])
        translator.save_to_file()

        return return_var

    def visitRole(self, ctx):
        role_id = ctx.role_id().STRING().getText().strip('"')
        role_name = ctx.role_name().STRING().getText().strip('"')
        role_assignment_method = ctx.role_assignment_method().STRING().getText().strip('"')
        agent_type = ctx.agent_type().STRING().getText().strip('"')
        role = Role(role_id, role_name, role_assignment_method, agent_type)
        self.roles[role_id] = role
        print(f'Role created with ID: {role_id}')
        return self.visitChildren(ctx)

    def visitCommittee(self, ctx):
        committee_id = ctx.committee_id().STRING().getText().strip('"')
        committee_description = ctx.committee_description().STRING().getText().strip('"')
        n_agent_min = ctx.n_agent_min().STRING().getText().strip('"') if ctx.n_agent_min() else None
        n_agent_max = ctx.n_agent_max().STRING().getText().strip('"') if ctx.n_agent_max() else None
        appointment_method = ctx.appointment_method().STRING().getText().strip('"')
        committee = Committee(committee_id, committee_description, n_agent_min, n_agent_max, appointment_method)
        self.committees[committee_id] = committee
        print(f'Committee created with ID: {committee_id}')
        return self.visitChildren(ctx)

    def visitPermission(self, ctx):
        permission_id = ctx.permission_id().STRING().getText().strip('"')
        allowed_action = ctx.allowed_action().STRING().getText().strip('"')
        permission_type = ctx.permission_type().STRING().getText().strip('"')
        permission = Permission(permission_id, allowed_action, permission_type)
        self.permissions[permission_id] = permission
        print(f'Permission created with ID: {permission_id}')
        return self.visitChildren(ctx)

    def visitRelations(self, ctx):
    #visits associated to relations and stores them in the dictionary
        if ctx.associated_to():
            for assoc in ctx.associated_to():
                content = self.aggregate_texts(assoc.content().chardata())
                if hasattr(ctx.parentCtx, 'role_id') and callable(getattr(ctx.parentCtx, 'role_id')):
                    id = ctx.parentCtx.role_id().STRING().getText().strip('"')
                else:
                    id = ctx.parentCtx.committee_id().STRING().getText().strip('"')
                if content not in self.associations[id]:
                    self.associations[id].append(content)
                    print(f'Role {id} is associated with {content}')
                else:
                    print(f'did not add {content} to Role {id}')
        #visits control relations and stores them in the dictionary
        if ctx.controlled_by():
            for control in ctx.controlled_by():
                content = self.aggregate_texts(control.content().chardata())
                if hasattr(ctx.parentCtx, 'role_id') and callable(getattr(ctx.parentCtx, 'role_id')):
                    id = ctx.parentCtx.role_id().STRING().getText().strip('"')
                else:
                    id = ctx.parentCtx.committee_id().STRING().getText().strip('"')
                if content not in self.associations[id]:
                    self.control_relations[id].append(content)
                    print(f'Role {id} is controlled by{content}')
                else:
                    print(f'did not add the control {content} to Role {id}')
        return self.visitChildren(ctx)

    def aggregate_texts(self, chardata_list):
        return ''.join([node.getText().strip() for node in chardata_list])

    def __str__(self):
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
        return "\n".join(result)




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

    visitor = DAO_ML_Visitor()
    traverse(tree, parser.ruleNames, 0)
    visitor.visit(tree)

    print("\n -----PRINTING VISITOR CONTENT----")
    print(visitor)
    print("\n -----PRINTING VISITOR CONTENT----")


if __name__ == '__main__':
    main(sys.argv)
'''