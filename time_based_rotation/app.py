import logging
import logging.handlers
import os
import time


def get_logger(name, log_level='INFO', filename='example.log'):
    level = getattr(logging, log_level.upper())
    logger = logging.getLogger(name)
    logger.setLevel(level)
    formatter = logging.Formatter(
        fmt='%(asctime)s.%(msecs)-3d [%(levelname)s] %(filename)s %(funcName)s: %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S'
    )

    # コンソールに書き出すハンドラー
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    dir_name = os.path.dirname(os.path.abspath(__file__))
    # ファイルに書き出すハンドラー
    fh = logging.handlers.TimedRotatingFileHandler(
        filename=f'{dir_name}/log/{filename}',
        backupCount=3, # バックアップは 3 ファイルまで
        when='S', # ローテートする時間単位（ここでは「秒」）
        interval=5 # when に指定した単位 5 つおき（つまり 5 秒）にファイルを新しくする
    )
    fh.setLevel(level)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger


def main():
    logger = get_logger(
        name=__name__,
        log_level='DEBUG',
        filename='example.log'
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
