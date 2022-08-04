import pyperclip
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

def main():
    win = Tk()
    win.resizable(0, 0)
    win.geometry("+300+300")
    win.iconbitmap("cip.ico")
    win.title("统计字符长度")
    
    fm_1 = Frame(win)
    fm_2 = Frame(win)
    fm_1.pack()
    fm_2.pack()

    lab_1 = Label(fm_1, text="在下方输入要统计长度的字符", font="songti 16 bold")
    lab_1.pack()
    txt_1 = Text(fm_1, width=75, height=10)
    txt_1.pack()
    lab_2 = Label(fm_1, text="下方将显示字符长度（右击文本框可复制到剪贴板中）", font="songti 16 bold")
    lab_2.pack()
    txt_2 = Text(fm_1, width=75, height=10, state="disabled")
    txt_2.pack()

    def sln():
        text = txt_1.get("0.0", END)[0:-1]
        text_len = len(text)
        txt_2.config(state="normal")
        txt_2.delete("0.0", END)
        txt_2.insert("0.0", str(text_len))
        txt_2.config(state="disabled")
        
    def copy(event):
        if txt_2.get("0.0", END) != "\n":
            pyperclip.copy(txt_2.get("0.0", END)[0:-1])
            showinfo("提示", "复制成功！")
        else:
            showwarning("警告", "不能复制空字符串！")

    btn_1 = Button(fm_2, text="统计", command=sln)
    btn_1.grid(row=1, column=1, padx=100, ipadx=10, ipady=10)
    btn_2 = Button(fm_2, text="退出", command=win.destroy)
    btn_2.grid(row=1, column=2, padx=100, ipadx=10, ipady=10)
    
    txt_2.bind("<Button-3>", copy)
    win.mainloop()

if __name__ == "__main__":
    main()
