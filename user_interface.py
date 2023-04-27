from tkinter import *
from PIL import ImageTk, Image
from mancala_main import *

class MancalaGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Board Games With Holes")
        self.root.iconbitmap('./tkinter_tutorial/Martin-Berube-Square-Animal-Gorilla.ico')
        self.frame = None
        self.img_label = None

    def setup(self):
        self.aesthetics()
        self.root.mainloop()

    def aesthetics(self):
        try:
            self.root.title("Board Games With Holes")
            for grid_slave in self.root.grid_slaves():
                grid_slave.grid_forget()
        except AttributeError:
            print("Program Starting Up.")
        self.frame = LabelFrame(self.root, text="Choose Your Game", padx=50, pady=50)
        self.frame.pack(padx=50, pady=50)

        mancala_button = Button(self.frame, text="mancala", command=self.mancala_page)
        sungka_button = Button(self.frame, text="sungka", command=self.sungka_page)
        sungkala_button = Button(self.frame, text="sungkala", command=self.sungkala_page)

        mancala_button.grid(row=0, column=0)
        sungka_button.grid(row=0, column=1)
        sungkala_button.grid(row=0, column=2)

    def mancala_page(self):
        self.frame.pack_forget()
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.title("Mancala")

        for grid_slave in self.root.grid_slaves():
            grid_slave.grid_forget()

        button_back = Button(self.root, text="<<", command=self.aesthetics)

        img = ImageTk.PhotoImage(Image.open("./tkinter_tutorial/Gorilla-icon.png"))
        self.img_label = Label(image=img)

        self.img_label.grid(row=0, column=0, columnspan=3)
        button_back.grid(row=1, column=0, sticky=W)

    def sungka_page(self):
        self.frame.pack_forget()
        for widget in self.frame.winfo_children():
            widget.destroy()
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.title("Sungka")

        for grid_slave in self.root.grid_slaves():
            grid_slave.grid_forget()

        img = ImageTk.PhotoImage(Image.open("./tkinter_tutorial/Gorilla-icon.png"))
        img_label = Label(image=img)
        img_label.grid(row=0, column=0)

        button_back = Button(self.root, text="<<", command=self.aesthetics)
        button_back.grid(row=1, column=0, sticky=W)

    def sungkala_page(self):
        self.frame.pack_forget()
        for widget in self.frame.winfo_children():
            widget.destroy()
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.title("Sungkala")

        for grid_slave in self.root.grid_slaves():
            grid_slave.grid_forget()

        img = ImageTk.PhotoImage(Image.open("./tkinter_tutorial/Gorilla-icon.png"))
        img_label = Label(image=img)
        img_label.grid(row=0, column=0)

        button_back = Button(self.root, text="<<", command=self.aesthetics)
        button_back.grid(row=1, column=0, sticky=W)


def main_cli():
    MancalaGUI().setup()


if __name__ == '__main__':
    main_cli()
