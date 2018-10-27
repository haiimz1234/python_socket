import logging
import logging.config
import threading
formatter = logging.Formatter('%(asctime)s %(threadName)-9s) %(levelname)s %(message)s')


class Setup_MyGlobal_logger:
    def __init__(self,name, log_file, level=logging.ERROR) :
        self.lock = threading.Lock()

  #  def Setup_MyGlobal_logger(name, log_file, level=logging.ERROR):
        """Function setup as many loggers as you want"""
        global formatter
        handler = logging.FileHandler(log_file)
        handler.setFormatter(formatter)

        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.addHandler(handler)
#        return logger
    def error(self,message):
        self.lock.acquire()
        try:
            self.logger.error(message)
        finally:
            self.lock.release()

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
