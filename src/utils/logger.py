import logging
message_formatter = logging.Formatter(
    '%(asctime)s  [ %(levelname)s ]  %(message)s \n')
table_formatter = logging.Formatter('%(message)s\n\n')


def setup_logger(name, log_file, type, level=logging.INFO):
    '''  Function to create logger.  '''

    handler = logging.FileHandler(log_file)

    if type == 'table':
        handler.setFormatter(table_formatter)
    else:
        handler.setFormatter(message_formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
