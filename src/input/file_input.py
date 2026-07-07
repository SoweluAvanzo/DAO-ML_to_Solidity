import src.input.input_base as ib
import src.pipeline.pipeline_item as pi
from contextlib import contextmanager

import src.utilities.utils as u


class FileInput(ib.InputBase):
    """
    Abstract class, able to be used in a "with" statement to open a file.
    """

    def __init__(self, pipeline_item_data: pi.PIData,
                 printer_debug: u.PrinterDebug = None,
                 filepath=None
                 ):
        super().__init__(pipeline_item_data,
                         printer_debug=printer_debug
                         )
        self.filepath = filepath

    def _get_filepath_from_input(self):
        return self.filepath \
            if self.inputs_from_run is None \
            or len(self.get_dependencies()) == 0 \
            else self.get_ith_input(self.inputs_from_run, 0)

    @contextmanager
    def open_file(self):
        try:
            file_path = self._get_filepath_from_input()
            f = open(file_path, 'r')
            try:
                yield f
            finally:
                f.close()
        except Exception as err:
            print(err)
            yield None
