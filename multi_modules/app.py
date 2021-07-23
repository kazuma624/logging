import log
import lib


logger = log.get_logger(filename=__name__, log_level='DEBUG')


def main():
    logger.debug('This is debug log')
    logger.info('Started')
    lib.do_something()
    logger.info('Finished')


if __name__ == '__main__':
    main()
