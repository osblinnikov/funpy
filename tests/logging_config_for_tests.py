import logging


def logging_config():
    logging.basicConfig(
        format='%(asctime)s %(name)s.%(funcName)s(): %(message)s',
        datefmt='%I:%M:%S %p',  # datefmt='%Y-%m-%d %I:%M:%S %p',
        level=logging.INFO
    )
    logging.info('Logger initialized')