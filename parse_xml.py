import sys
from antlr4 import *
from collections import defaultdict
from antlr4.tree.Tree import TerminalNodeImpl

if __name__ is not None and "." in __name__:
    from .XMLLexer import XMLLexer
    from .XMLParser import XMLParser
    from .XMLParserVisitor import XMLParserVisitor
else:
    from XMLLexer import XMLLexer
    from XMLParser import XMLParser
    from XMLParserVisitor import XMLParserVisitor


class DAO:
    def __init__(self, dao_id, dao_name, mission_statement, hierarchical_inheritance):
        self.dao_id = dao_id
        self.dao_name = dao_name
        self.mission_statement = mission_statement
        self.hierarchical_inheritance = hierarchical_inheritance
        self.roles = []
        self.committees = []

    def add_role(self, role):
        self.roles.append(role)

    def add_committee(self, committee):
        self.committees.append(committee)

    def __str__(self):
        return f'DAO(dao_id={self.dao_id}, dao_name={self.dao_name}, mission_statement={self.mission_statement}, hierarchical_inheritance={self.hierarchical_inheritance}, roles={self.roles}, committees={self.committees})'


class Role:
    def __init__(self, role_id, role_name, role_assignment_method, agent_type):
        self.role_id = role_id
        self.role_name = role_name
        self.role_assignment_method = role_assignment_method
        self.agent_type = agent_type
        self.permissions = []
        self.controllers = []

    def add_permission(self, permission):
        self.permissions.append(permission)

    def add_controller(self, controller_id):
        self.controllers.append(controller_id)

    def __str__(self):
        return f'Role(role_id={self.role_id}, role_name={self.role_name}, role_assignment_method={self.role_assignment_method}, agent_type={self.agent_type}, permissions={self.permissions}, controllers={self.controllers})'


class Committee:
    def __init__(self, committee_id, committee_description, n_agent_min, n_agent_max, appointment_method):
        self.committee_id = committee_id
        self.committee_description = committee_description
        self.n_agent_min = n_agent_min
        self.n_agent_max = n_agent_max
        self.appointment_method = appointment_method
        self.permissions = []
        self.controllers = []

    def add_permission(self, permission):
        self.permissions.append(permission)

    def add_controller(self, controller_id):
        self.controllers.append(controller_id)

    def __str__(self):
        return f'Committee(committee_id={self.committee_id}, committee_description={self.committee_description}, n_agent_min={self.n_agent_min}, n_agent_max={self.n_agent_max}, appointment_method={self.appointment_method}, permissions={self.permissions}, controllers={self.controllers})'


class Permission:
    def __init__(self, permission_id, allowed_action, permission_type):
        self.permission_id = permission_id
        self.allowed_action = allowed_action
        self.permission_type = permission_type

    def __str__(self):
        return f'Permission(permission_id={self.permission_id}, allowed_action={self.allowed_action}, permission_type={self.permission_type})'


class DAO_ML_Visitor(XMLParserVisitor):
    def __init__(self):
        self.daos = {}
        self.roles = {}
        self.committees = {}
        self.permissions = {}

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
                    role.add_permission(permission)
                    print(f'Permission {permission} assigned to Role {role.role_id} at the end of the execution \n')
            for committee in self.committees.values():
                if permission in self.associations[committee.committee_id]:
                    committee.add_permission(permission)
                    print(f'Permission {permission} assigned to Committee {committee.committee_id} at the end of the execution \n')
        print(f'End of permission assignment execution and visiting DAO \n')
        # Assign controllers to roles and committees in DAO based on control relations
        for role in self.roles.values():
            for controller in self.control_relations[role.role_id]:
                role.add_controller(controller)
                print(f'Controller {controller} assigned to Role {role.role_id} at the end of the execution \n')
        for committee in self.committees.values():
            for controller in self.control_relations[committee.committee_id]:
                committee.add_controller(controller)
                print(f'Controller {controller} assigned to Committee {committee.committee_id} at the end of the execution \n')
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
        # Assign permission to roles and committees
        return self.visitChildren(ctx)

    def visitRelations(self, ctx):
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


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = XMLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = XMLParser(stream)
    tree = parser.document()

    visitor = DAO_ML_Visitor()
    traverse(tree, parser.ruleNames, 0)
    visitor.visit(tree)
    
    # Print all the object properties at the end
    print(visitor)


if __name__ == '__main__':
    main(sys.argv)
