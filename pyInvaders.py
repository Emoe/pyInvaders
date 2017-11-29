import turtle
import os 

window = turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders")

# Draw Border around Playfield

border = turtle.Turtle()
border.speed(0)
border.color("blue")
border.penup()
border.setposition(-300,-300)
border.pendown()
for side in range(4):
	border.fd(600)
	border.lt(90)
border.hideturtle()

# Create player turtle

player = turtle.Turtle()
player.color("white")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15

def move_left():
	if player.xcor() - playerspeed < -280:
		player.setx(-280)
	else:
		player.setx(player.xcor() - playerspeed)

def move_right():
	if player.xcor() + playerspeed > 280:
		player.setx(280)
	else:
		player.setx(player.xcor() + playerspeed)


turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")

delay = raw_input("Press Enter to finish")
