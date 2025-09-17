# in command prompt, put in pip install keyboard
# Matthew Ren
# 9/15/25
# Make a turtle program
import turtle
import keyboard

t = turtle.Turtle()
turtle.bgcolor("#3d3f45")

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
        for f in range (200): 
            t.speed(100)
            t.forward(200)
            t.right(2**2)
            t.left(150)
            t.forward(100)
            f = f + 1
