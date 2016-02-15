import Tkinter
import Utils
import logging as log

if __name__ == "__main__":
    Utils.initLogger()
    log.info("Program start")
    top = Tkinter.Tk()
    top.mainloop()
    log.info("Program stop")
