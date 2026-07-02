from typing import Generator

import src.model.aggregable_entity as aggregable_entity
import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.governance_area as ga
import src.model.permission as p

import src.pipeline.pipeline_item as pi
import src.postprocessing.output_preparation.compilers.shared.templates.compiler_template_base_multipart as tb_m
# import src.postprocessing.output_preparation.compilers.shared.compiled_generic_data as cgd
import src.postprocessing.output_preparation.compilers.shared.templates.permissions_parts.recipe_permissions as r_p

import src.utilities.utils as u


class CompilerTemplateMultipartPermissionEnsamble(tb_m.CompilerTemplateBaseMultipart):
    """
    Compiler for Permissions, which also has the responsibility of deciding how to handle multiple permissions (assigned
    to a "permissions_holder", see the function "get_all_permissions_for").
    Multiple permissions might be collected inside a single output unit, or spread across multiple interconnected units
    (Solidity's Smart Contracts do have a size limit, so a system of Smart Contracts might be needed to spread the
    responsibilities), or even satisfy a recipe (or more?) that is efficiently defined to handle a very specific set
    of Permissions.

    This class might extend or make use of the class "CompilerTemplateMultipartPermissionParts".
    """

    def __init__(self, pipeline_item_data: pi.PIData,
                 optional_external_data=None,
                 # TODO: other things?
                 key_template_instance_data: str = None,
                 printer_debug: u.PrinterDebug = None
                 ):
        super().__init__(pipeline_item_data,
                         optional_external_data=optional_external_data,
                         key_template_instance_data=key_template_instance_data,
                         printer_debug=printer_debug
                         )

    def get_all_permissions_for(self, instance_data: dict, current_diagram: dm.DiagramManager, current_dao: d.DAO, permissions_holder: aggregable_entity.AggregableEntity | ga.GovernanceArea, additional_data=None) -> Generator[p.Permission, None, None]:
        """
        Extracts and returns all Permissions in this Permissions-holder (currently, 02/07/2026, Roles, Committees and even Governance Areas could have permissions)
        """
        pass

    def get_all_recipes(self, instance_data: dict, additional_data=None) -> Generator[r_p.RecipePermissions, None, None]:
        """
        Implementation notes: it could scan the "Templates/permissions/recipes" folder to fetch all recipes (either single
        files or group of files [identified by just the sub-folder's name]).
        The recipe list is inside an appropriated "recipe.json" file.


        Might make use of a "set-trie", described here: https://github.com/BBVA/mercury-settrie
        """
        pass

    def get_recipes_for(self, instance_data: dict, bag_of_permissions: dict[str, p.Permission], additional_data=None) -> Generator[r_p.RecipePermissions, None, None]:
        # TODO: make use of the data structure used by the function "get_all_recipes"
        pass
