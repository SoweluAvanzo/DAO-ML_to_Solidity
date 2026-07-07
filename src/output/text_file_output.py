import json
from collections.abc import Iterable

import src.pipeline.pipeline_item as pi


import src.output.base_output as bo

import src.files.file_utils as fu
import src.utilities.utils as u

NEW_LINE_CHARS = ("\n", "\r")
KEY_OPEN_FILE_MODE = "mode"
MODE_VALUES_WRITE_array = ["w", "true", "write", "y", "yes", "t", 1, "1"]
MODE_VALUES_WRITE = set(MODE_VALUES_WRITE_array)
MODE_VALUES_APPEND_array = ["a", "false", "append", "n", "no", "f", 0, "0"]
MODE_VALUES_APPEND = set(MODE_VALUES_APPEND_array)


class TextFileOutput(bo.BaseOutput):
    def __init__(self, pipeline_item_data: pi.PIData,
                 printer_debug: u.PrinterDebug = None,
                 write_mode_key: str = None,
                 key_base_destination: str = None,
                 key_filename_extension: str = None
                 ):
        super().__init__(
            pipeline_item_data,
            printer_debug=printer_debug,
        )
        self.key_base_destination = key_base_destination
        self.key_filename_extension = key_filename_extension
        self.write_mode_key = KEY_OPEN_FILE_MODE if write_mode_key is None else write_mode_key

    def compose_full_path_destination(self, base_destination: str, filename_extension: str) -> str:
        """
        Override-designed
        """
        return fu.concat_folder_filename(base_destination, filename_extension)

    def to_output(self, what, additional_data: dict) -> bool:
        if additional_data is None:
            raise Exception(
                f"Can't produce a text output without additional information (additional_data is None) in class ({type(self)}) with key: {self.get_key()}")
        if self.key_base_destination is None:
            raise Exception(
                f"key_base_destination is None in class ({type(self)}) with key: {self.get_key()}")
        if self.key_base_destination not in additional_data:
            raise Exception(
                f"key_base_destination ({self.key_base_destination}) not in additional_data in class ({type(self)}) with key: {self.get_key()}")
        if self.key_filename_extension is None:
            raise Exception(
                f"key_filename_extension is None in class ({type(self)}) with key: {self.get_key()}")
        if self.key_filename_extension not in additional_data:
            raise Exception(
                f"key_filename_extension ({self.key_filename_extension}) not in additional_data in class ({type(self)}) with key: {self.get_key()}")
        base_destination: str = additional_data[self.key_base_destination]
        if base_destination is None:
            base_destination = fu.get_base_folder(None)
        if base_destination is None:  # again?
            self.print_error(
                f"base_destination is None in class ({type(self)}) with key: {self.get_key()}")
            return False
        filename_extension: str = additional_data[self.key_filename_extension]
        if filename_extension is None:
            self.print_error(
                f"filename_extension is None in class ({type(self)}) with key: {self.get_key()}")
            return False
        is_write = True
        print(
            f"\n DEBUG: {type(self)} with key ({self.get_key()}) has additional_data equal to:")
        print(additional_data)
        for wmk in {KEY_OPEN_FILE_MODE, "mode", self.write_mode_key}:
            if wmk in additional_data:
                wm = additional_data[wmk]
                print(
                    f"\n DEBUG: {type(self)} with key ({self.get_key()}) has wm equal to:")
                print(wm)
                is_write = (wm == True) or \
                    (isinstance(wm, str) and
                        (wm.strip().lower() in MODE_VALUES_WRITE)) \
                    or (wm in MODE_VALUES_WRITE)
                break
        self.print_msg(
            f"creating base folder for output (of {type(self)} with key: {self.get_key()}) ---> {base_destination}")
        fu.check_and_make_folder(base_destination)
        full_path_file = self.compose_full_path_destination(
            base_destination, filename_extension)
        self.print_msg(
            f"full_path_file in output (of {type(self)} with key: {self.get_key()}) and is_write:{is_write} -> {full_path_file}")
        with open(full_path_file, 'w' if is_write else 'a') as f:
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
                    try:
                        f.write(json.dumps(what))
                        f.flush()
                        return True
                    except Exception as e:
                        import traceback
                        traceback.print_exception(e)
            return True
        return False

    def to_file(self, lines, folder_path, filename, extension, mode='w'):
        if folder_path is None:
            folder_path = fu.get_base_folder()
        else:
            fu.check_and_make_folder(folder_path)
        full_path = fu.concat_folder_filename(
            folder_path, f"{filename}.{extension}")

        self.print_msg(
            f"\nDEBUG: calling 'to_file' in {type(self)} with key ({self.get_key()})")
        return self.to_output(lines, full_path, {"mode": mode})
