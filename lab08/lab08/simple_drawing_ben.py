import lab08

class simple_drawing_ben(Simple_drawing_window):
    """docstring for simple_drawing_ben"""
    def __init__(self):
        super().__init__()
        self.rabbit = QImage("rabbit.jpg")

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))

        p.drawImage(QRect(200,100,320,320),self.rabbit)
        p.end()

