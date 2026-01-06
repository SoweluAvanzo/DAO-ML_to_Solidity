import src.pipeline.pipeline_item as pi
import src.validators.base_validator as bv


import src.model.base_entity as be
import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.committee as c
import src.model.aggregable_entity as ae
import src.model.role as r
import src.model.permission as p
import src.model.governance_area as ga
import src.model.relation as rel
import src.model.enums.relation_type as rt

import src.control_graph.control_graph_basic as cgb


class JSONValidator(bv.BaseValidator):

    def validate(self, input_to_validate: dict) -> bool:
        raise Exception("TODO : NOTHING TO BE IMPLEMENTED (05-01-2026)")
