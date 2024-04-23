import cv2 as cv
import numpy as np
import os
import glob
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from threading import Thread
import shutil

class Ui_MainWindow(object):
    FrameSlider : QSlider
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 1024)
        self.mw = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Image = QtWidgets.QLabel(self.centralwidget)
        self.Image.setText("")
        self.Image.setPixmap(QtGui.QPixmap("1_png_jpg.rf.16b774dc39f0f2d61f6b004910a91a51.jpg"))
        self.Image.setScaledContents(True)
        self.Image.setObjectName("Image")
        self.verticalLayout.addWidget(self.Image)
        self.FrameSlider = QtWidgets.QSlider(self.centralwidget)
        self.FrameSlider.setOrientation(QtCore.Qt.Horizontal)
        self.FrameSlider.setObjectName("FrameSlider")
        self.verticalLayout.addWidget(self.FrameSlider)
        self.ForwardButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ForwardButton.setFont(font)
        self.ForwardButton.setObjectName("ForwardButton")
        self.verticalLayout.addWidget(self.ForwardButton)
        self.BackwardButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BackwardButton.setFont(font)
        self.BackwardButton.setObjectName("BackwardButton")
        self.verticalLayout.addWidget(self.BackwardButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.ShowButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ShowButton.setFont(font)
        self.ShowButton.setObjectName("ShowButton")
        self.verticalLayout.addWidget(self.ShowButton)

        # ------------------------------------------------------------
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.HorizontalButton = QtWidgets.QPushButton(self.centralwidget)
        self.HorizontalButton.setObjectName("HorizontalButton")
        self.horizontalLayout.addWidget(self.HorizontalButton)
        self.VerticalButton = QtWidgets.QPushButton(self.centralwidget)
        self.VerticalButton.setObjectName("VerticalButton")
        self.horizontalLayout.addWidget(self.VerticalButton)
        self.Right_UPButton = QtWidgets.QPushButton(self.centralwidget)
        self.Right_UPButton.setObjectName("Right_UPButton")
        self.horizontalLayout.addWidget(self.Right_UPButton)
        self.Right_DOWNButton = QtWidgets.QPushButton(self.centralwidget)
        self.Right_DOWNButton.setObjectName("Right_DOWNButton")
        self.horizontalLayout.addWidget(self.Right_DOWNButton)
        self.UP_RightButton = QtWidgets.QPushButton(self.centralwidget)
        self.UP_RightButton.setObjectName("UP_RightButton")
        self.horizontalLayout.addWidget(self.UP_RightButton)
        self.DOWN_RightButton = QtWidgets.QPushButton(self.centralwidget)
        self.DOWN_RightButton.setObjectName("DOWN_RightButton")
        self.horizontalLayout.addWidget(self.DOWN_RightButton)
        self.FRONT = QtWidgets.QPushButton(self.centralwidget)
        self.FRONT.setObjectName("FRONT")
        self.horizontalLayout.addWidget(self.FRONT)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 870, 26))
        # ----------------------------------------------------------
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # ---------------------------------------------------------
        self.retranslateUi(MainWindow)
        self.FrameSlider.valueChanged['int'].connect(self.index_value) # type: ignore
        self.ForwardButton.clicked.connect(self.run_threads)
        self.BackwardButton.clicked.connect(self.run_threads)

        self.HorizontalButton.clicked.connect(self.run_threads)
        self.VerticalButton.clicked.connect(self.run_threads)
        self.Right_UPButton.clicked.connect(self.run_threads)
        self.Right_DOWNButton.clicked.connect(self.run_threads)
        self.UP_RightButton.clicked.connect(self.run_threads)
        self.DOWN_RightButton.clicked.connect(self.run_threads)
        self.FRONT.clicked.connect(self.run_threads)
        self.ShowButton.clicked.connect(self.run_threads)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # ---------------------------------------------------------
        self.c       = -1
        self.Pics = None
        self.notePath = None
        self.image_path = None
        self.imagesNames =[]

    def run_threads(self):
        """ Run a separate thread to execute aha function """
        self.thread = [Thread(target=self.aha, args=(self.mw.sender().objectName(),))]
        self.thread[0].start()

    def aha(self, notePath):
        """ Function to perform operations based on button clicked """
        self.notePath = notePath
        self.imagesNames = glob.glob(f'*.jpg')
        self.FrameSlider.setMaximum(len(self.imagesNames))
        self.image_path = self.imagesNames[self.c]

        self.set_image()
        print(f'index: {self.c}')


    def index_check(self):
        """ Function to handle different button clicks and update the image """
        # If ShowButton is clicked, do nothing
        if self.notePath == 'ShowButton':
            pass

        # If ForwardButton is clicked, increment the index and wrap around if at the end
        elif self.notePath == 'ForwardButton':
            self.c += 1
            if self.c >= len(self.imagesNames) :
                self.c = 0
                print('all images are displayed')

        # If BackwardButton is clicked, decrement the index and wrap around if at the start
        elif self.notePath == 'BackwardButton':
            self.c -= 1
            if self.c == -1 :
                self.c = len(self.imagesNames)-1

        # If HorizontalButton is clicked, copy the image to the Horizontal folder and remove the original
        # Repeat the same for VerticalButton, Right_UPButton, Right_DOWNButton, UP_RightButton, DOWN_RightButton and FRONT Button
        elif self.notePath in ['HorizontalButton', 'VerticalButton', 'Right_UPButton', 'Right_DOWNButton',
                              'UP_RightButton', 'DOWN_RightButton', 'FRONT']:
            src = self.image_path
            dst = f'E:/CrocoProject/Line follower New/{self.notePath.split("Button")[0]}' + '/' + src
            shutil.copy(src, dst)
            os.remove(src)

        # If none of the above conditions are met, do nothing
        else:
            pass

    def index_value(self, value):
        """ Update the index and set the image """
        self.c = int(value)
        self.set_image()

    def set_image(self):
        """ Set the image on the Image label """
        self.index_check()
        img = cv.imread(self.imagesNames[self.c])
        image = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        FlippedImage = image
        ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0],
                                   QImage.Format_RGB888)
        Pic = ConvertToQtFormat.scaled(640, 640, Qt.KeepAspectRatio)
        self.Pics = (Pic)
        self.Image.setPixmap(QtGui.QPixmap.fromImage(self.Pics))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ForwardButton.setText(_translate("MainWindow", "Forward"))
        self.BackwardButton.setText(_translate("MainWindow", "Backward"))
        self.ShowButton.setText(_translate("MainWindow", "SHOW"))
        # --------------------------------------------------------------
        self.HorizontalButton.setText(_translate("MainWindow", "Horizontal"))
        self.VerticalButton.setText(_translate("MainWindow", "Vertical"))
        self.Right_UPButton.setText(_translate("MainWindow", "Right->UP"))
        self.Right_DOWNButton.setText(_translate("MainWindow", "Right->DOWN"))
        self.UP_RightButton.setText(_translate("MainWindow", "UP->Right"))
        self.DOWN_RightButton.setText(_translate("MainWindow", "DOWN->Right"))
        self.FRONT.setText(_translate("MainWindow", "FRONT"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



