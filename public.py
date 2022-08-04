import pyperclip
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

def main():
    win = Tk()
    win.resizable(0, 0)
    win.geometry("+300+300")
    win.iconbitmap("cip.ico")
    win.title("编写简单代换密码")
    fm_1 = Frame(win)
    fm_2 = Frame(win)
    fm_1.pack()
    fm_2.pack()
