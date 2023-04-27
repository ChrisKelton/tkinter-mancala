from tkinter import *
import re

class Calculator:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title("Simple Calculator")
        self.e = Entry(self.root, width=35, borderwidth=5)
        # columnspan=3 b/c there will be 3 buttons in each row
        # so it will span across three columns at row 0
        self.e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.equals_flag = False
        self.equals = None

    def run(self):
        self.num_buttons()
        self.sym_buttons()

    def num_buttons(self):
        button_0 = Button(self.root, text=str(0), padx=40, pady=20, command=lambda: self.button_click(0))
        button_1 = Button(self.root, text=str(1), padx=40, pady=20, command=lambda: self.button_click(1))
        button_2 = Button(self.root, text=str(2), padx=40, pady=20, command=lambda: self.button_click(2))
        button_3 = Button(self.root, text=str(3), padx=40, pady=20, command=lambda: self.button_click(3))
        button_4 = Button(self.root, text=str(4), padx=40, pady=20, command=lambda: self.button_click(4))
        button_5 = Button(self.root, text=str(5), padx=40, pady=20, command=lambda: self.button_click(5))
        button_6 = Button(self.root, text=str(6), padx=40, pady=20, command=lambda: self.button_click(6))
        button_7 = Button(self.root, text=str(7), padx=40, pady=20, command=lambda: self.button_click(7))
        button_8 = Button(self.root, text=str(8), padx=40, pady=20, command=lambda: self.button_click(8))
        button_9 = Button(self.root, text=str(9), padx=40, pady=20, command=lambda: self.button_click(9))

        button_9.grid(row=1, column=2)
        button_8.grid(row=1, column=1)
        button_7.grid(row=1, column=0)
        button_6.grid(row=2, column=2)
        button_5.grid(row=2, column=1)
        button_4.grid(row=2, column=0)
        button_3.grid(row=3, column=2)
        button_2.grid(row=3, column=1)
        button_1.grid(row=3, column=0)
        button_0.grid(row=4, column=0)

    # Not sure why, but the input to all the self.button_click(i) command is zero for all the buttons (i.e., the last
    # element of the list comprehension.
    # def num_buttons(self):
    #     # define buttons
    #     # in order to allow us to take in the number buttons we make our command a lambda function
    #     buttons = [
    #         Button(
    #             self.root,
    #             text=str(i),
    #             padx=40,
    #             pady=20,
    #             command=lambda: self.button_click(i)
    #         ) for i in np.arange(9, -1, -1)
    #     ]
    #     cnt = 0
    #     for button in buttons:
    #         if cnt < 3:
    #             button.grid(row=1, column=(2 - cnt))
    #         elif cnt > 2 and cnt < 6:
    #             button.grid(row=2, column=((5 - cnt) % 3))
    #         elif cnt > 5 and cnt < 9:
    #             button.grid(row=3, column=((8 - cnt) % 6))
    #         else:
    #             button.grid(row=4, column=0)
    #         cnt += 1

    def sym_buttons(self):
        button_add = Button(self.root, text="+", padx=40, pady=20, command=self.button_add)
        button_minus = Button(self.root, text="-", padx=40, pady=20, command=self.button_minus)
        button_mult = Button(self.root, text="*", padx=40, pady=20, command=self.button_mult)
        button_div = Button(self.root, text="/", padx=40, pady=20, command=self.button_div)
        button_equal = Button(self.root, text="=", padx=90, pady=20, command=self.button_equal)
        button_right_par = Button(self.root, text=")", padx=40, pady=20, command=self.button_right_par)
        button_left_par = Button(self.root, text="(", padx=40, pady=20, command=self.button_left_par)
        button_clear = Button(self.root, text="Clear", padx=40, pady=20, command=self.button_clear)
        button_point = Button(self.root, text=".", padx=40, pady=20, command=self.button_point)
        button_power = Button(self.root, text="^", padx=40, pady=20, command=self.button_power)

        # make clear and equal buttons span two columns, not just one
        # in order to make the calculator look nice (this was for before adding more functionality)
        # button_clear.grid(row=4, column=1, columnspan=2)
        button_equal.grid(row=4, column=1, columnspan=2)
        button_add.grid(row=5, column=0)
        button_minus.grid(row=5, column=1)
        button_mult.grid(row=5, column=2)
        button_div.grid(row=6, column=0)
        button_left_par.grid(row=6, column=1)
        button_right_par.grid(row=6, column=2)
        button_point.grid(row=7, column=0)
        button_power.grid(row=7, column=1)
        button_clear.grid(row=7, column=2)

    def check_equals_flag(self):
        if self.equals_flag:
            self.equals_flag = False
            current = self.e.get()
            found = re.search("=", self.equals).span()
            if self.equals[found[1]] != "=":
                current = current.strip(self.equals[0:found[0]])
            else:
                current = current.strip(self.equals[0:found[1]])
            self.equals = None
            self.e.delete(0, END)
            self.e.insert(0, str(current))

    def button_click(self, number: int):
        self.check_equals_flag()
        current = self.e.get()
        # this will delete anything that has already been entered
        # so after every entry to the calculator this will delete the latest entry
        self.e.delete(0, END)
        self.e.insert(0, str(current) + str(number))

    def button_point(self):
        self.check_equals_flag()
        current = self.e.get()
        if not re.search("[.]", current):
            self.e.delete(0, END)
            self.e.insert(0, f"{current}.")

    def button_add(self):
        self.check_equals_flag()
        try:
            current = self.e.get()
            self.e.delete(0, END)
            self.e.insert(0, str(current) + "+")
        except ValueError:
            self.e.delete(0, END)
            self.e.insert(0, "Err. Press Clear to Reset.")

    def button_minus(self):
        self.check_equals_flag()
        try:
            current = self.e.get()
            self.e.delete(0, END)
            self.e.insert(0, str(current) + "-")
        except ValueError:
            self.e.delete(0, END)
            self.e.insert(0, "Err. Press Clear to Reset.")

    def button_mult(self):
        self.check_equals_flag()
        try:
            current = self.e.get()
            self.e.delete(0, END)
            self.e.insert(0, str(current) + "*")
        except ValueError:
            self.e.delete(0, END)
            self.e.insert(0, "Err. Press Clear to Reset.")

    def button_div(self):
        self.check_equals_flag()
        try:
            current = self.e.get()
            self.e.delete(0, END)
            self.e.insert(0, str(current) + "/")
        except ValueError:
            self.e.delete(0, END)
            self.e.insert(0, "Err. Press Clear to Reset.")

    def button_right_par(self):
        self.check_equals_flag()
        try:
            current = self.e.get()
            self.e.delete(0, END)
            self.e.insert(0, str(current) + ")")
        except ValueError:
            self.e.delete(0, END)
            self.e.insert(0, "Err. Press Clear to Reset.")

    def button_left_par(self):
        self.check_equals_flag()
        try:
            current = self.e.get()
            self.e.delete(0, END)
            self.e.insert(0, str(current) + "(")
        except ValueError:
            self.e.delete(0, END)
            self.e.insert(0, "Err. Press Clear to Reset.")

    def button_power(self):
        self.check_equals_flag()
        try:
            current = self.e.get()
            self.e.delete(0, END)
            self.e.insert(0, str(current) + "^")
        except ValueError:
            self.e.delete(0, END)
            self.e.insert(0, "Err. Press Clear to Reset.")

    # have to create a PEMDAS sorted list that retains the original indices of the
    # order of the symbols in order to retain which numbers to apply the maths to
    def button_equal(self):
        self.equals_flag = True
        try:
            current = self.e.get()
            self.e.delete(0, END)
            result = ""
            num_1 = ""
            symbol = None
            symbol2 = None
            try:
                for character in current:
                    try:
                        res = int(character)
                        if symbol is None:
                            result += str(res)
                        # check for symbol for numbers > 9
                        elif symbol is not None and symbol2 is None:
                            num_1 += str(res)
                        if result != "" and num_1 != "" and (symbol2 is not None or character == current[-1]):
                            result = float(result)
                            num_1 = float(num_1)
                            if symbol == "+":
                                result += num_1
                            elif symbol == "-":
                                result -= num_1
                            elif symbol == "*":
                                result *= num_1
                            elif symbol == "/":
                                result /= num_1
                            elif symbol == "^":
                                result **= num_1
                            num_1 = str(res)
                            if symbol2 is not None:
                                symbol = symbol2
                                symbol2 = None
                            else:
                                symbol = None
                    except ValueError:
                        if character == ".":
                            if num_1 == "":
                                result += character
                            else:
                                num_1 += character
                        elif character == "-":
                            if result == "":
                                result += character
                            elif symbol is not None:
                                if num_1 == "":
                                    num_1 += character
                                else:
                                    symbol2 = character
                            else:
                                symbol = character
                        else:
                            if symbol is None:
                                symbol = character
                            else:
                                symbol2 = character
            except OverflowError:
                result = "Overflow Error. Press Clear to Reset."

            self.e.delete(0, END)
            self.e.insert(0, str(current) + "=" + str(result))
            self.equals = self.e.get()
        except ValueError:
            self.e.delete(0, END)
            self.e.insert(0, "Err. Press Clear to Reset.")

    def button_clear(self):
        self.e.delete(0, END)
        self.equals_flag = False
        self.equals = None

def main_cli():
    root = Tk()
    Calculator(root).run()
    root.mainloop()

if __name__ == '__main__':
    main_cli()