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
    win.title("创建限定长度的随机密钥")
    fm_1 = Frame(win)
    fm_2 = Frame(win)
    fm_1.pack()
    fm_2.pack()
    lab_1 = Label(fm_1, text="请输入字符长度（必须是整数）", font="songti 16 bold")
    lab_1.pack()
    ent = Entry(fm_1, width=75)
    ent.pack()
    lab_2 = Label(fm_1, text="下方将显示随机密钥（右击文本框可复制到剪贴板中）", font="songti 16 bold")
    lab_2.pack()
    txt = Text(fm_1, width=75, height=10, state="disabled")
    txt.pack()

    def rnd():
        letter_list = list(LETTERS)
        key_list = []       
        try:
            key_len = int(ent.get())
        except:
            showwarning("警告", "请输入整数！")
            return
        for _ in range(key_len):
            key_list.append(random.choice(letter_list))
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
