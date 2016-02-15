import logging.config

def initLogger():
    logging.config.fileConfig('./Config/log.conf')
