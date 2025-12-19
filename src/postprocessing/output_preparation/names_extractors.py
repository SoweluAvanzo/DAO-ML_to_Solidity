import src.pipeline.pipeline_item as pi

import src.model.diagram_manager as dm
import src.model.dao as d

import src.utilities.utils as u


class NamesExtracted:
    def __init__(self):
        self.diagram_name: str = None
        self.daos_names_by_dao_id: dict[str, str] = None


class NamesExtractor(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData,
                 printer_debug: u.PrinterDebug = None,
                 key_diagram_model: str = None
                 ):
        super().__init__(
            pipeline_item_data,
            printer_debug=printer_debug
        )
        self.key_diagram_model = key_diagram_model

    def extract_dao_name(self, diagram: dm.DiagramManager, dao: d.DAO) -> str:
        return u.to_keyword(dao.get_name(), to_lower=False)

    def extract_diagram_name(self, diagram: dm.DiagramManager) -> str:
        return u.to_keyword(diagram.get_name(), to_lower=False)

    def run(self, inputs) -> NamesExtracted:
        if inputs is None:
            raise Exception(
                f"Input is None in {type(self)} with key: {self.get_key()}")
        diagram: dm.DiagramManager = None
        d_i = self.get_ith_input(inputs, 0) \
            if self.key_diagram_model is None else \
            inputs[self.key_diagram_model]
        if not isinstance(d_i, dm.DiagramManager):
            raise Exception(f"Expected a DiagramManager, got: {type(d_i)}")
        diagram = d_i
        ne = NamesExtracted()
        ne.diagram_name = self.extract_diagram_name(diagram)
        ne.daos_names_by_dao_id = {
            dao_id: self.extract_dao_name(diagram, dao)
            for dao_id, dao in diagram.daoByID.items()
        }
        return ne
