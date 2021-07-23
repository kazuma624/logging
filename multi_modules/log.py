import logging


def get_logger(filename, log_level='INFO'):
    logger = logging.getLogger(filename)
    logging.basicConfig(level=getattr(logging, log_level.upper()))
    return logger
