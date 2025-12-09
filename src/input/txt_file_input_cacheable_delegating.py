
import src.pipeline.pipeline_item as pi

import src.input.txt_file_input_cacheable as txt_f_i_caching

import src.utilities.utils as u


class TextFileInputCacheableDelegating(txt_f_i_caching.TextFileInputCacheable):
    def __init__(self, pipeline_item_data: pi.PIData,
                 printer_debug: u.PrinterDebug = None,
                 txt_input_cacheable_delegator: txt_f_i_caching.TextFileInputCacheable = None,
                 filepath=None,
                 should_strip_line=False
                 ):
        super().__init__(
            pipeline_item_data,
            printer_debug=printer_debug,
            filepath=filepath,
            should_strip_line=should_strip_line
        )
        self.txt_input_cacheable_delegator = txt_input_cacheable_delegator

    def get_cache_content_lines_by_path(self):
        self.print_msg(f"{type(self)} is delegating the cache instance")
        return super().get_cache_content_lines_by_path() \
            if self.txt_input_cacheable_delegator is None \
            else self.txt_input_cacheable_delegator.get_cache_content_lines_by_path()

    def clear_cache(self):
        if self.txt_input_cacheable_delegator is None:
            super().clear_cache()
        else:
            self.txt_input_cacheable_delegator.clear_cache()
