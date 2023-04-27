from tkinter import *

def label_0(root: Tk):
    # # label 'widget' have to put it into our root 'widget'
    myLabel = Label(root, text="Fibaboney")

    # # pack shoves the widget in at the first available spot on the screen
    # # keeps myLabel at the same spot no matter how the window is sized
    myLabel.pack()

def label_1(root: Tk):
    myLabel0 = Label(root, text="Fibaboney")
    myLabel1 = Label(root, text="Namadoodoo")
    # pick exact spot in window for desired positions of myLabel(s)
    # does not change with window resizing
    myLabel0.grid(row=0, column=0)
    # this grid system is relative, so even with column=5, myLabel1 will appear
    # as if it's only at column=1
    myLabel1.grid(row=1, column=5)

def label_2(root: Tk):
    myLabel0 = Label(root, text="Hello World")
    myLabel1 = Label(root, text="My Name is Gabagool")
    myLabel2 = Label(root, text="                   ")

    myLabel0.grid(row=0, column=0)
    myLabel1.grid(row=1, column=5)
    myLabel2.grid(row=1, column=1)

def label_3(root: Tk):
    myLabel0 = Label(root, text="Hello World").grid(row=0, column=0)
    myLabel1 = Label(root, text="My Name is Gabagool").grid(row=1, column=3)

def button_0(root: Tk):
    myButton = Button(root, text="Click Me!")
    myButton.pack()

def button_1(root: Tk):
    myButton = Button(root, text="Click Me!", state=DISABLED)
    myButton.pack()

def button_2(root: Tk):
    myButton = Button(root, text="Click Me!", padx=50)
    myButton.pack()

def button_3(root: Tk):
    myButton = Button(root, text="Click Me!", padx=50, pady=50)
    myButton.pack()

# make a button that does something!
class Button_4:
    def __init__(self, root: Tk):
        self.root = root

    def run(self):
        self.button()

    def myClick(self):
        myLabel = Label(self.root, text="Look I clicked a Button!")
        myLabel.pack()

    def button(self):
        # not self.myClick(), must be self.myClick
        # fg = foreground color (text color)
        # bg = background color
        myButton = Button(self.root, text="Click Me!", command=self.myClick, fg='blue', bg='white')
        myButton.pack()

class Input_Box(Button_4):
    def __init__(self, root: Tk):
        self.root = root
        self.e = Entry(root, width=50, borderwidth=5, fg='black', bg="white")
        self.e.pack()
        # 0th box, that's why it is 0
        # "Enter Your Name: " will show up in the output from clicking the button though
        self.e.insert(0, "Enter Your Name: ")

    def myClick(self):
        hello = "Hello " + self.e.get()
        # can input functions to text
        myLabel = Label(self.root, text=hello)
        myLabel.pack()

def main_cli():
    # main root 'widget' defined before everything else
    root = Tk()

    Input_Box(root).button()

    # keep looping program to keep window open and waiting for events
    root.mainloop()


if __name__ == '__main__':
    main_cli()