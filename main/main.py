from tkinter import Tk, Label, Button

class my_first_gui:
    def __init__(self, master):
        self.master = master
        master.title("This is my GUI")

root = Tk()
my_gui = my_first_gui(root)
root.mainloop()






