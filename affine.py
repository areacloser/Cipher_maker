import pyperclip, crypto
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

def main():
    win = Tk()
    win.resizable(0, 0)
    win.geometry("+300+300")
    win.iconbitmap("cip.ico")
    win.title("编写仿射密码")
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

    def get_key_parts(k):
        keyA = k // len(SYMBOLS)
        keyB = k % len(SYMBOLS)
        return (keyA, keyB)

    def aff():
        try:
            key = int(ent.get())
        except:
            showwarning("警告", "请输入有效的整数密钥！")
            return
        text = txt_1.get("0.0", END)[0:-1]
        kA, kB = get_key_parts(key)
        if kA == 1:
            showwarning("警告", "您的密钥会导致您的密码不安全！")
            return
        if kB == 0:
            showwarning("警告", "您的密钥会导致您的密码不安全！")
            return
        if kA < 0 or kB < 0 or kB > len(SYMBOLS) - 1:
            showwarning("警告", "密钥必须在合适的区间段内！")
            return
        if crypto.gcd(kA, len(SYMBOLS)) != 1:
            showwarning("警告", "密钥必须在合适的区间段内！")
            return
        encr = ""
        for sym in text:
            if sym in SYMBOLS:
                sym_index = SYMBOLS.find(sym)
                encr += SYMBOLS[(sym_index * kA + kB) % len(SYMBOLS)]
            else:
                encr += stm        
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
        
    btn_1 = Button(fm_2, text="加密", command=aff)
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
    win.title("解密仿射密码")
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

    def get_key_parts(k):
        keyA = k // len(SYMBOLS)
        keyB = k % len(SYMBOLS)
        return (keyA, keyB)

    def aff():
        try:
            key = int(ent.get())
        except:
            showwarning("警告", "请输入有效的整数密钥！")
            return
        text = txt_1.get("0.0", END)[0:-1]
        kA, kB = get_key_parts(key)
        if kA < 0 or kB < 0 or kB > len(SYMBOLS) - 1:
            showwarning("警告", "密钥必须在合适的区间段内！")
            return
        if crypto.gcd(kA, len(SYMBOLS)) != 1:
            showwarning("警告", "密钥必须在合适的区间段内！")
            return
        decr = ""
        MkA = crypto.fmi(kA, len(SYMBOLS))
        for sym in text:
            if sym in SYMBOLS:
                sym_index = SYMBOLS.find(sym)
                decr += SYMBOLS[(sym_index - kB) * MkA % len(SYMBOLS)]
            else:
                decr += stm        
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
        
    btn_1 = Button(fm_2, text="解密", command=aff)
    btn_1.grid(row=1, column=1, padx=100, ipadx=10, ipady=10)
    btn_2 = Button(fm_2, text="退出", command=win.destroy)
    btn_2.grid(row=1, column=2, padx=100, ipadx=10, ipady=10)
    txt_2.bind("<Button-3>", copy)
    win.mainloop()
    
if __name__ == "__main__":
    main()
