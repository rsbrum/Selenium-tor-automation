import logging

def setup_logger():
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
    s_handler = logging.StreamHandler()
    s_handler.setFormatter(formatter)
    f_handler = logging.FileHandler('./config/file.log')   
    f_handler.setFormatter(formatter)
    logger = logging.getLogger('root')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(f_handler)
    logger.addHandler(s_handler)
    return logger
