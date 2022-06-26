from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt

import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Simple program")
        self.setGeometry(300, 250, 350, 200)  # (300, 250) от левого верхнего угла
        # ширина, высота

        self.new_text = QtWidgets.QLabel(self)

        self.slider = QtWidgets.QSlider(Qt.Horizontal, self)
        self.slider.move(200, 100)
        self.slider.adjustSize()
        self.slider.setTickInterval(5)
        self.slider.setPageStep(1)
        self.slider.setValue(10)
        self.slider.setRange(10, 40)
        self.slider.setFocusPolicy(Qt.StrongFocus)
        self.slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.slider.setSingleStep(1)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self)
        vbox.addWidget(self.slider)
        #self.setLayout(vbox)

        self.slider.valueChanged.connect(QtWidgets.QLCDNumber(self).display)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Hello")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("Push")
        self.btn.adjustSize()
        self.btn.clicked.connect(self.add_label)

    def add_label(self):
        self.new_text.setText("New Text")
        self.new_text.move(100, 50)
        self.new_text.adjustSize()
        print(self.slider.value())





def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())  # корректное завершение


if __name__ == "__main__":
    application()
