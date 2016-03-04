import sys
from PySide.QtGui import *
from PySide.QtCore import *

class Freedraw(QWidget):
    """docstring for Freedraw"""
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple drawing")





def main():
    f = Freedraw()
