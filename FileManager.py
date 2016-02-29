import os
from logging import *
import Utils


# option to exclude things
def getAllFiles(path):
    f = []
    info("Retrives files")
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            absPath = os.path.abspath(dirpath + filename)
            info("File: {0}".format(absPath))
            f.append(absPath)
    return f

if __name__ == "__main__":
    info("Start")
    Utils.initLogger()
    print getAllFiles("./")
    info("Stop")
