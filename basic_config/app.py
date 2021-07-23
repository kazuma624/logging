import logging
import os


def get_logger(name, log_level='INFO', log_file='example.log'):
    dir_name = os.path.dirname(os.path.abspath(__file__))
    logger = logging.getLogger(name)
    logging.basicConfig(
        filename=f'{dir_name}/log/{log_file}',
        format='%(asctime)s.%(msecs)-3d [%(levelname)s] %(filename)s %(funcName)s: %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S',
        level=getattr(logging, log_level.upper()),
    )
    return logger


def main():
    logger = get_logger(
        name=__name__,
        log_level='DEBUG',
        log_file='hoge.log'
    )
    logger.debug('This is debug log')
    logger.info('Started')
    try:
        [][0]
    except Exception:
        logger.exception('エラーだよ')

    logger.info('Finished')


if __name__ == '__main__':
    main()
