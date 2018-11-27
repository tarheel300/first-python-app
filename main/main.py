import tkinter as tk
#from buttons import btn_actions

class my_first_gui:
    def __init__(self):
        #self.btn_actions = btn_actions()
        self.root = tk.Tk()
        self.root.title("This is my GUI")

        self.frame = tk.Frame(master=self.root)
        #self.frame.pack_propagate(1)
        self.frame.place(x = 0, y = 0, relwidth = 100, relheight = 100)
        #self.frame.pack(fill=tk.BOTH, expand=True)

        button = tk.Button(self.frame, text="Quit", fg="BLUE", command=self.btn_quit_click)
        button.pack()

        self.root.mainloop()

    #def btn_quit_click_window(self):
    #    print("Hello World")
    #    self.root.destroy()

    def btn_quit_click(self):
        self.root.destroy()


gui = my_first_gui()





