from tkinter import *
from tkinter.ttk import *

def main():
    win = Tk()
    win.resizable(0, 0)
    win.geometry("+300+300")
    win.iconbitmap("cip.ico")
    win.title("关于本软件")
    txt = Text(win)
    txt.insert(INSERT, """Cipher Maker v0.1.9-alpha (1435 lines) -- By lanlan2_
You should look at those words...\n
\"The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!\"""")
    txt.config(state="disabled")
    txt.pack()
    win.mainloop()

if __name__ == "__main__":
    main()
