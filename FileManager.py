import os
import logging.config
from logging import *


# option to exclude things
def getAllFiles(path):
    f = []

    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            f.append(dirpath + filename)
    return f

if __name__ == "__main__":
    logging.config.fileConfig('./Config/log.conf')
    info("Start")
    print getAllFiles("./")
    info("Stop")
