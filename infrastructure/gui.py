#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import Tk
import Tkinter
import tkFileDialog
import tkMessageBox


class Application(Tk):
    def __init__(self, master=None):
        Tk.__init__(self, master)
        self._enodebIpVar=Tkinter.StringVar()
        self._oFilePath=Tkinter.StringVar()
        self._runInfoVar=Tkinter.StringVar()
        self._createWidgets()

    def _createWidgets(self):
        Tkinter.Label(self, text="eNodeb Ip:", font=("Arial", 10), width=15, height=1)\
                                     .grid(row=1,column=1,padx=10,pady=10)
        self._enodebIpEntry = Tkinter.Entry(self, textvariable = self._enodebIpVar)
        self._enodebIpEntry.grid(row=1,column=2,padx=10,pady=10)
        self._enodebIpVar.set('XX.XX.XX.XX')
                                
        Tkinter.Label(self, text="DotO File:", font=("Arial", 10), width=15, height=1)\
                                  .grid(row=2,column=1,padx=10,pady=10)
        Tkinter.Entry(self, textvariable = self._oFilePath).grid(row=2,column=2,padx=10,pady=10)  
                                                     
        Tkinter.Button(self, text='DotO file path', command=self.obtain_file_path)\
                                   .grid(row=2,column=3,padx=10,pady=10)

        Tkinter.Button(self, text='Confirm', command=self.confirm)\
                                     .grid(row=3,column=2,padx=10,pady=10)
        
        Tkinter.Label(self, text="Warn:删除版本库版本", bg='yellow',font=("Arial", 9), width=17, height=1)\
                                  .grid(row=3,column=3,padx=10,pady=10)
                                   
        Tkinter.Label(self, text="Run Info:", font=("Arial", 10), width=15, height=1)\
                               .grid(row=4,column=1,padx=10,pady=10)
        
        self._listbox = Tkinter.Listbox(self,listvariable=self._runInfoVar)
        self._listbox.grid(row=4,column=2,padx=10,pady=10)
        
        Tkinter.Button(self, text='Exit', command=quit, background='red', width = 10)\
                                     .grid(row=4,column=3,padx=10,pady=10)
        
    def obtain_file_path(self):
        filename = tkFileDialog.askopenfilename(initialdir = 'E:/Python')
        self._oFilePath.set(filename)
        
    def obtain_enodeb_ip(self):
        self._enodebIpVar = self._enodebIpEntry.get()
        return self._enodebIpVar
    
    def confirm(self):
        self.obtain_enodeb_ip()
        if(self._enodebIpVar==''):
            tkMessageBox.showwarning(title='Hi', message='eNodebIp Is NULL!')
            return
        self.print_run_info(self._enodebIpVar)
        name = self._oFilePath.get()
        if(name==''):
            tkMessageBox.showwarning(title='Hi', message='File Path Is NULL!')
            return
#         self.print_run_info(name)
        
    def print_run_info(self, s):
        i = 1
        self._listbox.insert(i, s)
        i = i+1
        return
    
if __name__ == '__main__':
    app = Application()
    app.geometry('450x350')
    app.title('My Tk')    
    app.mainloop()