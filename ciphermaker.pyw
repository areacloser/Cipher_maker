import about, reverse, caesar, transpos, affine, sub, vigenere, onetime, rndalpha, rndnkey, strilen, pubprikey, accarr
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

accounts = {"lanlan2_":"123456", "areacloser":"111111"}

win = Tk()
win.withdraw()
win.resizable(0, 0)
win.geometry("400x300+%d+%d" %((win.winfo_height()+200)//2, (win.winfo_width()+300)//2))
win.iconbitmap("cip.ico")
win.title("密码制作器 -- By lanlan2_")
log = Toplevel()
log.resizable(0, 0)
log.title("用户登录")
log.geometry("+300+300")
log.iconbitmap("cip.ico")
log.attributes("-topmost", 1)

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
        quit()
        
    else:
        return

log_btn_1 = Button(log_fm_2, text="登录", command=commit)
log_btn_1.pack(side=LEFT, padx=10)
log_btn_2 = Button(log_fm_2, text="取消", command=win.destroy)
log_btn_2.pack(side=RIGHT, padx=10)

log.protocol("WM_DELETE_WINDOW", askquit)
win.protocol("WM_DELETE_WINDOW", askquit)

m_main = Menu(win, relief=RAISED)
m_sub_1 = Menu(m_main, tearoff=0, relief=RAISED)
m_sub_2 = Menu(m_main, tearoff=0, relief=RAISED)
m_sub_3 = Menu(m_main, tearoff=0, relief=RAISED)

m_sub_1.add_command(label="反向密码（强度极低）", command=reverse.main)#OK=reverse)
m_sub_1.add_separator()
m_sub_1.add_command(label="凯撒密码（强度低）", command=caesar.main)#, command=caesar)
m_sub_1.add_command(label="置换密码（强度低）", command=transpos.main)#, command=transpos)
m_sub_1.add_command(label="仿射密码（强度低）", command=affine.main)#, command=affine)
m_sub_1.add_separator()
m_sub_1.add_command(label="简单代换密码（强度中）", command=sub.main)#, command=sub)
m_sub_1.add_command(label="维吉尼亚密码（强度中）", command=vigenere.main)#, command=vigenere)
m_sub_1.add_separator()
m_sub_1.add_command(label="一次一密（强度高）", command=onetime.main)#, command=onetime)
m_sub_1.add_command(label="公钥密码（强度较高）")#, command=pubkey)

m_sub_2.add_command(label="反向密码", command=reverse.main_2)#, command=reverse)
m_sub_2.add_command(label="凯撒密码", command=caesar.main_2)#, command=ceasar)
m_sub_2.add_command(label="置换密码", command=transpos.main_2)#, command=transpos)
m_sub_2.add_command(label="仿射密码", command=affine.main_2)#, command=affine)
m_sub_2.add_command(label="简单代换密码", command=sub.main_2)#, command=sub)
m_sub_2.add_command(label="维吉尼亚密码", command=vigenere.main_2)#, command=vigenere)
m_sub_2.add_command(label="一次一密", command=onetime.main_2)#, command=onetime)
m_sub_2.add_command(label="公钥密码")#, command=pubkey)

m_sub_3.add_command(label="创建打乱的大写字母表", command=rndalpha.main)
m_sub_3.add_command(label="创建限定长度的随机密钥", command=rndnkey.main)
m_sub_3.add_command(label="统计字符长度", command=strilen.main)
m_sub_3.add_command(label="创建公、私钥", command=pubprikey.main)

m_main.add_cascade(label="加密", menu=m_sub_1)
m_main.add_cascade(label="解密", menu=m_sub_2)
m_main.add_cascade(label="工具", menu=m_sub_3)
m_main.add_command(label="关于", command=about.main)
m_main.add_command(label="退出", command=askquit)

win.config(menu=m_main)
#win.quit()
win.mainloop()
