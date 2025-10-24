
from antlr4 import CommonTokenStream, InputStream
from antlr4.tree.Tree import TerminalNodeImpl

import src.pipeline.pipeline_item as pi

import src.parsers.xml.XMLLexer as xmlL
import src.parsers.xml.XMLParser as xmlP
import src.parsers.xml.XMLParserVisitor as xmlPV
import src.validators.validation_result as validation_res

import src.model_generators.base_generator as bg
# import src.utilities.utils as u
import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.governance_area as ga
import src.model.role as r
import src.model.committee as c
import src.model.permission as p
import src.model.enums.relation_type as r_t


class XmlStringModelGenerator(bg.BaseGenerator):
    def __init__(self, pipeline_item_data: pi.PIData):
        super().__init__(pipeline_item_data)

    def generate(self, validation_result):
        try:
            if not isinstance(validation_result, validation_res.ValidationResult):
                raise Exception(
                    f"Unrecognized validation result type: expected ValidationResult, got: {type(validation_result)}.")

            # errors=validation_result["errors"]
            # tree_parsed=validation_result["tree_parsed"]
            input = validation_result.input
            # input_string_list=validation_result["input_string_list"]

            # setup of the parser
            # buffer # StringIO(text_wrapper.read())
            xml_content_as_stream = InputStream(input)
            lexer = xmlL.XMLLexer(xml_content_as_stream)
            stream = CommonTokenStream(lexer)
            parser = xmlP.XMLParser(stream)
            tree = parser.document()

            # actual transformation
            visitor = XMLDAOVisitor()
            diagram_manager = dm.DiagramManager()
            visitor.parseDiagramTree(tree, diagram_manager)
            return diagram_manager
        except Exception as e:
            print("\nERROR while generating Model")
            print(e)
            print("\n")
            return None


