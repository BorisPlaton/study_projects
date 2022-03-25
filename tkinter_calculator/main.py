from tkinter import *


def equal():
    global user_input
    try:
        user_input = f"{eval(user_input)}"
    except Exception:
        output_line["text"] = "Error"
    else:
        output_line["text"] = user_input


def plus():
    global user_input
    user_input += "+"
    output_line["text"] += "+"
    output()


def minus():
    global user_input
    user_input += "-"
    output_line["text"] += "-"
    output()


def divide():
    global user_input
    user_input += "/"
    output_line["text"] += "/"
    output()


def delete():
    global user_input
    user_input = ""
    output_line["text"] = ""
    output()


def multiply():
    global user_input
    user_input += "*"
    output_line["text"] += "*"
    output()


def bracket_1():
    global user_input
    user_input += "("
    output_line["text"] += "("
    output()


def bracket_2():
    global user_input
    user_input += ")"
    output_line["text"] += ")"
    output()


def degree():
    global user_input
    user_input += "**"
    output_line["text"] += "^"
    output()


def one():
    global user_input
    user_input += "1"
    output_line["text"] += "1"
    output()


def two():
    global user_input
    user_input += "2"
    output_line["text"] += "2"


def three():
    global user_input
    user_input += "3"
    output_line["text"] += "3"
    output()


def four():
    global user_input
    user_input += "4"
    output_line["text"] += "4"
    output()


def five():
    global user_input
    user_input += "5"
    output_line["text"] += "5"
    output()


def six():
    global user_input
    user_input += "6"
    output_line["text"] += "6"
    output()


def seven():
    global user_input
    user_input += "7"
    output_line["text"] += "7"
    output()


def eight():
    global user_input
    user_input += "8"
    output_line["text"] += "8"
    output()


def nine():
    global user_input
    user_input += "9"
    output_line["text"] += "9"
    output()


def zero():
    global user_input
    user_input += "0"
    output_line["text"] += "0"
    output()


def erase():
    global user_input
    user_input = user_input[:len(user_input) - 1]
    output_line["text"] = user_input
    output()


def output():
    global user_input
    global output_text
    try:
        if isinstance(eval(user_input), float):
            output_text = f"{eval(user_input):.{4}f}"
        else:
            output_text = f"{eval(user_input)}"
    except Exception:
        output_line_2["text"] = ""
    else:
        output_line_2["text"] = output_text


def copy():
    global output_text
    main_win.clipboard_clear()
    main_win.clipboard_append(output_line_2['text'])
    main_win.update()


user_input = ""
output_text = ""

"""Window option"""

main_win = Tk()
main_win.title("Calculator")
main_win.iconbitmap("Images/calculator.ico")
main_win.geometry("415x350")
main_win.resizable(False, False)
main_win["bg"] = "#282828"

"""Buttons option"""

# 1
img_1 = PhotoImage(file="Images/1.png").subsample(4, 4)
btn_1 = Button(main_win, image=img_1, bg="#282828", bd=0, activebackground="#282828", command=one)
btn_1.place(x=10, y=110)

# 2
img_2 = PhotoImage(file="Images/2.png").subsample(4, 4)
btn_2 = Button(main_win, image=img_2, bg="#282828", bd=0, activebackground="#282828", command=two)
btn_2.place(x=90, y=110)

# 3
img_3 = PhotoImage(file="Images/3.png").subsample(4, 4)
btn_3 = Button(main_win, image=img_3, bg="#282828", bd=0, activebackground="#282828", command=three)
btn_3.place(x=170, y=110)

# 4
img_4 = PhotoImage(file="Images/4.png").subsample(4, 4)
btn_4 = Button(main_win, image=img_4, bg="#282828", bd=0, activebackground="#282828", command=four)
btn_4.place(x=10, y=169)

# 5
img_5 = PhotoImage(file="Images/5.png").subsample(4, 4)
btn_5 = Button(main_win, image=img_5, bg="#282828", bd=0, activebackground="#282828", command=five)
btn_5.place(x=90, y=169)

# 6
img_6 = PhotoImage(file="Images/6.png").subsample(4, 4)
btn_6 = Button(main_win, image=img_6, bg="#282828", bd=0, activebackground="#282828", command=six)
btn_6.place(x=170, y=169)

