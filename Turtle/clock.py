# -*- coding: utf8 -*-
import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
john = turtle.Turtle()
john.shape("turtle")
john.color("blue")

john.penup()                      # 提筆
deg=360/12
size = 150
#for i in range(12):
#        john.forward(size)       # 往前走
#        john.stamp()  # 蓋章
#        john.backward(size)
#        john.right(deg)           # 向右轉

size = 120
#shapes: “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
john.shape("turtle")
for i in range(12):
        john.penup()
        john.forward(size)       # 往前走
        john.pendown()
        john.forward(10)
        john.penup()
        john.forward(20)
        john.stamp()
        john.backward(size+30)
        john.right(deg)           # 向右轉
window.exitonclick()