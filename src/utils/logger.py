import logging

message_formatter = logging.Formatter("%(asctime)s  [ %(levelname)s ]  %(message)s \n")
table_formatter = logging.Formatter("%(message)s\n\n")

error_formatter = logging.Formatter(
    "%(asctime)s [ %(levelname)s ] [%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s \n"
)


console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger("").addHandler(console)


def setup_logger(name, log_file, type, level=logging.INFO):
    """  Function to create logger.  """

    handler = logging.FileHandler(log_file)

    if type == "table":
        handler.setFormatter(table_formatter)
        console.setFormatter(table_formatter)
    elif type == "error":
        handler.setFormatter(error_formatter)
        console.setFormatter(error_formatter)
    else:
        handler.setFormatter(message_formatter)
        console.setFormatter(message_formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
