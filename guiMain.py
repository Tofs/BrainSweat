from Tkinter import *
import Utils
import logging as log

def buildGUI():
    log.debug("build GUI ...")
    top = Tk()



    log.info("GUI Done!")
    return top


if __name__ == "__main__":
    Utils.initLogger()
    log.info("Program start")
    tk = buildGUI()
    tk.mainloop()
    log.info("Program stop")
