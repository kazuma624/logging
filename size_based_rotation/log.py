import logging
import logging.handlers
import os


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
    fh = logging.handlers.RotatingFileHandler(
        filename=f'{dir_name}/log/{filename}',
        backupCount=3,
        maxBytes=32,
    )
    fh.setLevel(level)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger
