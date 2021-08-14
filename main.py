# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import turtle
import random
import tkinter

a=random.randint(20,220)
b=random.randint(450,670)
c=a
d=random.randint(470,670)
wn = turtle.Screen()
wn.setup(400,400)

aturtle = turtle.Turtle()
b=True
while b:
  aturtle.forward(a)
  aturtle.left(c)
  aturtle.forward(c)
run= True
while run:

    turtle.begin_fill()
    screen=turtle.Screen()
    screen.setup(1000,800)
    screen.bgpic()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
