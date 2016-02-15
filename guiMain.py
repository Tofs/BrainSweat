from Tkinter import *
import Utils
import logging as log
import FileManager




def getFiles():
    global paths
    paths.set(FileManager.getAllFiles("./"))

def buildGUI():
    global paths
    log.debug("build GUI ...")
    root = Tk()
    root.title("BreainSweat")


    paths = StringVar()

    mainFrame = Frame(root)
    mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    mainFrame.columnconfigure(0, weight=1)
    mainFrame.rowconfigure(0, weight=1)


    Label(mainFrame, textvariable=paths).grid(column=0,row=0, sticky=(W, E))

    Button(mainFrame, text="Load", command=getFiles).grid(column=0,row=1, sticky=(W, E))

    log.info("GUI Done!")
    return root


if __name__ == "__main__":
    Utils.initLogger()
    log.info("Program start")
    tk = buildGUI()
    tk.mainloop()
    log.info("Program stop")
