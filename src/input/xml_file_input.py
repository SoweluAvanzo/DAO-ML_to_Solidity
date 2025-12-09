
import src.pipeline.pipeline_item as pi

import src.input.txt_file_input_cacheable_delegating as txt_f_i_caching_d

import src.utilities.utils as u

DEFAULT_VERSION_XML_FILE_INPUT = "1.0"


class TextFileInputXML(txt_f_i_caching_d.TextFileInputCacheableDelegating):
    def __init__(self, pipeline_item_data: pi.PIData,
                 printer_debug: u.PrinterDebug = None,
                 filepath=None,
                 should_strip_line=False,
                 txt_input_cacheable_delegator: txt_f_i_caching_d.TextFileInputCacheableDelegating = None,
                 xml_version=DEFAULT_VERSION_XML_FILE_INPUT,
                 ):
        super().__init__(
            pipeline_item_data,
            printer_debug=printer_debug,
            filepath=filepath,
            should_strip_line=should_strip_line,
            txt_input_cacheable_delegator=txt_input_cacheable_delegator
        )
        self.xml_version = DEFAULT_VERSION_XML_FILE_INPUT if xml_version is None else xml_version
        # TODO: altro?
        # 2025-12-09 nothing else
