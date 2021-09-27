#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import serial
from PyQt5.QtCore import pyqtSignal,QThread

class serialThreadClass(QThread):
    mesaj=pyqtSignal(str)
    
    def __init__(self,parent=None):
        super(serialThreadClass,self).__init__(parent)
        self.seriport=serial.Serial('COM6',9600)
        #self.seriport.open()
    
    def run(self):
        while True:
            veri=self.seriport.readline()
            self.mesaj.emit(str(veri))
            print(veri)
    
    #def sendSerial(self):
     #   self.seriport.write(b'A')
        

