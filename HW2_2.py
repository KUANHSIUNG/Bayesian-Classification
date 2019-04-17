import sys, math
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
import random
import numpy as np
import scipy.stats as st
import matplotlib
import matplotlib.pyplot as plt
from collections import Counter


class MainWindow(QWidget):
    def __init__(self):
        self.title = 'Homework 2'
        self.img_width = 300
        self.img_height = 300
        self.initUI()

    def initUI(self):
        super().__init__()
        self.setWindowTitle(self.title)
        self.resize(self.img_width, self.img_height) 

        self.button1 = QPushButton(self) 
        self.button1.move(200,20)
        self.button1.resize(90, 260)
        self.button1.setText("計算")
        self.button1.clicked.connect(self.toss)

        self.label1 = QLabel('Case 1 :', self) ##case 1
        self.label1.move(20,20)
        self.label2 = QLabel('執行幾次(d) : ', self)
        self.label2.move(20,50)
        self.label3 = QLabel('丟幾次(n) : ', self)
        self.label3.move(20,80)
        self.label4 = QLabel('正面機率(theta) : ', self)
        self.label4.move(20,110)

        self.label5 = QLabel('Case 2 :', self) ##case 1
        self.label5.move(20,160)
        self.label6 = QLabel('執行幾次(d) : ', self)
        self.label6.move(20,190)
        self.label7 = QLabel('丟幾次(n) : ', self)
        self.label7.move(20,220)
        self.label8 = QLabel('正面機率(theta) : ', self)
        self.label8.move(20,250)

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(100, 50)
        self.textbox1.resize(60, 20)
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(100, 80)
        self.textbox2.resize(60, 20)
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(130, 110)
        self.textbox3.resize(60, 20)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(100, 190)
        self.textbox4.resize(60, 20)
        self.textbox5 = QLineEdit(self)
        self.textbox5.move(100, 220)
        self.textbox5.resize(60, 20)
        self.textbox6 = QLineEdit(self)
        self.textbox6.move(130, 250)
        self.textbox6.resize(60, 20)

    def toss(self):
        #輸入第一組數據
        n = int(self.textbox1.text())
        d = int(self.textbox2.text())
        theta = float(self.textbox3.text())
        #輸入的第二組數據
        n1 = int(self.textbox4.text())
        d1 = int(self.textbox5.text())
        theta1 = float(self.textbox6.text())
        mid_line = theta + (theta1 - theta) * ( n / (n+n1))
        #丟硬幣
        k = np.arange(d) 
        k1 = np.arange(d1) 
        a = np.random.binomial(n,theta,d)
        b = np.random.binomial(n1,theta1,d1)
        list1 = set(a)  
        list2 = []
        list_a = list(a)
        for i in list1:
            count1 = list_a.count(i)
            list2.append(count1)
        
        p = []
        for i in list1:
            prob = float(i) / float(n)
            p.append(prob)

        list3 = set(b)  
        list4 = []
        list_b = list(b)
        for i in list3:
            count2 = list_b.count(i)
            list4.append(count2)
        
        p1 = []
        for i in list3:
            prob = float(i) / float(n1)
            p1.append(prob)

        rate1 = []
        for i in a:
            if(i > (mid_line * 100) ):
                rate1.append(i)
        rate_len = len(rate1)
        a_len = len(a)
        rate_1 =  (a_len - (rate_len * 2)) / a_len

        rate2 = []
        for i in b:
            if(i < (mid_line * 100) ):
                rate2.append(i)
        rate_len2 = len(rate2)
        b_len = len(b)
        rate_2 =  (b_len - (rate_len2 * 2)) / b_len
        print("Case 1 classification rate : ",rate_1)
        print("Case 2 classification rate : ",rate_2)
        plt.fill(np.array(p), np.array(list2), color = "g", alpha = 0.3)
        plt.fill(np.array(p1), np.array(list4), color = "b", alpha = 0.3)
        plt.axvline(mid_line, 0, 1, linestyle= '--')
        plt.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
 