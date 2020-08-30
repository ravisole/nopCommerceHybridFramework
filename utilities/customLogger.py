import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt="HH:mm:ss.SSS")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
