from io import StringIO

class BaseEntity:
    def __init__(self, id) -> None:
        self.id = id

    def get_id(self):
        return self.id

    def toJSON(self):
        return {
            "id": self.id
        }

    def __str__(self, more_stuff=None):
        string_builder = StringIO()

        string_builder.write(self.__class__.__name__)
        string_builder.write('(')
        string_builder.write('id=')
        string_builder.write(f"{self.id}")

        if (more_stuff is not None) and isinstance(more_stuff, str):
            string_builder.write(', ')
            string_builder.write(more_stuff)

        string_builder.write(')')
        return string_builder.getvalue()
    
    def __repr__(self):
        return self.toJSON()