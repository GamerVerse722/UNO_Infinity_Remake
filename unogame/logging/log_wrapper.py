from colorlog import ColoredFormatter
import logging, inspect, os

class LoggerWrapper:
    def __init__(self, filename: str = "", console: bool | None = None):
        self.logger = None
        if console is True:
            formatter = ColoredFormatter(
                "%(log_color)s[%(asctime)s] [%(levelname)s] %(name)s: %(message)s%(reset)s",
                datefmt="%H:%M:%S",
                log_colors={
                    'DEBUG': 'cyan',
                    'INFO': 'green',
                    'WARNING': 'red',
                    'ERROR': 'yellow',
                    'CRITICAL': 'red',
                }
            )
            handler = logging.StreamHandler()
            handler.setFormatter(formatter)
            logging.basicConfig(
                                level=logging.DEBUG,
                                handlers=[handler])
            self.logger = logging.getLogger(__name__)

        elif console is False:
            logging.basicConfig(filename=filename,
                                    filemode="w",
                                    level=logging.DEBUG,
                                    format="[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
                                    datefmt="%H:%M:%S")
            self.logger = logging.getLogger(__name__)

    @staticmethod
    def call_location() -> str:
        location_data: list = inspect.stack()
        for x in location_data:
            line_number: str = x.lineno
            file_name: str = os.path.basename(x.filename)[:-3]
            source_class: str = x.frame.f_locals.get('self').__class__.__name__
            source_name: str = x.function
            if os.path.basename(x.filename)[:-3] != 'log_wrapper':
                return f"[line {line_number}] [{file_name}.{source_class}.{source_name}]"

        return "Not Found"

    def info(self, message: str) -> None:
        if self.logger is None:
            return
        self.logger = logging.getLogger(self.call_location())
        self.logger.info(message)

    def debug(self, message: str) -> None:
        if self.logger is None:
            return
        self.logger = logging.getLogger(self.call_location())
        self.logger.debug(message)

    def warning(self, message: str) -> None:
        if self.logger is None:
            return
        self.logger = logging.getLogger(self.call_location())
        self.logger.warning(message)

    def error(self, message: str) -> None:
        if self.logger is None:
            return
        self.logger = logging.getLogger(self.call_location())
        self.logger.error(message)

    def critical(self, message: str) -> None:
        if self.logger is None:
            return
        self.logger = logging.getLogger(self.call_location())
        self.logger.critical(message)

    def fatal(self, message: str) -> None:
        if self.logger is None:
            return
        self.logger = logging.getLogger(self.call_location())
        self.logger.fatal(message)