from utilities.log_wrapper import LoggerWrapper

logger: LoggerWrapper = LoggerWrapper(filename="logs/latest.log")
logger.info("testing log wrapper")
logger.warning("There is a waring")

class Main:
    def __init__(self, log_wrapper: LoggerWrapper):
        self.logger = log_wrapper

    def send_message(self):
        self.logger.info("This Message")


main = Main(logger)
main.send_message()