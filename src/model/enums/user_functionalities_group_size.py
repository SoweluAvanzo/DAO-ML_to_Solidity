from enum import Enum

class UserFunctionalitiesGroupSize(Enum):
    SMALL = (32,5)
    MEDIUM = (64,6)
    LARGE = (128,7)
    EXTRA_LARGE = (256,8)
    def from_size(size):
        if size <= 32:
            return UserFunctionalitiesGroupSize.SMALL
        elif size <= 64:
            return UserFunctionalitiesGroupSize.MEDIUM
        elif size <= 128:
            return UserFunctionalitiesGroupSize.LARGE
        elif size <= 256:
            return UserFunctionalitiesGroupSize.EXTRA_LARGE
        else:
            return None
