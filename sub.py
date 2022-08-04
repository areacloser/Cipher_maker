import pyperclip
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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

    lab_1 = Label(fm_1, text="在下方输入要加密的字符（只能是英文字符）", font="songti 16 bold")
    lab_1.pack()
    txt_1 = Text(fm_1, width=75, height=10)
    txt_1.pack()
    lab_2 = Label(fm_1, text="在下方输入密钥（打乱的大写字母表）", font="songti 16 bold")
    lab_2.pack()
    ent = Entry(fm_1, width=75)
    ent.pack()
    lab_3 = Label(fm_1, text="下方将显示加密后的字符（右击文本框可复制到剪贴板中）", font="songti 16 bold")
    lab_3.pack()
    txt_2 = Text(fm_1, width=75, height=10, state="disabled")
    txt_2.pack()
    
    def sub():
        key = ent.get()
        text = txt_1.get("0.0", END)[0:-1]
        k_list = list(key)
        letter_list = list(LETTERS)
        k_list.sort()
        letter_list.sort()
        if k_list != letter_list:
            showwarning("警告", "请输入有效的密钥！\n（注：可在工具菜单中创建打乱的大写字母表）")
            return
        encr = ""
        cA = LETTERS
        cB = key
        for sym in text:
              if sym.upper() in cA:
                  sym_index = cA.find(sym.upper())
                  if sym.isupper():
                      encr += cB[sym_index].upper()
                  else:
                    encr += cB[sym_index].lower()
              else:
                  encr += sym
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
        
    btn_1 = Button(fm_2, text="加密", command=sub)
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
    win.title("解密简单代换密码")
    fm_1 = Frame(win)
    fm_2 = Frame(win)
    fm_1.pack()
    fm_2.pack()

    lab_1 = Label(fm_1, text="在下方输入要解密的字符（只能是英文字符）", font="songti 16 bold")
    lab_1.pack()
    txt_1 = Text(fm_1, width=75, height=10)
    txt_1.pack()
    lab_2 = Label(fm_1, text="在下方输入密钥（打乱的大写字母表）", font="songti 16 bold")
    lab_2.pack()
    ent = Entry(fm_1, width=75)
    ent.pack()
    lab_3 = Label(fm_1, text="下方将显示解密后的字符（右击文本框可复制到剪贴板中）", font="songti 16 bold")
    lab_3.pack()
    txt_2 = Text(fm_1, width=75, height=10, state="disabled")
    txt_2.pack()
    
    def sub():
        key = ent.get()
        text = txt_1.get("0.0", END)[0:-1]
        k_list = list(key)
        letter_list = list(LETTERS)
        k_list.sort()
        letter_list.sort()
        if k_list != letter_list:
            showwarning("警告", "警告", "请输入有效的密钥！\n（注：可在工具菜单中创建打乱的大写字母表）")
            return
        decr = ""
        cA = key
        cB = LETTERS
        for sym in text:
              if sym.upper() in cA:
                  sym_index = cA.find(sym.upper())
                  if sym.isupper():
                      decr += cB[sym_index].upper()
                  else:
                    decr += cB[sym_index].lower()
              else:
                  decr += sym
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
        
    btn_1 = Button(fm_2, text="解密", command=sub)
    btn_1.grid(row=1, column=1, padx=100, ipadx=10, ipady=10)
    btn_2 = Button(fm_2, text="退出", command=win.destroy)
    btn_2.grid(row=1, column=2, padx=100, ipadx=10, ipady=10)
    txt_2.bind("<Button-3>", copy)
    win.mainloop()

if __name__ == "__main__":
    main()
