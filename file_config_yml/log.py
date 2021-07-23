import logging
import logging.config
import os

import yaml


def get_logger(name, log_level):
    dir_name = os.path.dirname(os.path.abspath(__file__))
    with open(f'{dir_name}/config/logging.yml') as f:
        config = yaml.safe_load(f)

    logging.config.dictConfig(config)
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, log_level.upper()))
    return logger
