# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 09:26:08 2019

@author: Oluleye
"""

from tkinter import*
from PIL import Image, ImageTk

class Traffic:
    def __init__(self):
        self.root=Tk()
        self.root.title('TrafficLight')
        #self.frm = Frame(self.root, width=400, height=400).pack()
        self.dim1 = 50,10,250,180
        self.dim2 = 50,190,250,380
        self.dim3 = 50,390,250,580
        self.can = Canvas(self.root, width=300, height=600, bg='black')
        self.can_red = self.can.create_oval(self.dim1, fill='grey')
        self.can_yel = self.can.create_oval(self.dim2, fill='grey')
        self.can_gre = self.can.create_oval(self.dim3, fill='grey')
        self.can.pack(side='top')
        self.start_btn = Button(self.root, text='Start', command=self.start).pack(side='top')
        self.stop_btn = Button(self.root, text='Stop', command=self.stop).pack(side='top')
        #self.strt_btn = Button(self.can).pack(side='bottom')
        self.root.mainloop()
        self.stop_var = False
        
    def start(self):
        self.stop_var=False
        self.red_light()
        
    def red_light(self):
        if self.stop_var:
            return
        self.can_red = self.can.create_oval(self.dim1, fill='red')
        self.can_yel = self.can.create_oval(self.dim2, fill='grey')
        self.can_gre = self.can.create_oval(self.dim3, fill='grey')
        self.can.after(5000,self.yellow_light)
    def yellow_light(self):
        if self.stop_var:
            return
        self.can_red = self.can.create_oval(self.dim1, fill='grey')
        self.can_yel = self.can.create_oval(self.dim2, fill='yellow')
        self.can_gre = self.can.create_oval(self.dim3, fill='grey')
        self.can.after(5000,self.green_light)
    def green_light(self):
        if self.stop_var:
            return
        self.can_red = self.can.create_oval(self.dim1, fill='grey')
        self.can_yel = self.can.create_oval(self.dim2, fill='grey')
        self.can_gre = self.can.create_oval(self.dim3, fill='green')
        self.can.after(5000,self.red_light)
    def stop(self):

        self.can_red = self.can.create_oval(self.dim1, fill='grey')
        self.can_yel = self.can.create_oval(self.dim2, fill='grey')
        self.can_gre = self.can.create_oval(self.dim3, fill='grey')
        self.stop_var = True

tr = Traffic()