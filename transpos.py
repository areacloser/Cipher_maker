import math
import pyperclip
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

def main():
    win = Tk()
    win.resizable(0, 0)
    win.geometry("+300+300")
    win.iconbitmap("cip.ico")
    win.title("编写置换密码")
    fm_1 = Frame(win)
    fm_2 = Frame(win)
    fm_1.pack()
    fm_2.pack()

    lab_1 = Label(fm_1, text="在下方输入要加密的字符（只能是英文字符）", font="songti 16 bold")
    lab_1.pack()
    txt_1 = Text(fm_1, width=75, height=10)
    txt_1.pack()
    lab_2 = Label(fm_1, text="在下方输入密钥（请输入整数）", font="songti 16 bold")
    lab_2.pack()
    ent = Entry(fm_1, width=75)
    ent.pack()
    lab_3 = Label(fm_1, text="下方将显示加密后的字符（右击文本框可复制到剪贴板中）", font="songti 16 bold")
    lab_3.pack()
    txt_2 = Text(fm_1, width=75, height=10, state="disabled")
    txt_2.pack()

    def encry(k, m):
        encr_text = [""] * k
        for col in range(k):
            index = col
            while index < len(m):
                encr_text[col] += m[index]
                index += k
        return "".join(encr_text)

    def trp():
        try:
            key = int(ent.get())
        except:
            showwarning("警告", "请输入有效的整数密钥！")
            return
        text = txt_1.get("0.0", END)[0:-1]
        encr = encry(key, text)
        txt_2.config(state="normal")
        txt_2.delete("0.0", END)
        txt_2.insert("0.0", encr)
        txt_2.config(state="disabled")
      
    def copy(event):
        if txt_2.get("0.0", END) != "\n":
            pyperclip.copy(txt_2.get("0.0", END)[0:-1])
            showinfo("提示", "复制成功！")
        else:
            showwarning("警告", "不能复制空字符串！")
        
    btn_1 = Button(fm_2, text="加密", command=trp)
    btn_1.grid(row=1, column=1, padx=100, ipadx=10, ipady=10)
    btn_2 = Button(fm_2, text="退出", command=win.destroy)
    btn_2.grid(row=1, column=2, padx=100, ipadx=10, ipady=10)
    txt_2.bind("<Button-3>", copy)
    win.mainloop()

def main_2():
    win = Tk()
    win.resizable(0, 0)
    win.geometry("+300+300")
    win.iconbitmap("cip.ico")
    win.title("解密置换密码")
    fm_1 = Frame(win)
    fm_2 = Frame(win)
    fm_1.pack()
    fm_2.pack()

    lab_1 = Label(fm_1, text="在下方输入要解密的字符（只能是英文字符）", font="songti 16 bold")
    lab_1.pack()
    txt_1 = Text(fm_1, width=75, height=10)
    txt_1.pack()
    lab_2 = Label(fm_1, text="在下方输入密钥（请输入整数）", font="songti 16 bold")
    lab_2.pack()
    ent = Entry(fm_1, width=75)
    ent.pack()
    lab_3 = Label(fm_1, text="下方将显示解密后的字符（右击文本框可复制到剪贴板中）", font="songti 16 bold")
    lab_3.pack()
    txt_2 = Text(fm_1, width=75, height=10, state="disabled")
    txt_2.pack()

    def decry(k, m):
        col_num = int(math.ceil(len(m) / float(k)))
        row_num = k
        shaded_box_num = (col_num * row_num) - len(m)
        decr_text = [""] * col_num
        col = 0
        row = 0
        for sym in m:
            decr_text[col] += sym
            col += 1
            if (col == col_num) or (col == col_num - 1 and row >= row_num - shaded_box_num):
                col = 0
                row += 1
        return "".join(decr_text)
        
    def trp():
        try:
            key = int(ent.get())
        except:
            showwarning("警告", "请输入有效的整数密钥！")
            return
        text = txt_1.get("0.0", END)[0:-1]
        decr = decry(key, text)
        txt_2.config(state="normal")
        txt_2.delete("0.0", END)
        txt_2.insert("0.0", decr)
        txt_2.config(state="disabled")
      
    def copy(event):
        if txt_2.get("0.0", END) != "\n":
            pyperclip.copy(txt_2.get("0.0", END)[0:-1])
            showinfo("提示", "复制成功！")
        else:
            showwarning("警告", "不能复制空字符串！")
        
    btn_1 = Button(fm_2, text="解密", command=trp)
    btn_1.grid(row=1, column=1, padx=100, ipadx=10, ipady=10)
    btn_2 = Button(fm_2, text="退出", command=win.destroy)
    btn_2.grid(row=1, column=2, padx=100, ipadx=10, ipady=10)
    txt_2.bind("<Button-3>", copy)
    win.mainloop()

if __name__ == "__main__":
    main()
