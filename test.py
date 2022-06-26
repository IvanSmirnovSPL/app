from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout,
                             QLabel, QApplication, QLineEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.smth = QLineEdit(self)

        hbox = QHBoxLayout()

        self.sld = QSlider(Qt.Horizontal, self)
        self.sld.setRange(0, 100)
        self.sld.setFocusPolicy(Qt.NoFocus)
        self.sld.setPageStep(5)

        self.sld.valueChanged.connect(self.updateLabel)
        self.smth.textChanged.connect(self.updateSlider)

        self.label = QLabel('0', self)
        self.label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label.setMinimumWidth(80)

        hbox.addWidget(self.sld)
        hbox.addSpacing(15)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QSlider')
        self.show()

    def updateLabel(self, value):

        self.smth.setText(str(value))
        
    def updateSlider(self):
        value = self.smth.text()
        self.sld.setValue(int(value))
        


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()