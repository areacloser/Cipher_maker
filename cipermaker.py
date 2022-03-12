import about, reverse
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

accounts = {"lanlan2_":"123456", "areacloser":"111111"}

win = Tk()
win.withdraw()
win.resizable(0, 0)
win.geometry("400x300+%d+%d" %((win.winfo_height()+200)//2, (win.winfo_width()+300)//2))
win.iconbitmap("cip.ico")
win.title("密码制作器 V0.0.1 -- By lanlan2_")
log = Toplevel()
log.resizable(0, 0)
log.title("用户登录")
log.geometry("+400+400")
log.iconbitmap("cip.ico")

log_fm_1 = Frame(log)
log_fm_2 = Frame(log)
log_fm_1.pack(fill=BOTH, padx=10, pady=10)
log_fm_2.pack(fill=BOTH, padx=10, pady=10)
log_l1 = Label(log_fm_1, text="用户名：")
log_l1.grid(row=1, column=1, padx=5, pady=5)
log_e1 = Entry(log_fm_1, font="cosolas 12")
log_e1.grid(row=1, column=2, padx=5, pady=5)
log_l2 = Label(log_fm_1, text="密码：")
log_l2.grid(row=2, column=1, padx=5, pady=5)
log_e2 = Entry(log_fm_1, show="*", font="cosolas 12")
log_e2.grid(row=2, column=2, padx=5, pady=5)

def commit():
    usr_count = 0
    usr = log_e1.get()
    pwd = log_e2.get()
    if usr in accounts:
        if pwd == accounts[usr]:
            log.destroy()
            showinfo("提示", "登录成功！")
            win.deiconify()
        else:
            showwarning("警告", "输入信息错误！")
            return
    else:
        showwarning("警告", "输入信息错误！")
        return

def askquit():
    answer = askyesno("退出", "你想现在退出吗？")
    if answer == True:
        win.destroy()
    else:
        return

log_btn_1 = Button(log_fm_2, text="登录", command=commit)
log_btn_1.pack(side=LEFT, padx=10)
log_btn_2 = Button(log_fm_2, text="取消", command=win.destroy)
log_btn_2.pack(side=RIGHT, padx=10)

log.protocol("WM_DELETE_WINDOW", askquit)
m_main = Menu(win, relief=RAISED)
m_sub_1 = Menu(m_main, tearoff=0, relief=RAISED)
m_sub_2 = Menu(m_main, tearoff=0, relief=RAISED)

m_sub_1.add_command(label="反向密码（强度极低）", command=reverse.main)#, command=reverse)
m_sub_1.add_separator()
m_sub_1.add_command(label="凯撒密码（强度低）")#, command=ceasar)
m_sub_1.add_command(label="置换密码（强度低）")#, command=transpos)
m_sub_1.add_command(label="仿射密码（强度低）")#, command=affine)
m_sub_1.add_separator()
m_sub_1.add_command(label="简单代换密码（强度中）")#, command=sub)
m_sub_1.add_command(label="维吉尼亚密码（强度中）")#, command=vigenere)
m_sub_1.add_separator()
m_sub_1.add_command(label="一次一密（强度高）")#, command=onetime)
m_sub_1.add_command(label="公钥密码（强度较高）")#, command=pubkey)
m_sub_2.add_command(label="反向密码", command=reverse.main_2)#, command=reverse)
m_sub_2.add_command(label="凯撒密码")#, command=ceasar)
m_sub_2.add_command(label="置换密码")#, command=transpos)
m_sub_2.add_command(label="仿射密码")#, command=affine)
m_sub_2.add_command(label="简单代换密码")#, command=sub)
m_sub_2.add_command(label="维吉尼亚密码")#, command=vigenere)
m_sub_2.add_command(label="一次一密")#, command=onetime)
m_sub_2.add_command(label="公钥密码")#, command=pubkey)

m_main.add_cascade(label="加密", menu=m_sub_1)
m_main.add_cascade(label="解密", menu=m_sub_2)
m_main.add_command(label="关于", command=about.main)
m_main.add_command(label="退出", command=win.destroy)

win.config(menu=m_main)
#win.quit()
win.mainloop()
