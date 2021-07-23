import lib
import log


logger = log.get_logger(name=__name__, log_level='DEBUG')
print('logger', getattr(logger, 'level'))

def main():
    logger.debug('This is debug log')
    logger.info('Started')
    logger.warning('Some warining')
    lib.do_something()
    logger.info('Finished')


if __name__ == '__main__':
    main()
