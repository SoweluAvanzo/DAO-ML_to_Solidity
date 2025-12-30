
from antlr4 import CommonTokenStream, InputStream
from antlr4.tree.Tree import TerminalNodeImpl

import src.pipeline.pipeline_item as pi

import src.parsers.xml.XMLLexer as xmlL
import src.parsers.xml.XMLParser as xmlP
import src.parsers.xml.XMLParserVisitor as xmlPV
import src.validators.validation_result as validation_res

import src.model_generators.base_generator as bg
import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.governance_area as ga
import src.model.role as r
import src.model.committee as c
import src.model.permission as p
import src.model.enums.relation_type as r_t

import src.utilities.utils as u


class XmlStringModelGenerator(bg.BaseGenerator):
    def __init__(self, pipeline_item_data: pi.PIData,
                 printer_debug: u.PrinterDebug = None
                 ):
        super().__init__(pipeline_item_data,
                         printer_debug=printer_debug
                         )

    def new_XMLDAOVisitor(self):
        return XMLDAOVisitor(printer_debug=self.printer_debug)

    def generate(self, validation_result, additional_data=None):
        try:
            if not isinstance(validation_result, validation_res.ValidationResult):
                raise Exception(
                    f"Unrecognized validation result type: expected ValidationResult, got: {type(validation_result)}.")

            # errors=validation_result["errors"]
            # tree_parsed=validation_result["tree_parsed"]
            input_consumed = validation_result.input_consumed
            # input_string_list=validation_result["input_string_list"]

            # setup of the parser
            # buffer # StringIO(text_wrapper.read())
            xml_content_as_stream = InputStream(input_consumed)
            lexer = xmlL.XMLLexer(xml_content_as_stream)
            stream = CommonTokenStream(lexer)
            parser = xmlP.XMLParser(stream)
            tree = parser.document()

            # actual transformation
            visitor = self.new_XMLDAOVisitor()
            diagram_manager = dm.DiagramManager()
            visitor.parseDiagramTree(tree, diagram_manager)
            return diagram_manager
        except Exception as e:
            self.print_error("\nERROR while generating Model")
            self.print_error(e)
            self.print_error("\n")
            return None