class XMLDAOVisitor(xmlPV.XMLParserVisitor):
    def __init__(self):
        self.current_dao = None
        self.translation_results = []
        self.diagramManager: dm.DiagramManager = None

    def parseDiagramTree(self, tree, diagramManager: dm.DiagramManager):
        self.diagramManager = diagramManager
        # at first, gather all the data (raw instances) through the "visitABC" methods into the "diagramManager" ...
        self.visit(tree)
        # ... then, process and "link" all the raw data
        diagramManager.processRawInstances()
        self.diagramManager = None  # just to clean the memory

    def visitDiagram(self, ctx: xmlP.XMLParser.DiagramContext):
        print("..........visitDiagram ^^ ")
        uniqueID = ctx.diagram_uniqueID()[0].STRING().getText().strip('"')
        self.diagramManager.id = uniqueID
        self.diagramManager.uniqueID = uniqueID
        print(f"Diagram uniqueID: {uniqueID}")
        return super().visitDiagram(ctx)

    def visitRole(self, ctx: xmlP.XMLParser.RoleContext):
        role_id = ctx.role_id()[0].STRING().getText().strip('"')
        role_name = ctx.role_name()[0].STRING().getText().strip('"')
        role_assignment_method = ctx.role_assignment_method()[0].STRING().getText().strip(
            '"') if len(ctx.role_assignment_method()) > 0 and ctx.role_assignment_method()[0] else None
        n_agent_min = ctx.n_agent_min()[0].STRING().getText().strip('"') if len(
            ctx.n_agent_min()) > 0 and ctx.n_agent_min()[0] else None
        n_agent_max = ctx.n_agent_max()[0].STRING().getText().strip('"') if len(
            ctx.n_agent_max()) > 0 and ctx.n_agent_max()[0] else None
        agent_type = ctx.agent_type()[0].STRING().getText().strip(
            '"') if len(ctx.agent_type()) > 0 else None
        role = r.Role(role_id, role_name, role_assignment_method,
                      n_agent_min, n_agent_max, agent_type)
        self.diagramManager.addRole(self.current_dao, role)
        return self.visitChildren(ctx)

    def visitCommittee(self, ctx):
        committee_id = ctx.committee_id()[0].STRING().getText().strip('"')
        committee_description = ctx.committee_description()[
            0].STRING().getText().strip('"')
        voting_condition = ctx.voting_condition()[0].STRING().getText().strip(
            '"') if len(ctx.voting_condition()) > 0 and ctx.voting_condition()[0] else None
        proposal_condition = ctx.proposal_condition()[0].STRING().getText().strip(
            '"') if len(ctx.proposal_condition()) > 0 and ctx.proposal_condition()[0] else None
        decision_making_method = ctx.decision_making_method()[0].STRING().getText().strip(
            '"') if len(ctx.decision_making_method()) > 0 and ctx.decision_making_method()[0] else None
        committee = c.Committee(committee_id, committee_description,
                                voting_condition, proposal_condition, decision_making_method)
        self.diagramManager.addCommittee(self.current_dao, committee)
        return self.visitChildren(ctx)

    def visitPermission(self, ctx):
        permission_id = ctx.permission_id()[0].STRING().getText().strip('"')
        allowed_action = ctx.allowed_action()[0].STRING().getText().strip('"')
        permission_type = ctx.permission_type()[0].STRING().getText().strip(
            '"') if len(ctx.permission_type()) > 0 else None
        ref_gov_area = ctx.ref_gov_area()[0].STRING().getText().strip('"') if len(
            ctx.ref_gov_area()) > 0 and ctx.ref_gov_area()[0] else None
        permission = p.Permission(
            permission_id, allowed_action, permission_type, ref_gov_area)
        self.diagramManager.addPermission(self.current_dao, permission)
        return self.visitChildren(ctx)

    def __extract_ID(self, node) -> str:
        beholderID = None
        if hasattr(node, 'role_id') and callable(getattr(node, 'role_id')):
            beholderID = node.role_id()[0]
        if hasattr(node, 'committee_id') and callable(getattr(node, 'committee_id')):
            beholderID = node.committee_id()[0]
        if beholderID is None:
            raise Exception("can't extract an id")
        return beholderID.STRING().getText().strip('"')

    def visitRelations(self, ctx):
        # visits associated to relations and stores them in the dictionary
        if ctx.associated_to():
            for assoc in ctx.associated_to():
                content = self.aggregate_texts(assoc.content().chardata())
                id = self.__extract_ID(ctx.parentCtx)
                self.diagramManager.addRelation(
                    self.current_dao, r_t.RelationType.ASSOCIATION, id, content)
        if ctx.controlled_by():
            for control in ctx.controlled_by():
                content = self.aggregate_texts(control.content().chardata())
                id = self.__extract_ID(ctx.parentCtx)
                self.diagramManager.addRelation(
                    self.current_dao, r_t.RelationType.CONTROL, id, content)
        if ctx.aggregates():
            for aggregated in ctx.aggregates():
                content = self.aggregate_texts(aggregated.content().chardata())
                id = self.__extract_ID(ctx.parentCtx)
                self.diagramManager.addRelation(
                    self.current_dao, r_t.RelationType.AGGREGATION, id, content)
        if ctx.federates_into():
            for federated in ctx.federates_into():
                content = self.aggregate_texts(federated.content().chardata())
                id = self.__extract_ID(ctx.parentCtx)
                self.diagramManager.addRelation(
                    self.current_dao, r_t.RelationType.FEDERATION, id, content)
        return self.visitChildren(ctx)

    def visitDao(self, ctx):
        dao_id = ctx.dao_id()[0].STRING().getText().strip('"')
        dao_name = ctx.dao_name()[0].STRING().getText().strip('"')
        mission_statement = ctx.mission_statement()[0].STRING().getText().strip(
            '"') if len(ctx.mission_statement()) > 0 else None
        hierarchical_inheritance = ctx.hierarchical_inheritance()[
            0].STRING().getText().strip('"')
        dao = d.DAO(dao_id, dao_name, mission_statement,
                    hierarchical_inheritance)
        # self.daos[dao_id] = dao
        self.diagramManager.addDao(dao)
        print(f'DAO created with ID: {dao_id}')
        # recursively visits the children of the dao
        self.current_dao = dao
        self.visitChildren(ctx)
        print("visitDao completed")
        self.current_dao = None
        return dao

    def visitGov(self, ctx: xmlP.XMLParser.GovContext):
        gov_area_ID = ctx.gov_area_ID()[0].STRING().getText().strip('"')
        gov_area_description = ctx.gov_area_description()[
            0].STRING().getText().strip('"')
        gov_area_implementation = ctx.gov_area_implementation()[
            0].STRING().getText().strip('"')
        print(
            f"visitGov: gov_area_ID: {gov_area_ID} --- gov_area_description: {gov_area_description}")
        governance_area = ga.GovernanceArea(
            gov_area_ID, gov_area_description, gov_area_implementation)
        self.diagramManager.addGovernanceArea(
            self.current_dao, governance_area=governance_area)
        return self.visitChildren(ctx)

    def aggregate_texts(self, chardata_list, separator=""):
        return (separator if separator else "").join([node.getText().strip() for node in chardata_list])

    def __str__(self):
        raise Exception("should not be invoked")

    def get_translation_summary(self):
        return str(self)


def traverse(tree, rule_names, indent=0):
    if tree.getText() == "<EOF>":
        return
    elif isinstance(tree, TerminalNodeImpl):
        print("{0}TOKEN='{1}'".format("\t" * indent, tree.getText()))
    else:
        print("{0}{1}".format("\t" * indent, rule_names[tree.getRuleIndex()]))
        for child in tree.children:
            traverse(child, rule_names, indent + 1)
