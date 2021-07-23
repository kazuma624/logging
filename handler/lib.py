import log


logger = log.get_logger(name=__name__, log_level='DEBUG')


def do_something():
    logger.info('Doing something')