class XMLDAOVisitor(xmlPV.XMLParserVisitor):
    def __init__(self, printer_debug: u.PrinterDebug = None):
        self.current_dao = None
        self.translation_results = []
        self.diagramManager: dm.DiagramManager = None
        self.printer_debug = printer_debug

    def print_error(self, msg):
        if self.printer_debug is not None:
            self.printer_debug.print_error(msg)

    def print_msg(self, msg):
        if self.printer_debug is not None:
            self.printer_debug.print_msg(msg)

    def parseDiagramTree(self, tree, diagramManager: dm.DiagramManager):
        self.diagramManager = diagramManager
        self.print_msg("starting parsing diagram tree")
        # at first, gather all the data (raw instances) through the "visitABC" methods into the "diagramManager" ...
        self.visit(tree)
        # ... then, process and "link" all the raw data
        diagramManager.processRawInstances()
        self.diagramManager = None  # just to clean the memory

    def _text_from_node(self, node) -> str:
        return node.STRING().getText().strip('"')

    def visitDiagram(self, ctx: xmlP.XMLParser.DiagramContext):
        self.print_msg("\n\nXML..........visitDiagram ^^ ")
        uniqueID = self._text_from_node(ctx.diagram_uniqueID()[0])
        self.diagramManager.id = uniqueID
        self.print_msg(f"Diagram uniqueID: {uniqueID}")
        return super().visitDiagram(ctx)

    def visitRole(self, ctx: xmlP.XMLParser.RoleContext):
        role_id = self._text_from_node(ctx.role_id()[0])
        role_name = self._text_from_node(ctx.role_name()[0])
        role_assignment_method = self._text_from_node(ctx.role_assignment_method()[0]) \
            if len(ctx.role_assignment_method()) > 0 and ctx.role_assignment_method()[0] \
            else None
        n_agent_min = int(self._text_from_node(ctx.n_agent_min()[0])) \
            if len(ctx.n_agent_min()) > 0 and ctx.n_agent_min()[0]\
            else None
        n_agent_max = int(self._text_from_node(ctx.n_agent_max()[0])) \
            if len(ctx.n_agent_max()) > 0 and ctx.n_agent_max()[0]\
            else None
        agent_type = self._text_from_node(ctx.agent_type()[0]) \
            if len(ctx.agent_type()) > 0 else None
        role = r.Role(
            role_id,
            role_name,
            role_assignment_method,
            n_agent_min,
            n_agent_max,
            agent_type
        )
        self.diagramManager.addRole(self.current_dao, role)
        return self.visitChildren(ctx)

    def visitCommittee(self, ctx):
        committee_id = self._text_from_node(ctx.committee_id()[0])
        committee_description = self._text_from_node(
            ctx.committee_description()[0])
        voting_condition = self._text_from_node(ctx.voting_condition()[0]) \
            if len(ctx.voting_condition()) > 0 and ctx.voting_condition()[0] \
            else None
        proposal_condition = self._text_from_node(ctx.proposal_condition()[0]) \
            if len(ctx.proposal_condition()) > 0 and ctx.proposal_condition()[0] \
            else None
        decision_making_method = self._text_from_node(ctx.decision_making_method()[0]) \
            if len(ctx.decision_making_method()) > 0 and ctx.decision_making_method()[0] \
            else None
        committee = c.Committee(
            committee_id,
            committee_description,
            voting_condition,
            proposal_condition,
            decision_making_method
        )
        self.diagramManager.addCommittee(self.current_dao, committee)
        return self.visitChildren(ctx)

    def visitPermission(self, ctx):
        permission_id = self._text_from_node(ctx.permission_id()[0])
        allowed_action = self._text_from_node(ctx.allowed_action()[0])
        permission_type = self._text_from_node(ctx.permission_type()[0]) \
            if len(ctx.permission_type()) > 0 \
            else None
        ref_gov_area = self._text_from_node(ctx.ref_gov_area()[0]) \
            if len(ctx.ref_gov_area()) > 0 and ctx.ref_gov_area()[0] \
            else None
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
        return self._text_from_node(beholderID)

    def visitRelations(self, ctx):
        # visits associated to relations and stores them in the dictionary
        if ctx.associated_to():
            for assoc in ctx.associated_to():
                content = self.aggregate_texts(assoc.content().chardata())
                id = self.__extract_ID(ctx.parentCtx)
                self.diagramManager.addRelation(
                    self.current_dao,
                    r_t.RelationType.ASSOCIATION,
                    id,
                    content
                )
        if ctx.controlled_by():
            for control in ctx.controlled_by():
                content = self.aggregate_texts(control.content().chardata())
                id = self.__extract_ID(ctx.parentCtx)
                self.diagramManager.addRelation(
                    self.current_dao,
                    r_t.RelationType.CONTROL,
                    id,
                    content
                )
        if ctx.aggregates():
            for aggregated in ctx.aggregates():
                content = self.aggregate_texts(aggregated.content().chardata())
                id = self.__extract_ID(ctx.parentCtx)
                self.diagramManager.addRelation(
                    self.current_dao,
                    r_t.RelationType.AGGREGATION,
                    id,
                    content
                )
        if ctx.federates_into():
            for federated in ctx.federates_into():
                content = self.aggregate_texts(federated.content().chardata())
                id = self.__extract_ID(ctx.parentCtx)
                self.diagramManager.addRelation(
                    self.current_dao,
                    r_t.RelationType.FEDERATION,
                    id,
                    content
                )
        return self.visitChildren(ctx)

    def visitDao(self, ctx):
        dao_id = self._text_from_node(ctx.dao_id()[0])
        dao_name = self._text_from_node(ctx.dao_name()[0])
        mission_statement = self._text_from_node(ctx.mission_statement()[0]) \
            if len(ctx.mission_statement()) > 0 \
            else None
        hierarchical_inheritance = self._text_from_node(
            ctx.hierarchical_inheritance()[0])
        dao = d.DAO(
            dao_id,
            dao_name,
            mission_statement,
            hierarchical_inheritance
        )
        # self.daos[dao_id] = dao
        self.diagramManager.addDao(dao)
        self.print_msg(f'DAO created with ID: {dao_id}')
        # recursively visits the children of the dao
        self.current_dao = dao
        self.visitChildren(ctx)
        self.print_msg("visitDao completed")
        self.current_dao = None
        return dao

    def visitGov(self, ctx: xmlP.XMLParser.GovContext):
        gov_area_ID = self._text_from_node(ctx.gov_area_ID()[0])
        gov_area_description = self._text_from_node(
            ctx.gov_area_description()[0])
        gov_area_implementation = self._text_from_node(
            ctx.gov_area_implementation()[0])
        self.print_msg(
            f"visitGov: gov_area_ID: {gov_area_ID} --- gov_area_description: {gov_area_description}")
        governance_area = ga.GovernanceArea(
            gov_area_ID,
            gov_area_description,
            gov_area_implementation
        )
        self.diagramManager.addGovernanceArea(
            self.current_dao, governance_area)
        return self.visitChildren(ctx)

    def aggregate_texts(self, chardata_list, separator=""):
        return (separator if separator else "").join([node.getText().strip() for node in chardata_list])

    def __str__(self):
        raise Exception("should not be invoked")

    def get_translation_summary(self):
        return str(self)

    def traverse_parsing_tree_debug(self, tree, rule_names, indent=0):
        """
        Originally used  to just debug the parsed tree, now unused
        """
        if self.printer_debug is None:
            # print("ERROR: CAN'T DEBUG using the method \"traverse_parsing_tree_debug\" because no printer_debug is found")
            self.printer_debug = u.PrinterDebug()
        if tree.getText() == "<EOF>":
            return
        elif isinstance(tree, TerminalNodeImpl):
            self.print_msg(
                "{0}TOKEN='{1}'".format("\t" * indent, tree.getText()))
        else:
            self.print_msg("{0}{1}".format(
                "\t" * indent, rule_names[tree.getRuleIndex()]))
            for child in tree.children:
                self.traverse_parsing_tree_debug(child, rule_names, indent + 1)
