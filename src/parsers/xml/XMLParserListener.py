# Generated from ./XMLParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .XMLParser import XMLParser
else:
    from XMLParser import XMLParser

# This class defines a complete listener for a parse tree produced by XMLParser.
class XMLParserListener(ParseTreeListener):

    # Enter a parse tree produced by XMLParser#document.
    def enterDocument(self, ctx:XMLParser.DocumentContext):
        pass

    # Exit a parse tree produced by XMLParser#document.
    def exitDocument(self, ctx:XMLParser.DocumentContext):
        pass


    # Enter a parse tree produced by XMLParser#prolog.
    def enterProlog(self, ctx:XMLParser.PrologContext):
        pass

    # Exit a parse tree produced by XMLParser#prolog.
    def exitProlog(self, ctx:XMLParser.PrologContext):
        pass


    # Enter a parse tree produced by XMLParser#content.
    def enterContent(self, ctx:XMLParser.ContentContext):
        pass

    # Exit a parse tree produced by XMLParser#content.
    def exitContent(self, ctx:XMLParser.ContentContext):
        pass


    # Enter a parse tree produced by XMLParser#element.
    def enterElement(self, ctx:XMLParser.ElementContext):
        pass

    # Exit a parse tree produced by XMLParser#element.
    def exitElement(self, ctx:XMLParser.ElementContext):
        pass


    # Enter a parse tree produced by XMLParser#diagram.
    def enterDiagram(self, ctx:XMLParser.DiagramContext):
        pass

    # Exit a parse tree produced by XMLParser#diagram.
    def exitDiagram(self, ctx:XMLParser.DiagramContext):
        pass


    # Enter a parse tree produced by XMLParser#dao.
    def enterDao(self, ctx:XMLParser.DaoContext):
        pass

    # Exit a parse tree produced by XMLParser#dao.
    def exitDao(self, ctx:XMLParser.DaoContext):
        pass


    # Enter a parse tree produced by XMLParser#role.
    def enterRole(self, ctx:XMLParser.RoleContext):
        pass

    # Exit a parse tree produced by XMLParser#role.
    def exitRole(self, ctx:XMLParser.RoleContext):
        pass


    # Enter a parse tree produced by XMLParser#committee.
    def enterCommittee(self, ctx:XMLParser.CommitteeContext):
        pass

    # Exit a parse tree produced by XMLParser#committee.
    def exitCommittee(self, ctx:XMLParser.CommitteeContext):
        pass


    # Enter a parse tree produced by XMLParser#permission.
    def enterPermission(self, ctx:XMLParser.PermissionContext):
        pass

    # Exit a parse tree produced by XMLParser#permission.
    def exitPermission(self, ctx:XMLParser.PermissionContext):
        pass


    # Enter a parse tree produced by XMLParser#gov.
    def enterGov(self, ctx:XMLParser.GovContext):
        pass

    # Exit a parse tree produced by XMLParser#gov.
    def exitGov(self, ctx:XMLParser.GovContext):
        pass


    # Enter a parse tree produced by XMLParser#daocontent.
    def enterDaocontent(self, ctx:XMLParser.DaocontentContext):
        pass

    # Exit a parse tree produced by XMLParser#daocontent.
    def exitDaocontent(self, ctx:XMLParser.DaocontentContext):
        pass


    # Enter a parse tree produced by XMLParser#relations.
    def enterRelations(self, ctx:XMLParser.RelationsContext):
        pass

    # Exit a parse tree produced by XMLParser#relations.
    def exitRelations(self, ctx:XMLParser.RelationsContext):
        pass


    # Enter a parse tree produced by XMLParser#associated_to.
    def enterAssociated_to(self, ctx:XMLParser.Associated_toContext):
        pass

    # Exit a parse tree produced by XMLParser#associated_to.
    def exitAssociated_to(self, ctx:XMLParser.Associated_toContext):
        pass


    # Enter a parse tree produced by XMLParser#controlled_by.
    def enterControlled_by(self, ctx:XMLParser.Controlled_byContext):
        pass

    # Exit a parse tree produced by XMLParser#controlled_by.
    def exitControlled_by(self, ctx:XMLParser.Controlled_byContext):
        pass


    # Enter a parse tree produced by XMLParser#aggregates.
    def enterAggregates(self, ctx:XMLParser.AggregatesContext):
        pass

    # Exit a parse tree produced by XMLParser#aggregates.
    def exitAggregates(self, ctx:XMLParser.AggregatesContext):
        pass


    # Enter a parse tree produced by XMLParser#federates_into.
    def enterFederates_into(self, ctx:XMLParser.Federates_intoContext):
        pass

    # Exit a parse tree produced by XMLParser#federates_into.
    def exitFederates_into(self, ctx:XMLParser.Federates_intoContext):
        pass


    # Enter a parse tree produced by XMLParser#reference.
    def enterReference(self, ctx:XMLParser.ReferenceContext):
        pass

    # Exit a parse tree produced by XMLParser#reference.
    def exitReference(self, ctx:XMLParser.ReferenceContext):
        pass


    # Enter a parse tree produced by XMLParser#comments_and_stuff.
    def enterComments_and_stuff(self, ctx:XMLParser.Comments_and_stuffContext):
        pass

    # Exit a parse tree produced by XMLParser#comments_and_stuff.
    def exitComments_and_stuff(self, ctx:XMLParser.Comments_and_stuffContext):
        pass


    # Enter a parse tree produced by XMLParser#set_of_attributes.
    def enterSet_of_attributes(self, ctx:XMLParser.Set_of_attributesContext):
        pass

    # Exit a parse tree produced by XMLParser#set_of_attributes.
    def exitSet_of_attributes(self, ctx:XMLParser.Set_of_attributesContext):
        pass


    # Enter a parse tree produced by XMLParser#diagram_uniqueID.
    def enterDiagram_uniqueID(self, ctx:XMLParser.Diagram_uniqueIDContext):
        pass

    # Exit a parse tree produced by XMLParser#diagram_uniqueID.
    def exitDiagram_uniqueID(self, ctx:XMLParser.Diagram_uniqueIDContext):
        pass


    # Enter a parse tree produced by XMLParser#dao_id.
    def enterDao_id(self, ctx:XMLParser.Dao_idContext):
        pass

    # Exit a parse tree produced by XMLParser#dao_id.
    def exitDao_id(self, ctx:XMLParser.Dao_idContext):
        pass


    # Enter a parse tree produced by XMLParser#dao_name.
    def enterDao_name(self, ctx:XMLParser.Dao_nameContext):
        pass

    # Exit a parse tree produced by XMLParser#dao_name.
    def exitDao_name(self, ctx:XMLParser.Dao_nameContext):
        pass


    # Enter a parse tree produced by XMLParser#mission_statement.
    def enterMission_statement(self, ctx:XMLParser.Mission_statementContext):
        pass

    # Exit a parse tree produced by XMLParser#mission_statement.
    def exitMission_statement(self, ctx:XMLParser.Mission_statementContext):
        pass


    # Enter a parse tree produced by XMLParser#hierarchical_inheritance.
    def enterHierarchical_inheritance(self, ctx:XMLParser.Hierarchical_inheritanceContext):
        pass

    # Exit a parse tree produced by XMLParser#hierarchical_inheritance.
    def exitHierarchical_inheritance(self, ctx:XMLParser.Hierarchical_inheritanceContext):
        pass


    # Enter a parse tree produced by XMLParser#role_id.
    def enterRole_id(self, ctx:XMLParser.Role_idContext):
        pass

    # Exit a parse tree produced by XMLParser#role_id.
    def exitRole_id(self, ctx:XMLParser.Role_idContext):
        pass


    # Enter a parse tree produced by XMLParser#role_name.
    def enterRole_name(self, ctx:XMLParser.Role_nameContext):
        pass

    # Exit a parse tree produced by XMLParser#role_name.
    def exitRole_name(self, ctx:XMLParser.Role_nameContext):
        pass


    # Enter a parse tree produced by XMLParser#role_assignment_method.
    def enterRole_assignment_method(self, ctx:XMLParser.Role_assignment_methodContext):
        pass

    # Exit a parse tree produced by XMLParser#role_assignment_method.
    def exitRole_assignment_method(self, ctx:XMLParser.Role_assignment_methodContext):
        pass


    # Enter a parse tree produced by XMLParser#n_agent_min.
    def enterN_agent_min(self, ctx:XMLParser.N_agent_minContext):
        pass

    # Exit a parse tree produced by XMLParser#n_agent_min.
    def exitN_agent_min(self, ctx:XMLParser.N_agent_minContext):
        pass


    # Enter a parse tree produced by XMLParser#n_agent_max.
    def enterN_agent_max(self, ctx:XMLParser.N_agent_maxContext):
        pass

    # Exit a parse tree produced by XMLParser#n_agent_max.
    def exitN_agent_max(self, ctx:XMLParser.N_agent_maxContext):
        pass


    # Enter a parse tree produced by XMLParser#agent_type.
    def enterAgent_type(self, ctx:XMLParser.Agent_typeContext):
        pass

    # Exit a parse tree produced by XMLParser#agent_type.
    def exitAgent_type(self, ctx:XMLParser.Agent_typeContext):
        pass


    # Enter a parse tree produced by XMLParser#committee_id.
    def enterCommittee_id(self, ctx:XMLParser.Committee_idContext):
        pass

    # Exit a parse tree produced by XMLParser#committee_id.
    def exitCommittee_id(self, ctx:XMLParser.Committee_idContext):
        pass


    # Enter a parse tree produced by XMLParser#committee_description.
    def enterCommittee_description(self, ctx:XMLParser.Committee_descriptionContext):
        pass

    # Exit a parse tree produced by XMLParser#committee_description.
    def exitCommittee_description(self, ctx:XMLParser.Committee_descriptionContext):
        pass


    # Enter a parse tree produced by XMLParser#voting_condition.
    def enterVoting_condition(self, ctx:XMLParser.Voting_conditionContext):
        pass

    # Exit a parse tree produced by XMLParser#voting_condition.
    def exitVoting_condition(self, ctx:XMLParser.Voting_conditionContext):
        pass


    # Enter a parse tree produced by XMLParser#proposal_condition.
    def enterProposal_condition(self, ctx:XMLParser.Proposal_conditionContext):
        pass

    # Exit a parse tree produced by XMLParser#proposal_condition.
    def exitProposal_condition(self, ctx:XMLParser.Proposal_conditionContext):
        pass


    # Enter a parse tree produced by XMLParser#decision_making_method.
    def enterDecision_making_method(self, ctx:XMLParser.Decision_making_methodContext):
        pass

    # Exit a parse tree produced by XMLParser#decision_making_method.
    def exitDecision_making_method(self, ctx:XMLParser.Decision_making_methodContext):
        pass


    # Enter a parse tree produced by XMLParser#aggregation_level.
    def enterAggregation_level(self, ctx:XMLParser.Aggregation_levelContext):
        pass

    # Exit a parse tree produced by XMLParser#aggregation_level.
    def exitAggregation_level(self, ctx:XMLParser.Aggregation_levelContext):
        pass


    # Enter a parse tree produced by XMLParser#federation_level.
    def enterFederation_level(self, ctx:XMLParser.Federation_levelContext):
        pass

    # Exit a parse tree produced by XMLParser#federation_level.
    def exitFederation_level(self, ctx:XMLParser.Federation_levelContext):
        pass


    # Enter a parse tree produced by XMLParser#permission_id.
    def enterPermission_id(self, ctx:XMLParser.Permission_idContext):
        pass

    # Exit a parse tree produced by XMLParser#permission_id.
    def exitPermission_id(self, ctx:XMLParser.Permission_idContext):
        pass


    # Enter a parse tree produced by XMLParser#allowed_action.
    def enterAllowed_action(self, ctx:XMLParser.Allowed_actionContext):
        pass

    # Exit a parse tree produced by XMLParser#allowed_action.
    def exitAllowed_action(self, ctx:XMLParser.Allowed_actionContext):
        pass


    # Enter a parse tree produced by XMLParser#permission_type.
    def enterPermission_type(self, ctx:XMLParser.Permission_typeContext):
        pass

    # Exit a parse tree produced by XMLParser#permission_type.
    def exitPermission_type(self, ctx:XMLParser.Permission_typeContext):
        pass


    # Enter a parse tree produced by XMLParser#ref_gov_area.
    def enterRef_gov_area(self, ctx:XMLParser.Ref_gov_areaContext):
        pass

    # Exit a parse tree produced by XMLParser#ref_gov_area.
    def exitRef_gov_area(self, ctx:XMLParser.Ref_gov_areaContext):
        pass


    # Enter a parse tree produced by XMLParser#gov_area_ID.
    def enterGov_area_ID(self, ctx:XMLParser.Gov_area_IDContext):
        pass

    # Exit a parse tree produced by XMLParser#gov_area_ID.
    def exitGov_area_ID(self, ctx:XMLParser.Gov_area_IDContext):
        pass


    # Enter a parse tree produced by XMLParser#gov_area_description.
    def enterGov_area_description(self, ctx:XMLParser.Gov_area_descriptionContext):
        pass

    # Exit a parse tree produced by XMLParser#gov_area_description.
    def exitGov_area_description(self, ctx:XMLParser.Gov_area_descriptionContext):
        pass


    # Enter a parse tree produced by XMLParser#gov_area_implementation.
    def enterGov_area_implementation(self, ctx:XMLParser.Gov_area_implementationContext):
        pass

    # Exit a parse tree produced by XMLParser#gov_area_implementation.
    def exitGov_area_implementation(self, ctx:XMLParser.Gov_area_implementationContext):
        pass


    # Enter a parse tree produced by XMLParser#attribute.
    def enterAttribute(self, ctx:XMLParser.AttributeContext):
        pass

    # Exit a parse tree produced by XMLParser#attribute.
    def exitAttribute(self, ctx:XMLParser.AttributeContext):
        pass


    # Enter a parse tree produced by XMLParser#chardata.
    def enterChardata(self, ctx:XMLParser.ChardataContext):
        pass

    # Exit a parse tree produced by XMLParser#chardata.
    def exitChardata(self, ctx:XMLParser.ChardataContext):
        pass


    # Enter a parse tree produced by XMLParser#misc.
    def enterMisc(self, ctx:XMLParser.MiscContext):
        pass

    # Exit a parse tree produced by XMLParser#misc.
    def exitMisc(self, ctx:XMLParser.MiscContext):
        pass



del XMLParser