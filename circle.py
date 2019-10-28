#
# import turtle
# import math
# import random
# wn = turtle.Screen()
# wn.bgcolor('black')
# Albert = turtle.Turtle()
# Albert.speed(0)
# Albert.color('white')
# rotate=int(360)
# def drawCircles(t,size):
#     for i in range(10):
#         t.circle(size)
#         size=size-4
# def drawSpecial(t,size,repeat):
#   for i in range (repeat):
#     drawCircles(t,size)
#     t.right(360/repeat)
# drawSpecial(Albert,100,10)
# Steve = turtle.Turtle()
# Steve.speed(0)
# Steve.color('yellow')
# rotate=int(90)
# def drawCircles(t,size):
#     for i in range(4):
#         t.circle(size)
#         size=size-10
# def drawSpecial(t,size,repeat):
#     for i in range (repeat):
#         drawCircles(t,size)
#         t.right(360/repeat)
# drawSpecial(Steve,100,10)
# Barry = turtle.Turtle()
# Barry.speed(0)
# Barry.color('blue')
# rotate=int(80)
# def drawCircles(t,size):
#     for i in range(4):
#         t.circle(size)
#         size=size-5
# def drawSpecial(t,size,repeat):
#     for i in range (repeat):
#         drawCircles(t,size)
#         t.right(360/repeat)
# drawSpecial(Barry,100,10)
# Terry = turtle.Turtle()
# Terry.speed(0)
# Terry.color('orange')
# rotate=int(90)
# def drawCircles(t,size):
#     for i in range(4):
#         t.circle(size)
#         size=size-19
# def drawSpecial(t,size,repeat):
#     for i in range (repeat):
#         drawCircles(t,size)
#         t.right(360/repeat)
# drawSpecial(Terry,100,10)
# Will = turtle.Turtle()
# Will.speed(0)
# Will.color('pink')
# rotate=int(90)
# def drawCircles(t,size):
#     for i in range(4):
#         t.circle(size)
#         size=size-20
# def drawSpecial(t,size,repeat):
#     for i in range (repeat):
#         drawCircles(t,size)
#         t.right(360/repeat)
# drawSpecial(Will,100,10)

# import turtle
# my_turtle = turtle.Turtle()
# my_turtle.speed(0)
# def main(length, angle):
#         my_turtle.forward(length)
#         my_turtle.right(angle)
#         my_turtle.forward(length)
#         my_turtle.right(angle)
# #
# for circle in range(100):
#     main(200, 90)
#     main(200, 95)

# import turtle
# my_turtle = turtle.Turtle()
#
# my_turtle.speed(0)
# def main(length, angle):
#     for i in range(4):
#         my_turtle.forward(length)
#         my_turtle.right(angle)
#
#
# for circle in range(100):
#     main(100, 90)
#     my_turtle.right(10)

import turtle
my_turtle = turtle.Turtle()
 # my_turtle.speed(0)
for i in range(10):
    my_turtle.circle(100)
    my_turtle.forward(100)
    my_turtle.circle(100)
    my_turtle.right(90)
    my_turtle.forward(-100)

