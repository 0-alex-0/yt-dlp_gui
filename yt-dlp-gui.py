#! /usr/bin/env python3

from tkinter import *
from tkinter import ttk
from re import findall

import subprocess

#def
def urlFeeder():
  url = urlIn.get("1.0",'end-1c')
  print(url)
  checkDownload = subprocess.getoutput('yt-dlp {}'.format(url))
  print(checkDownload)
  
tk = Tk()
tk.title("YT-DLP GUI")
mainFrame = Frame(tk, relief=RIDGE, borderwidth=2, bg="grey")
mainFrame.pack()

urlFrame = Frame(mainFrame, relief=RIDGE, borderwidth=2, bg="grey")
Title = Label(urlFrame, text="URL", font=('Arial', 14))
urlIn = Text(urlFrame, width=36, height=1, font=('Arial', 14))
urlBtn = Button(urlFrame, text="Download", command=urlFeeder)

urlFrame.pack(side=LEFT, anchor=W)
Title.pack(side=TOP, anchor=N)
urlBtn.pack(side=LEFT, anchor=W)
urlIn.pack(side=RIGHT, anchor=E)

tk.mainloop()
