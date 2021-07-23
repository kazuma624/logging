import log
import time


logger = log.get_logger(
    name=__name__,
    log_level='DEBUG',
    # filename='example.log'
)


def main():
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
