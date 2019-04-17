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

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(100, 50)
        self.textbox1.resize(60, 20)
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(100, 80)
        self.textbox2.resize(60, 20)
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(130, 110)
        self.textbox3.resize(60, 20)


    def toss(self):
        #輸入第一組數據
        n = int(self.textbox1.text())
        d = int(self.textbox2.text())
        theta = float(self.textbox3.text())

        #丟硬幣
        k = np.arange(d) 

        a = np.random.binomial(n,theta,d)

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


        plt.fill(np.array(p), np.array(list2), color = "g", alpha = 0.3)

        plt.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())