from turtle import *


class Disk:


    def __init__(self,name,x,y,h,w,color):
        self.turtle = Turtle()
        self.name = name
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.tcolor = color

    def showdisk(self):
        self.turtle.seth(0)
        self.turtle.pu()
        self.turtle.goto(self.x,self.y)
        self.turtle.color(self.color)
        self.turtle.fillcolor(self.color)
        self.turtle.begin_fill()
        self.turtle.pd()
        self.turtle.fd(self.w/2)
        self.turtle.left(90)
        self.turtle.fd(self.h)
        self.turtle.left(90)
        self.turtle.fd(self.w)
        self.turtle.left(90)
        self.turtle.fd(self.h)
        self.turtle.left(90)
        self.turtle.fd(self.w/2)
        self.turtle.end_fill()





