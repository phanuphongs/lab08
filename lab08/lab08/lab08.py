import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple drawing")
<<<<<<< HEAD
 
=======

>>>>>>> origin/master

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([
                       QPoint(70, 100), QPoint(100,110),
                       QPoint(130, 100), QPoint(100, 150)
                       ])
        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)

        p.drawPolygon([
                       QPoint(50, 200), QPoint(150, 200), QPoint(100, 400),
                       ])

<<<<<<< HEAD
        p.end()


class Simple_drawing_window1(Simple_drawing_window):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("drawing square")
    
    
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setBrush(QColor(102, 255, 178))
        p.drawRect(75, 200, 50, 50)
        p.setPen(QColor(0, 0, 255))
        p.setBrush(QColor(255, 0, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)

    
        
     
        p.end()


def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_ben()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
=======

        p.end()
>>>>>>> origin/master
