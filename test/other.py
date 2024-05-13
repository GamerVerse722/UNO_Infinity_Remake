from unogame.logger.log_wrapper import LoggerWrapper

logger = LoggerWrapper(filename="test.log", mode="d")
logger.info("hi")


