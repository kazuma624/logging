import logging
import logging.config
import os


def get_logger(name, log_level):
    dir_name = os.path.dirname(os.path.abspath(__file__))
    logging.config.fileConfig(f'{dir_name}/config/logging.conf')
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, log_level.upper()))
    return logger
