import log


logger = log.get_logger(
    name=__name__,
    log_level='DEBUG',
    log_file='hoge.log'
)


def main():
    logger.debug('This is debug log')
    logger.info('Started')
    try:
        [][0]
    except Exception:
        logger.exception('エラーだよ')

    logger.info('Finished')


if __name__ == '__main__':
    main()
