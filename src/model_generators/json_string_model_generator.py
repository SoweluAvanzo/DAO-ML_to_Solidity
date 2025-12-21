import json

import src.pipeline.pipeline_item as pi
import src.model_generators.base_generator as bg

import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.committee as c
import src.model.role as r
import src.model.permission as p
import src.model.governance_area as ga
import src.model.relation as rel
import src.model.enums.relation_type as rt

import src.utilities.utils as u

VERSION = "1.0.0"


class JsonStringModelGenerator(bg.BaseGenerator):
    def __init__(self, pipeline_item_data: pi.PIData,
                 printer_debug: u.PrinterDebug = None
                 ):
        super().__init__(pipeline_item_data,
                         printer_debug=printer_debug
                         )
        # self._diagram_fields_optionality: dict[str, bool] = None  # lazy
        # self._dao_fields_optionality: dict[str, bool] = None  # lazy
        # self._committee_fields_optionality: dict[str, bool] = None  # lazy
        # self._role_fields_optionality: dict[str, bool] = None  # lazy
        # self._permission: dict[str, bool] = None  # lazy
        # self._gov: dict[str, bool] = None  # lazy
        # lazy
        self._fields_mandatority_by_classname: dict[str, dict[str, bool]] = {}

    def generate(self, data, additional_input=None):
        try:
            data_obj: dict = data
            is_string = u.is_string_or_list(data)
            if is_string:
                data_obj = json.loads(data)
            elif is_string != None:
                # list
                data_obj = json.loads("".join(data))
            return self.parseDiagram(data_obj)
        except Exception as e:
            print(e)
        return None

    def _exception_missing_data(self, what, where, add_msg: str = None):
        raise Exception(
            f"Missing {what} field(s) in class {where}!{'' if add_msg is None else add_msg}")

    def check_fields(self, obj: dict, fields: dict[str, bool], className: str, add_msg: str = None) -> bool:
        missing = []
        optional_f = []
        for f, is_mandatory in fields.items():
            if f not in obj:
                if is_mandatory:
                    missing.append(f)
                else:
                    optional_f.append(f)
        optional_msg = None if len(optional_f) == 0 else \
            f"[{', '.join(optional_f)}] fields were optional."
        if len(missing) == 0:
            if optional_msg is not None:
                self.print_msg(f"In class {className}, {optional_msg}")
            return True
        self._exception_missing_data(f"[{', '.join(missing)}]{'' if optional_msg is None else f' ({optional_msg})'})",
                                     className, add_msg=add_msg)
        return False

    def _fields_of(self, clazz: type) -> dict[str, bool]:
        class_name: str = clazz.__name__
        if class_name in self._fields_mandatority_by_classname:
            self._fields_mandatority_by_classname[class_name]
        fields = self._fields_of_by_class_name(clazz, class_name)
        self._fields_mandatority_by_classname[class_name] = fields
        return fields

    #
    # Override-designed
    #

    def _fields_of_by_class_name(self, clazz: type, class_name: str) -> dict[str, bool]:
        """
        Override-designed
        """
        fields: dict[str, bool] = None
        # not using "match" because it needs constant values
        # in decreasing order of encounter-frequencies
        # TODO altre classi in model
        if issubclass(clazz, rel.Relation):
            fields = self._fields_of_relation()
        elif issubclass(clazz, d.DAO):
            fields = self._fields_of_dao()
        elif issubclass(clazz, dm.DiagramManager):
            fields = self._fields_of_diagram()
        return fields

    def _fields_of_diagram(self):
        """
        Override-designed
        """
        return {
            "id": True,
            "daoByID": True,
            "relations_by_dao": True,
            "controlGraphGenerator": False
        }

    def _fields_of_relation(self):
        """
        Override-designed
        """
        return {
            "dao_id": False,
            "relation_type": True,
            "from_id": True,
            "content": True
        }

    def _fields_of_dao(self):
        """
        Override-designed
        """
        return {
            "id": True,
            # TODO
        }

    def _parse_relations_by_dao(self, data_obj: dict, daos_by_id: dict[str, d.DAO]):
        rbd: dict[str, list[rel.Relation]] = {}
        rbd_data = data_obj["relations_by_dao"]
        expected_relation_fields = self._fields_of(rel.Relation)
        for dao_id, l in rbd_data.items():
            if dao_id not in daos_by_id:
                raise Exception(f"Missing DAO (id: {dao_id})")
            index_relation = 0
            relations: list[rel.Relation] = []
            for relation in l:
                self.check_fields(
                    relation, expected_relation_fields,
                    rel.Relation.__class__.__name__,
                    add_msg=f"Relation # {index_relation} of DAO (id): {dao_id}"
                )
                relations.append(
                    rel.Relation(
                        dao_id,
                        rt.RelationType[relation["relation_type"]],
                        relation["from_id"],
                        relation["content"]
                    )
                )
                index_relation += 1
            rbd[dao_id] = relations
        return rbd

    def parseDiagram(self, data_obj) -> dm.DiagramManager:
        fields_mandatority: dict[str, bool] = self._fields_of(
            dm.DiagramManager
        )
        self.check_fields(data_obj, fields_mandatority,
                          dm.DiagramManager.__class__.__name__)
        # the parsing
        diagram = dm.DiagramManager()
        diagram.id = data_obj["id"]
        # ... daos
        daos_by_id: dict[str, d.DAO] = {}
        # TODO
        diagram.daoByID = daos_by_id
        # ... relations_by_dao
        diagram.relations_by_dao = self._parse_relations_by_dao(
            data_obj, daos_by_id)
        return diagram
