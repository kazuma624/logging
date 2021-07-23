import logging


def get_logger(name, log_level='INFO'):
    level = getattr(logging, log_level.upper())
    logger = logging.getLogger(name) # 名前をつけてファイルごとのハンドラが毎回新しく生成されないようにする
    logger.setLevel(level)
    ch = logging.StreamHandler()
    ch.setLevel(level)
    formatter = logging.Formatter(
        fmt='%(asctime)s.%(msecs)-3d [%(levelname)s] %(filename)s %(funcName)s: %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S'
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
