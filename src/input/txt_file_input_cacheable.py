
import src.pipeline.pipeline_item as pi
import src.input.txt_file_input as tfi

import src.utilities.utils as u


class TextFileInputCacheable(tfi.TextFileInput):
    def __init__(self, pipeline_item_data: pi.PIData,
                 printer_debug: u.PrinterDebug = None,
                 filepath=None,
                 should_strip_line=False,
                 is_caching_file_content=True
                 ):
        super().__init__(
            pipeline_item_data,
            printer_debug=printer_debug,
            filepath=filepath,
            should_strip_line=should_strip_line
        )
        self.is_caching_file_content = is_caching_file_content
        self.file_content_lines_cached_by_path: dict[str, str] = {}

    def get_cache_content_lines_by_path(self):
        return self.file_content_lines_cached_by_path

    def set_is_caching_file_content(self, is_caching: bool):
        self.is_caching_file_content = is_caching

    def clear_cache(self):
        self.file_content_lines_cached_by_path = {}

    def get_filepaths_cached(self) -> list[str]:
        return list(self.get_cache_content_lines_by_path().keys())

    def strip_line(self, line: str) -> str:
        return line.strip() if self.should_strip_line else line.replace("\n", "").replace("\r", "")

    def get_input_as_iterable(self):
        filepath = self._get_filepath_from_input()
        if (not self.is_caching_file_content) or (filepath in self.get_cache_content_lines_by_path()):
            self.print_msg(
                f"get_input_as_iterable in class {type(self)} is getting the content from the super (with filename: {filepath})")
            content_as_iter = super().get_input_as_iterable()
            if self.is_caching_file_content:
                lines = []
                self.print_msg("cache obtained, now returning it")
                for line in content_as_iter:
                    lines.append(line)
                    yield self.strip_line(line)
                self.get_cache_content_lines_by_path()[filepath] = lines
            else:  # else, simply return them
                for line in content_as_iter:
                    yield self.strip_line(line)
        else:
            self.print_msg(
                f"get_input_as_iterable in class {type(self)} is getting the content from the cache!")
            content_as_iter = self.get_cache_content_lines_by_path()[
                filepath]
            for line in content_as_iter:
                yield self.strip_line(line)
