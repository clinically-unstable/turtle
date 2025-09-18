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
t._tracer(0)
# ai math equation to make an oval 
def draw_oval(start_x, start_y, width, height, heading):

    angle = math.radians(heading)
    center_x = start_x - (0 * math.cos(angle) - (-height/2) * math.sin(angle))
    center_y = start_y - (0 * math.sin(angle) + (-height/2) * math.cos(angle))

    t.penup()
    t.goto(start_x, start_y)
    t.setheading(heading)
    t.pendown()
    steps = 25
   
    theta_start = 3 * math.pi / 2
    for i in range(steps + 1):
        theta = theta_start + (2 * math.pi * i / steps)
        x = width * math.cos(theta)
        y = height * math.sin(theta)
        rot_x = x * math.cos(angle) - y * math.sin(angle)
        rot_y = x * math.sin(angle) + y * math.cos(angle)
        t.goto(center_x + rot_x, center_y + rot_y)
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

oval_width = 80
oval_height = 160

start_x = t.xcor()
start_y = t.ycor()

theta_bottom = 3 * math.pi / 2
center_x = start_x
center_y = start_y

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
    if keyboard.is_pressed('9'):
        for f in range(9):
            heading = t.heading()
            t.speed(0)
            draw_oval(center_x, center_y, oval_width, oval_height, heading)
            t.left(10)
            t._tracer(1)
    if keyboard.is_pressed('8'):
        t.penup()
        t.goto(center_x-50, center_y-160)
        t.setheading(0)
        t.pendown()
        for m in range(180):
            t.speed(0)
            t.forward(200)
            t.right(2**2)
            t.left(90)
            t.forward(100)
        t.penup()
        t.goto(center_x, center_y)
        t.pendown()
        t._tracer(2)
    if keyboard.is_pressed('0'):
        t.color("#3d3f45")
