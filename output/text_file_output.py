
from collections.abc import Iterable
import output.base_output as bo
import files.file_utils as fu

class TextFileOutput(bo.BaseOutput):
    def __init__(self, base_destination=None):
        self.base_destination = base_destination

    def to_output(self, what, destination:str=None, additional_data=None) -> bool:
        if destination is None:
            destination = fu.get_base_folder(self.base_destination)
        if destination is None: #again?
            return False
        is_write = True
        if additional_data is not None:
            if 'write' in additional_data:
                is_write = (additional_data['write'] == True) or (additional_data['write'] == 'w') 
            elif 'mode' in additional_data:
                is_write = (additional_data['mode'] == True) or (additional_data['mode'] == 'w') 
        with open(destination, 'w' if is_write else 'a') as f:
            if isinstance(what, str):
                f.write(what)
                f.flush()
            elif isinstance(what, list) or hasattr(what, '__iter__') or isinstance(what, Iterable):
                for w in what:
                    f.write(w)
                    f.write("\n")
                    f.flush()
            else:
                #try to iterate -> it's the pythonic way to check it
                try:
                    for w in what:
                        f.write(w)
                        f.write("\n")
                        f.flush()
                except TypeError: # then, fail gracefully
                    f.write(what)
                    f.flush()
            return True
        return False
    
    def to_file(self, lines, folder_path, filename, extension, mode='w'):
        if folder_path is None:
            folder_path = fu.get_base_folder()
        else:
            fu.check_and_make_folder(folder_path)
        full_path = fu.concat_folder_filename(folder_path, f"{filename}.{extension}")
        return self.to_output(lines, full_path, {"mode": mode})
