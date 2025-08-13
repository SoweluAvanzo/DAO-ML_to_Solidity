import src.model.enums.extended_enum as ext_enum

class UserFunctionalitiesGroupSize(ext_enum.ExtendedEnum):
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
    
    def to_maximum_size(self):
        return self.value[0]
    
    def get_mask_size(self):
        return self.value[1]
    
    def get_mask_id(self):
        id_mask = 1
        mask_size = self.get_mask_size()
        bit = 1
        for i in range(1, mask_size):
            bit <<= 1
            id_mask |= bit
        return id_mask
