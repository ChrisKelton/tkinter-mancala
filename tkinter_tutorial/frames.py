from tkinter import *

def frames_0():
    root = Tk()
    root.title("Gorilla Poop")
    root.iconbitmap('./Martin-Berube-Square-Animal-Gorilla.ico')

    # this padding goes inside of the frame (location of frame text)
    frame = LabelFrame(root, text="This is my frame...", padx=50, pady=50)
    # padding means from the edges of the viewer
    frame.pack(padx=100, pady=100)

    # can do grid inside of frame, rather than having to stick to either pack or grid
    b0 = Button(frame, text="Don't Click Here")
    b0.grid(row=0, column=0)
    b1 = Button(frame, text="Do Click Here")
    b1.grid(row=1, column=1)

    root.mainloop()

def main_cli():
    frames_0()

if __name__ == '__main__':
    main_cli()