import logging

def getLogger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)

        fh = logging.FileHandler('app.log')
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger
