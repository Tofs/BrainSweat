from Tkinter import *
import Utils
import logging as log
import FileManager



listbox = None
def getFiles():
    global listbox
    for item in FileManager.getAllFiles("./"):
        log.debug("Add item to listbox: {0}".format(item))
        listbox.insert(END, item)


def buildGUI():
    global listbox
    log.debug("build GUI ...")
    root = Tk()
    root.title("BreainSweat")


    paths = StringVar()

    mainFrame = Frame(root)
    mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
    mainFrame.columnconfigure(0, weight=1)
    mainFrame.rowconfigure(0, weight=1)

    listbox = Listbox(mainFrame)
    listbox.grid(column=0,row=0, sticky=(W, E))
    Button(mainFrame, text="Load", command=getFiles).grid(column=0,row=1, sticky=(W, E))

    log.info("GUI Done!")
    return root


if __name__ == "__main__":
    Utils.initLogger()
    log.info("Program start")
    tk = buildGUI()
    tk.mainloop()
    log.info("Program stop")
