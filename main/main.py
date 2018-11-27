import tkinter as tk
#from buttons import btn_actions

class my_first_gui:
    def __init__(self):
        #self.btn_actions = btn_actions()
        self.root = tk.Tk()
        self.root.title("This is my GUI")

        button = tk.Button(self.root, text="Quit", fg="BLUE", command=self.btn_quit_click)
        button.pack()

        self.root.mainloop()

    #def btn_quit_click_window(self):
    #    print("Hello World")
    #    self.root.destroy()

    def btn_quit_click(self):
        self.root.destroy()


gui = my_first_gui()





