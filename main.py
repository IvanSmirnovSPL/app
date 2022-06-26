from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt

import sys

from my_slider import MySlider, Point


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Simple program")
        self.setGeometry(300, 250, 350, 200)  # (300, 250) от левого верхнего угла
        # ширина, высота

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Hello")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.move(10, 160)
        self.btn1.setText("Edit")
        self.btn1.adjustSize()
        self.btn1.clicked.connect(self.add_label)

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.move(120, 160)
        self.btn2.setText("Apply")

        self.slider = MySlider(self, self.btn2, Point(200, 100), range(0, 5))

        '''self.slider = QtWidgets.QSlider(Qt.Horizontal, self)
        self.slider.move(200, 100)
        self.slider.adjustSize()
        self.slider.setTickInterval(5)
        self.slider.setPageStep(1)
        self.slider.setValue(10)
        self.slider.setRange(10, 40)
        self.slider.setFocusPolicy(Qt.StrongFocus)
5        self.slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.slider.setSingleStep(1)

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self)
        self.vbox.addWidget(self.slider)
        #self.setLayout(vbox)

        self.slider.valueChanged.connect(QtWidgets.QLCDNumber(self).display)'''




    def add_label(self):
        self.new_text.setText("New Text")
        self.new_text.move(100, 50)
        self.new_text.adjustSize()
        #print(self.slider.value())





def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())  # корректное завершение


if __name__ == "__main__":
    application()
