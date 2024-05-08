import logging

class LoggerWrapper:
    def __init__(self, filename: str):
        logging.basicConfig(filename=filename,
                            filemode="w",
                            level=logging.DEBUG,
                            format="[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s",
                            datefmt="%H:%M:%S")
        self.logger = logging.getLogger(__name__)

    def info(self, message: str):
        self.logger.info(message)

    def debug(self, message: str):
        self.logger.debug(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

    def critical(self, message: str):
        self.logger.critical(message)

    def fatal(self, message: str):
        self.logger.fatal(message)