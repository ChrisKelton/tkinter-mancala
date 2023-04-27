from tkinter import *

class RadioButtons0:
    def __init__(self):
        self.root = Tk()
        self.root.title("Gorilla Poop")
        self.root.iconbitmap('./Martin-Berube-Square-Animal-Gorilla.ico')
        self.label = None

    def run(self):
        self.radio_buttons()
        self.root.mainloop()

    def radio_buttons(self):
        # tkinter int variable
        r = IntVar()
        # initialize r as value=2
        r.set("2")

        # we can pass a string as the value here, if we did that we would have to update
        # r -> r = StrVar()
        Radiobutton(self.root, text="Option 1", variable=r, value=1, command=lambda: self.clicked(r.get())).pack()
        Radiobutton(self.root, text="Option 2", variable=r, value=2, command=lambda: self.clicked(r.get())).pack()

        self.label = Label(self.root, text=r.get()).pack()

        # make a button that, if clicked, will continuously output the value of the radio button
        button = Button(self.root, text="Click Me!", command=lambda: self.clicked(r.get())).pack()

    def clicked(self, value):
        self.label = Label(self.root, text=value).pack()


class RadioButtons1:
    def __init__(self):
        self.root = Tk()
        self.root.title("Gorilla Poop")
        self.root.iconbitmap('./Martin-Berube-Square-Animal-Gorilla.ico')
        self.label = None
        self.TOPPINGS = [
            ("Pepperoni", "Pepperoni"),
            ("Cheese", "Cheese"),
            ("Mushroom", "Mushroom"),
            ("Onion", "Onion"),
        ]

    def run(self):
        self.radio_buttons()
        self.root.mainloop()

    def radio_buttons(self):
        pizza = StringVar()
        pizza.set("Pepperoni")

        for text, topping in self.TOPPINGS:
            Radiobutton(self.root, text=text, variable=pizza, value=topping).pack(anchor=W)

        # make a button that, if clicked, will continuously output the value of the radio button
        button = Button(self.root, text="Click Me!", command=lambda: self.clicked(pizza.get())).pack()

    def clicked(self, value):
        self.label = Label(self.root, text=value).pack()

def main_cli():
    RadioButtons1().run()

if __name__ == '__main__':
    main_cli()