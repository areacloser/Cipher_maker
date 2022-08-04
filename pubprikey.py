import pyperclip, random, prime, crypto
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

def main():
    win = Tk()
    win.resizable(0, 0)
    win.geometry("+300+300")
    win.iconbitmap("cip.ico")
    win.title("创建公钥、私钥")
    
    fm_1 = Frame(win)
    fm_2 = Frame(win)
    fm_1.pack()
    fm_2.pack()

    lab_1 = Label(fm_1, text="在下方输入密钥长度（最好是1024位，否则可能卡死）", font="songti 16 bold")
    lab_1.pack()
    ent = Entry(fm_1, width=75)
    ent.pack()
    lab_2 = Label(fm_1, text="下方将显示公钥（右击文本框可复制到剪贴板中）", font="songti 16 bold")
    lab_2.pack()
    txt_1 = Text(fm_1, width=75, height=10, state="disabled")
    txt_1.pack()
    lab_3 = Label(fm_1, text="下方将显示私钥（右击文本框可复制到剪贴板中）", font="songti 16 bold")
    lab_3.pack()
    txt_2 = Text(fm_1, width=75, height=10, state="disabled")
    txt_2.pack()

    def mpk():
        try:
            size = int(ent.get())
        except:
            showwarning("警告", "请输入整数!")
            return
        p = 0
        q = 0
        while p == q:
            p = prime.large_prime(size)
            q = prime.large_prime(size)
        n = p * q
        while True:
            e = random.randrange(2 ** (size-1), 2 ** (size))
            if crypto.gcd(e, (p -1) * (q - 1)) == 1:
                break
        d = crypto.fmi(e, (p - 1) * (q - 1))
        pubk = (n, e)
        prik = (n, d)
        txt_1.config(state="normal")
        txt_1.delete("0.0", END)
        txt_1.insert("0.0", str(pubk))
        txt_1.config(state="disabled")
        txt_2.config(state="normal")
        txt_2.delete("0.0", END)
        txt_2.insert("0.0", str(prik))
        txt_2.config(state="disabled")
        

    def copy_1(event):
        if txt_1.get("0.0", END) != "\n":
            pyperclip.copy(txt_1.get("0.0", END)[0:-1])
            showinfo("提示", "复制成功！")
        else:
            showwarning("警告", "不能复制空字符串！")

    def copy_2(event):
        if txt_2.get("0.0", END) != "\n":
            pyperclip.copy(txt_2.get("0.0", END)[0:-1])
            showinfo("提示", "复制成功！")
        else:
            showwarning("警告", "不能复制空字符串！")

    btn_1 = Button(fm_2, text="创建", command=mpk)
    btn_1.grid(row=1, column=1, padx=100, ipadx=10, ipady=10)
    btn_2 = Button(fm_2, text="退出", command=win.destroy)
    btn_2.grid(row=1, column=2, padx=100, ipadx=10, ipady=10)
    
    txt_1.bind("<Button-3>", copy_1)
    txt_2.bind("<Button-3>", copy_2)
    win.mainloop()

if __name__ == "__main__":
    main()
