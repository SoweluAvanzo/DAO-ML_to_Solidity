import sys
import logging

import src.utilities.utils as u

DEFAULT_NAME = __name__
DEFAULT_FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
def DEFAULT_HANDLER_SYSOUT_PRODUCER(): return logging.StreamHandler(sys.stdout)

#


class DispatchingFormatter:
    """
    Dispatch formatter for logger and it's sub logger.
    Source: https://stackoverflow.com/a/34626685/3961710
    """

    def __init__(self, formatters: dict, default_formatter: logging.Formatter):
        self._formatters = formatters
        self._default_formatter = default_formatter

    def format(self, record):
        # Search from record's logger up to it's parents:
        logger = logging.getLogger(record.name)
        while logger:
            # Check if suitable formatter for current logger exists:
            if logger.name in self._formatters:
                formatter = self._formatters[logger.name]
                break
            else:
                logger = logger.parent
        else:
            # If no formatter found, just use default:
            formatter = self._default_formatter
        return formatter.format(record)

#


class LoggerDebug(u.PrinterDebug):
    def __init__(self,
                 class_name: str = DEFAULT_NAME,
                 format_msg: str = DEFAULT_FORMAT,
                 log_level=logging.INFO,
                 handler: logging.Handler = None,
                 hierarchical_formats: dict[str, str] = None
                 ):
        super().__init__()
        logger = logging.getLogger(class_name)
        logger.setLevel(log_level)
        if handler is None:
            handler = DEFAULT_HANDLER_SYSOUT_PRODUCER()
        if hierarchical_formats is None:
            handler.setFormatter(format_msg)
        else:
            handler.setFormatter(
                DispatchingFormatter(
                    {
                        hierarchy_name: logging.Formatter(
                            format_hierarchy_specifc)
                        for hierarchy_name, format_hierarchy_specifc in hierarchical_formats.items()
                    },
                    logging.Formatter(format_msg)
                )
            )
        logger.addHandler(handler)
        # logging.getLogger().addHandler(handler)
        self.logger = logger
