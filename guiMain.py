from Tkinter import *
import Utils
import logging as log

def buildGUI():
    log.debug("build GUI ...")
    root = Tk()

    Button(root, text="BrainSweat").grid()

    log.info("GUI Done!")
    return root


if __name__ == "__main__":
    Utils.initLogger()
    log.info("Program start")
    tk = buildGUI()
    tk.mainloop()
    log.info("Program stop")
