from colorlog import ColoredFormatter
import logging, inspect, os

class LoggerWrapper:
    def __init__(self, filename: str, console: bool = False):
        if console:
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
        else:
            logging.basicConfig(filename=filename,
                                    filemode="w",
                                    level=logging.DEBUG,
                                    format="[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
                                    datefmt="%H:%M:%S")
        self.logger = logging.getLogger(__name__)

    @staticmethod
    def call_location() -> str:
        location_data: list = inspect.stack()
        length: int = len(location_data)
        for _ in range(length):
            caller_frame = location_data[length-2]
            caller_name: str = caller_frame.function
            caller_class: str = caller_frame.frame.f_locals.get('self').__class__.__name__
            caller_filename: str = os.path.basename(caller_frame.filename)[:-3]
            caller_line_number: str = caller_frame.lineno
            if caller_class == 'MyClass':
                continue

            if caller_class == 'NoneType':
                return f"[line {caller_line_number}] [{caller_filename}.{caller_name}]"

            elif caller_class != 'NoneType':
                return f"[line {caller_line_number}] [{caller_filename}.{caller_class}.{caller_name}]"

        return "Not Found"


    def info(self, message: str):
        self.logger = logging.getLogger(self.call_location())
        self.logger.info(message)

    def debug(self, message: str):
        self.logger = logging.getLogger(self.call_location())
        self.logger.debug(message)

    def warning(self, message: str):
        self.logger = logging.getLogger(self.call_location())
        self.logger.warning(message)

    def error(self, message: str):
        self.logger = logging.getLogger(self.call_location())
        self.logger.error(message)

    def critical(self, message: str):
        self.logger = logging.getLogger(self.call_location())
        self.logger.critical(message)

    def fatal(self, message: str):
        self.logger = logging.getLogger(self.call_location())
        self.logger.fatal(message)