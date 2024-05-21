from unogame.logging.log_wrapper import LoggerWrapper

logger = LoggerWrapper(filename="test.log", console=True)
logger.info("hi")


