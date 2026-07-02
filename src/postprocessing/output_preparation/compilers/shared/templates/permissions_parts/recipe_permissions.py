
import src.model.permission as p


class RecipePermissions:
    """
    Defines an already-precompiled parts that is optimized for a set of Permissions (a "recipe"): rather then assembling all
    Permissions into a single object naively (for example, a single huge Smart Contract, or multiple Smart Contracts filled
    with ways to allow them to properly communicate as a single unit), a fine-tuned solution could be desirable.
    More accurately, at the current stage of development (02/07/2026), this class just defines the recipe list.
    """

    def __init__(self,
                 permission_names: list[str] = None
                 ):
        self.permission_names = permission_names
