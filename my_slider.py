from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout,
                             QLabel, QApplication, QLineEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class MySlider():

    def __init__(self, window, button_apply, point, slider_range):
        self.window = window
        self.point = point
        self.slider_range = slider_range
        #self.button_edit = button_edit
        self.button_apply = button_apply
        #self.count = 0
        self.make_line()
        self.make_slider()
        self.make_signals()

    def make_line(self):
        self.line = QLineEdit(self.window)
        self.line.move(self.point.x, self.point.y + 30)

    def make_slider(self):
        self.slider = QSlider(Qt.Horizontal, self.window)
        self.slider.setRange(self.slider_range[0], self.slider_range[-1])
        self.slider.setFocusPolicy(Qt.NoFocus)
        self.slider.setPageStep(5)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.move(self.point.x, self.point.y)

    def value(self):
        return self.slider.value()


    def make_signals(self):
        self.slider.valueChanged.connect(self.updateLine)
        #self.button_edit.clicked.connect(self.updateCount)
        self.button_apply.clicked.connect(self.updateSlider)
        #self.line.textChanged.connect(self.updateSlider)

    def updateLine(self):
        #if self.count == 0:
        value = self.slider.value()
        self.line.setText(str(value))

    def updateSlider(self):
        value = self.line.text()
        #print(value, 'Apply', int(value) in self.slider_range, self.slider_range)
        if int(value) not in self.slider_range:
            value = self.slider_range[0]
        self.slider.setValue(int(value))
        #self.count = 0

'''    def updateCount(self):
        print("Edit")
        self.count = 1'''





