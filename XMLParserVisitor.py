# Generated from XMLParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .XMLParser import XMLParser
else:
    from XMLParser import XMLParser

# This class defines a complete generic visitor for a parse tree produced by XMLParser.

class XMLParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by XMLParser#document.
    def visitDocument(self, ctx:XMLParser.DocumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#prolog.
    def visitProlog(self, ctx:XMLParser.PrologContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#content.
    def visitContent(self, ctx:XMLParser.ContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#element.
    def visitElement(self, ctx:XMLParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#diagram.
    def visitDiagram(self, ctx:XMLParser.DiagramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#dao.
    def visitDao(self, ctx:XMLParser.DaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#role.
    def visitRole(self, ctx:XMLParser.RoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#committee.
    def visitCommittee(self, ctx:XMLParser.CommitteeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#permission.
    def visitPermission(self, ctx:XMLParser.PermissionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#gov.
    def visitGov(self, ctx:XMLParser.GovContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#daocontent.
    def visitDaocontent(self, ctx:XMLParser.DaocontentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#relations.
    def visitRelations(self, ctx:XMLParser.RelationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#associated_to.
    def visitAssociated_to(self, ctx:XMLParser.Associated_toContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#controlled_by.
    def visitControlled_by(self, ctx:XMLParser.Controlled_byContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#aggregates.
    def visitAggregates(self, ctx:XMLParser.AggregatesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#federates_into.
    def visitFederates_into(self, ctx:XMLParser.Federates_intoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#reference.
    def visitReference(self, ctx:XMLParser.ReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#dao_id.
    def visitDao_id(self, ctx:XMLParser.Dao_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#dao_name.
    def visitDao_name(self, ctx:XMLParser.Dao_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#mission_statement.
    def visitMission_statement(self, ctx:XMLParser.Mission_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#hierarchical_inheritance.
    def visitHierarchical_inheritance(self, ctx:XMLParser.Hierarchical_inheritanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#role_id.
    def visitRole_id(self, ctx:XMLParser.Role_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#role_name.
    def visitRole_name(self, ctx:XMLParser.Role_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#role_assignment_method.
    def visitRole_assignment_method(self, ctx:XMLParser.Role_assignment_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#agent_type.
    def visitAgent_type(self, ctx:XMLParser.Agent_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#committee_id.
    def visitCommittee_id(self, ctx:XMLParser.Committee_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#committee_description.
    def visitCommittee_description(self, ctx:XMLParser.Committee_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#n_agent_min.
    def visitN_agent_min(self, ctx:XMLParser.N_agent_minContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#n_agent_max.
    def visitN_agent_max(self, ctx:XMLParser.N_agent_maxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#appointment_method.
    def visitAppointment_method(self, ctx:XMLParser.Appointment_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#decision_making_method.
    def visitDecision_making_method(self, ctx:XMLParser.Decision_making_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#permission_id.
    def visitPermission_id(self, ctx:XMLParser.Permission_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#allowed_action.
    def visitAllowed_action(self, ctx:XMLParser.Allowed_actionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#permission_type.
    def visitPermission_type(self, ctx:XMLParser.Permission_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#ref_gov_area.
    def visitRef_gov_area(self, ctx:XMLParser.Ref_gov_areaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#attribute.
    def visitAttribute(self, ctx:XMLParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#chardata.
    def visitChardata(self, ctx:XMLParser.ChardataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#misc.
    def visitMisc(self, ctx:XMLParser.MiscContext):
        return self.visitChildren(ctx)



del XMLParser