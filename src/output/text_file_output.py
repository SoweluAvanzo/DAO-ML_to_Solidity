
from collections.abc import Iterable
import src.output.base_output as bo
import src.files.file_utils as fu
import src.pipeline.pipeline_item as pi

NEW_LINE_CHARS = ("\n", "\r")
WRITE_MODE_KEY = "write"
WRITE_MODE_VALUES = {"true", "w", "write", "y", "yes", "t", 1, "1"}


class TextFileOutput(bo.BaseOutput):
    def __init__(self, pipeline_item_data: pi.PIData, base_destination=None, write_mode_key: str = None):
        super().__init__(pipeline_item_data, base_destination)
        self.write_mode_key = WRITE_MODE_KEY if write_mode_key is None else write_mode_key

    def to_output(self, what, destination: str = None, additional_data=None) -> bool:
        print(f"to_output with what of type: {type(what)}")
        print(f"... at: {destination}")
        print(f"... with additional data: {additional_data}")
        if destination is None:
            destination = fu.get_base_folder(self.base_destination)
        if destination is None:  # again?
            return False
        is_write = True
        if additional_data is not None:
            for wmk in {WRITE_MODE_KEY, "mode", self.write_mode_key}:
                if wmk in additional_data:
                    wm = additional_data[wmk]
                    is_write = (wm == True) or \
                        (isinstance(wm, str) and
                         (wm.strip().lower() in WRITE_MODE_VALUES)) \
                        or (wm in WRITE_MODE_VALUES)
                    break
        folder_destination = fu.extract_folder_from_full_path(destination)
        fu.check_and_make_folder(folder_destination)
        with open(destination, 'w' if is_write else 'a') as f:
            if isinstance(what, str):
                f.write(what)
                f.flush()
            elif isinstance(what, list) or hasattr(what, '__iter__') or isinstance(what, Iterable):
                for w in what:
                    f.write(w)
                    if isinstance(w, str) and (not w.endswith(NEW_LINE_CHARS)):
                        f.write("\n")
                    f.flush()
            else:
                # try to iterate -> it's the pythonic way to check it
                try:
                    for w in what:
                        f.write(w)
                        if isinstance(w, str) and (not w.endswith(NEW_LINE_CHARS)):
                            f.write("\n")
                        f.flush()
                except TypeError:  # then, fail gracefully
                    f.write(what)
                    f.flush()
            return True
        return False

    def to_file(self, lines, folder_path, filename, extension, mode='w'):
        if folder_path is None:
            folder_path = fu.get_base_folder()
        else:
            fu.check_and_make_folder(folder_path)
        full_path = fu.concat_folder_filename(
            folder_path, f"{filename}.{extension}")
        return self.to_output(lines, full_path, {"mode": mode})
