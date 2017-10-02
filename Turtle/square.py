# -*- coding: utf8 -*-
import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
john = turtle.Turtle()
john.color("blue")

john.penup()                      # 提筆
size = 50
#shapes: “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
#往左上角移動
john.shape("turtle")
john.left(90)
john.forward(220)
john.right(90)
john.backward(250)
#開始蓋章
john.stamp()
for i in range(5):
    john.right(90)
    john.forward(50)
    john.left(90)
    for j in range(5):
        john.forward(size)       # 往前走
        john.stamp()
    john.backward(size*5)

john.left(90)
john.forward(50*5)
john.right(90)

window.exitonclick()