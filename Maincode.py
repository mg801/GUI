#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5.QtWidgets import QApplication,QWidget
import sys
import test
from serialThreadFile import serialThreadClass
class MainClass(QWidget,test.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.myserial=serialThreadClass()
        self.myserial.mesaj.connect(self.label.setText)
        self.myserial.start()
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    pen=MainClass()
    pen.show()
    app.exec_()

