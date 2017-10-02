# -*- coding: utf8 -*-
import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
john = turtle.Turtle()
john.color("blue")

size = 72*2
for i in range(5):
        john.forward(150)       # 往前走
        john.right(size)           # 向右轉

window.exitonclick()