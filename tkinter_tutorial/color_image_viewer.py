from tkinter import *
from PIL import ImageTk, Image

def icons_and_images_0(root: Tk):
    # change title on top of window
    root.title("Monkey Man")
    # change icon in top left of window
    root.iconbitmap('./Martin-Berube-Square-Animal-Gorilla.ico')
    # Tkinter only supports *.gif & *.pnm? So we must use PIL to support *.jpeg, *.png, etc...
    img = ImageTk.PhotoImage(Image.open("./Gorilla-icon.png"))
    label = Label(image=img)
    label.pack()

    button_quit = Button(root, text="Exit Program", command=root.quit)
    button_quit.pack()

    root.mainloop()

class ColorImageViewer:
    def __init__(self):
        self.root = Tk()
        self.root.title("Color Image Viewer")
        self.root.iconbitmap('./Martin-Berube-Square-Animal-Gorilla.ico')
        self.img_list = None
        self.num_of_imgs = 0
        self.img_label = None
        self.button_forward = None
        self.button_back = None
        self.img_cnt = 0
        self.status = 0

    def run(self):
        self.get_imgs()
        self.make_buttons()
        self.status_bar()
        self.root.mainloop()

    def get_imgs(self):
        img0 = ImageTk.PhotoImage(Image.open("./Gorilla-icon.png").resize((256, 256)))
        img1 = ImageTk.PhotoImage(Image.open("C:/Users/Chris/Documents/Dumbo/0_ole_tiresias.jpg").resize((256, 256)))
        img2 = ImageTk.PhotoImage(Image.open("C:/Users/Chris/Documents/Dumbo/badges.jpg").resize((256, 256)))
        img3 = ImageTk.PhotoImage(Image.open("C:/Users/Chris/Documents/Dumbo/Canyon.jpg").resize((256, 256)))
        img4 = ImageTk.PhotoImage(Image.open("C:/Users/Chris/Documents/Dumbo/Canyon-1 (Cartoon).JPG").resize((256, 256)))
        img5 = ImageTk.PhotoImage(Image.open("C:/Users/Chris/Documents/Dumbo/the_boy_weird.PNG").resize((256, 256)))
        self.img_list = [img0, img1, img2, img3, img4, img5]
        self.num_of_imgs = len(self.img_list)
        self.img_label = Label(image=self.img_list[0])
        self.img_label.grid(row=0, column=0, columnspan=3)

    def make_buttons(self):
        self.button_back = Button(self.root, text="<<", command=self.back, state=DISABLED)
        button_quit = Button(self.root, text="Exit Program", command=self.root.quit)
        self.button_forward = Button(self.root, text=">>", command=self.forward)
        self.button_back.grid(row=1, column=0)
        button_quit.grid(row=1, column=1, pady=10)
        self.button_forward.grid(row=1, column=2)

    def status_bar(self):
        # E = East, so will display in the bottom right of the viewer
        self.status = Label(self.root, text="Image " + str(self.img_cnt + 1) + " of " + str(self.num_of_imgs), bd=1, relief=SUNKEN, anchor=E)
        # The grid system works like cardinal directions, so W+E stretches the button all the way from the left to the right
        self.status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    def back(self):
        if self.img_cnt != 0:
            self.button_forward = Button(self.root, text=">>", command=self.forward)
            self.img_cnt -= 1
            self.img_label.grid_forget()
            self.img_label = Label(image=self.img_list[self.img_cnt])
            self.img_label.grid(row=0, column=0, columnspan=3)
            if self.img_cnt == 0:
                self.button_back = Button(self.root, text="<<", state=DISABLED)
        self.status_bar()
        self.button_back.grid(row=1, column=0)
        self.button_forward.grid(row=1, column=2)

    def forward(self):
        if self.img_cnt != len(self.img_list) - 1:
            self.button_back = Button(self.root, text="<<", command=self.back)
            self.img_cnt += 1
            self.img_label.grid_forget()
            self.img_label = Label(image=self.img_list[self.img_cnt])
            self.img_label.grid(row=0, column=0, columnspan=3)
            if self.img_cnt == len(self.img_list) - 1:
                self.button_forward = Button(self.root, text=">>", state=DISABLED)
        self.status_bar()
        self.button_back.grid(row=1, column=0)
        self.button_forward.grid(row=1, column=2)

def main_cli():
    ColorImageViewer().run()

if __name__ == '__main__':
    main_cli()