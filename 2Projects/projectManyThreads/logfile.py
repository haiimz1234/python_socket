import logging
import logging.config
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')


def Setup_MyGlobal_logger(name, log_file, level=logging.ERROR):
    """Function setup as many loggers as you want"""
    global formatter
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

def Local_logger(name, log_file, level,message):
    """Function write message to specil file"""
    global formatter
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    logger.addHandler(handler)
    if (level == logging.INFO):
        logger.info(message)
    else:
        logger.error(message)
    handler.close() #
