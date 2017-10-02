# -*- coding: utf8 -*-
import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
john = turtle.Turtle()
john.shape("turtle")
john.color("blue")

john.penup()                      # 提筆
size = 20
for i in range(30):
        john.stamp()             # 蓋章
        size = size + 3          # 逐漸增加每次往前的距離
        john.forward(size)       # 往前走
        john.right(24)           # 向右轉

window.exitonclick()