# -*- coding: utf8 -*-
import turtle             # 匯入turtle套件，允許我們使用turtle指令
window = turtle.Screen()  # 產生畫布以進行畫圖
john = turtle.Turtle()    # 建立一個海龜turtle，它的名字叫john

john.forward(50)          # 告訴海龜往前走50個單位
john.left(90)             # 告訴海龜左轉90度
john.forward(50)          # 告訴海龜往前走30個單位
john.left(90)
john.forward(50)          # 告訴海龜往前走30個單位
john.left(90)
john.forward(50)          # 告訴海龜往前走30個單位
window.exitonclick()      # 等待使用者關閉視窗