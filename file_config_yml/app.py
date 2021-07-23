import logging
import logging.config
import os
import time

import yaml


def get_logger(name, log_level):
    dir_name = os.path.dirname(os.path.abspath(__file__))
    with open(f'{dir_name}/config/logging.yml') as f:
        config = yaml.safe_load(f)

    logging.config.dictConfig(config)
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, log_level.upper()))
    return logger


def main():
    logger = get_logger(
        name=__name__,
        log_level='DEBUG',
        # filename='example.log' # TODO: 後からファイル名を指定したい
    )
    logger.debug('This is debug log')
    logger.info('Start')
    cnt = 0
    while True:
        time.sleep(1)
        logger.info(f'Counter: {cnt}')
        cnt += 1
        if cnt == 10:
            logger.warning(f'Counter: {cnt} stop')
            break


if __name__ == '__main__':
    main()