# 7
img_7 = PhotoImage(file="Images/7.png").subsample(4, 4)
btn_7 = Button(main_win, image=img_7, bg="#282828", bd=0, activebackground="#282828", command=seven)
btn_7.place(x=10, y=228)

# 8
img_8 = PhotoImage(file="Images/8.png").subsample(4, 4)
btn_8 = Button(main_win, image=img_8, bg="#282828", bd=0, activebackground="#282828", command=eight)
btn_8.place(x=90, y=228)

# 9
img_9 = PhotoImage(file="Images/9.png").subsample(4, 4)
btn_9 = Button(main_win, image=img_9, bg="#282828", bd=0, activebackground="#282828", command=nine)
btn_9.place(x=170, y=228)

# 0
img_0 = PhotoImage(file="Images/0.png").subsample(4, 4)
btn_0 = Button(main_win, image=img_0, bg="#282828", bd=0, activebackground="#282828", command=zero)
btn_0.place(x=90, y=287)

# =
img_equals = PhotoImage(file="Images/=.png").subsample(4, 4)
btn_equals = Button(main_win, image=img_equals, bg="#282828", bd=0, activebackground="#282828", command=equal)
btn_equals.place(x=330, y=110)

# /
img_div = PhotoImage(file="Images/div.png").subsample(4, 4)
btn_div = Button(main_win, image=img_div, bg="#282828", bd=0, activebackground="#282828", command=divide)
btn_div.place(x=250, y=287)

# ×
img_multiply = PhotoImage(file="Images/×.png").subsample(4, 4)
btn_multiply = Button(main_win, image=img_multiply, bg="#282828", bd=0, activebackground="#282828", command=multiply)
btn_multiply.place(x=250, y=228)

# +
img_plus = PhotoImage(file="Images/+.png").subsample(4, 4)
btn_plus = Button(main_win, image=img_plus, bg="#282828", bd=0, activebackground="#282828", command=plus)
btn_plus.place(x=250, y=110)

# -
img_minus = PhotoImage(file="Images/-.png").subsample(4, 4)
btn_minus = Button(main_win, image=img_minus, bg="#282828", bd=0, activebackground="#282828", command=minus)
btn_minus.place(x=250, y=169)

# C
img_C = PhotoImage(file="Images/C.png").subsample(4, 4)
btn_C = Button(main_win, image=img_C, bg="#282828", bd=0, activebackground="#282828", command=delete)
btn_C.place(x=10, y=287)

# ←
img_arrow = PhotoImage(file="Images/arrow.png").subsample(4, 4)
btn_arrow = Button(main_win, image=img_arrow, bg="#282828", bd=0, activebackground="#282828", command=erase)
btn_arrow.place(x=170, y=287)

# (
img_bracket_1 = PhotoImage(file="Images/(.png").subsample(4, 4)
btn_bracket_1 = Button(main_win, image=img_bracket_1, bg="#282828", bd=0, activebackground="#282828", command=bracket_1)
btn_bracket_1.place(x=330, y=169)

# )
img_bracket_2 = PhotoImage(file="Images/).png").subsample(4, 4)
btn_bracket_2 = Button(main_win, image=img_bracket_2, bg="#282828", bd=0, activebackground="#282828", command=bracket_2)
btn_bracket_2.place(x=330, y=228)

# ^
img_bracket_s = PhotoImage(file="Images/^.png").subsample(4, 4)
btn_bracket_s = Button(main_win, image=img_bracket_s, bg="#282828", bd=0, activebackground="#282828", command=degree)
btn_bracket_s.place(x=330, y=287)

# Copy
img_copy = PhotoImage(file="Images/copy.png").subsample(4, 4)
btn_copy = Button(main_win, image=img_copy, bg="#282828", bd=0, activebackground="#282828", command=copy)
btn_copy.place(x=330, y=75)

"""Output line"""

output_line = Label(main_win, bg="#F5F5DC", height=2, width=32, text=user_input, font=("Arial", 16), anchor=W)
output_line.place(x=13, y=15)

output_line_2 = Label(main_win, bg="#4C5866", height=1, width=28, text=output_text, font=("Arial", 14), anchor=W,
                      foreground="#B0B7C6")
output_line_2.place(x=13, y=74)

mainloop()
