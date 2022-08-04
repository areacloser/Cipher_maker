import pyperclip, random
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    win = Tk()
    win.resizable(0, 0)
    win.geometry("+300+300")
    win.iconbitmap("cip.ico")
    win.title("创建打乱的大写字母表")
    fm_1 = Frame(win)
    fm_2 = Frame(win)
    fm_1.pack()
    fm_2.pack()
    lab = Label(fm_1, text="下方将显示打乱的大写字母表（右击文本框可复制到剪贴板中）", font="songti 16 bold")
    lab.pack()
    txt = Text(fm_1, width=75, height=10, state="disabled")
    txt.pack()

    def rnd():
        key_list = list(LETTERS)
        random.shuffle(key_list)
        key = "".join(key_list)
        txt.config(state="normal")
        txt.delete("0.0", END)
        txt.insert("0.0", key)
        txt.config(state="disabled")
        

    def copy(event):
        if txt.get("0.0", END) != "\n":
            pyperclip.copy(txt.get("0.0", END)[0:-1])
            showinfo("提示", "复制成功！")
        else:
            showwarning("警告", "不能复制空字符串！")
        
    btn_1 = Button(fm_2, text="创建", command=rnd)
    btn_1.grid(row=1, column=1, padx=100, ipadx=10, ipady=10)
    btn_2= Button(fm_2, text="退出", command=win.destroy)
    btn_2.grid(row=1, column=2, padx=100, ipadx=10, ipady=10)
    txt.bind("<Button-3>", copy)
    win.mainloop()

if __name__ == "__main__":
    main()
