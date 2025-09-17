# Matthew Ren
# 9/17/25
# Mr. Scimeca
# Turtle Lab 
# in command prompt, type "pip install keyboard"
import turtle
import keyboard
import math

t = turtle.Turtle()
turtle.bgcolor("#3d3f45")

# AI did this formula for me cause my brain couldn't handle the math

def draw_oval_from_origin(origin_x, origin_y, width, height, heading):

    angle = math.radians(heading)
   
    center_x = origin_x - (height/2) * math.sin(angle)
    center_y = origin_y - (height/2) * math.cos(angle)
    t.penup()

    start_x = origin_x
    start_y = origin_y
    t.goto(start_x, start_y)
    t.setheading(heading)
    t.pendown()
    steps = 150
    for i in range(steps + 1):
        theta = 2 * math.pi * i / steps
   
        x = width * math.cos(theta)
        y = height * math.sin(theta)
      
        rot_x = x * math.cos(angle) - y * math.sin(angle)
        rot_y = x * math.sin(angle) + y * math.cos(angle)
        t.goto(center_x + rot_x, center_y + rot_y)
    t.penup()
    t.goto(origin_x, origin_y)
    t.pendown()

origin_x, origin_y = 0, 0  

while True:
    if keyboard.is_pressed('w'):
        t.forward(5)
    if keyboard.is_pressed('a'):
        t.left(5)
    if keyboard.is_pressed('d'):
        t.right(5)
    if keyboard.is_pressed('1'):
        t.color("red")
    if keyboard.is_pressed('2'):
        t.color("orange")
    if keyboard.is_pressed('3'):
        t.color("yellow")
    if keyboard.is_pressed('4'):
        t.color("green")
    if keyboard.is_pressed('5'):
        t.color("blue")
    if keyboard.is_pressed('6'):
        t.color("purple")
    if keyboard.is_pressed('7'):
        t.color("black")
    if keyboard.is_pressed('8'):
        t.speed(100)
        for f in range(10):
            heading = t.heading()
            draw_oval_from_origin(origin_x, origin_y, 40, 80, heading)
            t.left(10)
