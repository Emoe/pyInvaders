import turtle
import os 
import math

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

# Title-Screen
titleScrenn ="""
--- PyInvaders ---
"""
title = turtle.Turtle()
title.speed(0)
title.color("blue")
title.penup()
title.setposition(-175,280)
title.pendown()
title.hideturtle()
title.write(titleScrenn,font=("Arial", 32, "bold"))

# Points
gamepoints = 0
points = turtle.Turtle()
points.speed(0)
points.color("blue")
points.penup()
points.setposition(200,-350)
points.pendown()
points.hideturtle()
points.write("Points: " + str(gamepoints), font=("Arial", 16, "normal"))

# Game Over
gameover = turtle.Turtle()
gameover.speed(0)
gameover.color("red")
gameover.penup()
gameover.setposition(-300,-350)
gameover.pendown()
gameover.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.color("white")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15

# Create Invaders
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200,250)

enemyspeed = 2
enemydrop = 20

# create Weapon
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20

# ready - hidden and can be fired
# fired - bullet is fired
bulletstate="ready"

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

def fire_bullet():
	global bulletstate 
	if bulletstate == "ready":
		bullet.setposition(player.xcor(),player.ycor()+10)
		bullet.showturtle()
		bulletstate = "fired"

def isCollision(t1,t2):
	distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2) + math.pow(t1.ycor() - t2.ycor(),2))
	if distance <= 15:
		return True
	else:
		return False


turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")


# Main game Loop
while True:
	# Move the Enemy
	enemy.setx(enemy.xcor()+enemyspeed)

	# Move Enemy back 
	if enemy.xcor()+enemyspeed > 280:
		enemyspeed *= -1
		enemy.sety(enemy.ycor() - enemydrop)
	
	if enemy.xcor()+enemyspeed < -280:
		enemyspeed *= -1
		enemy.sety(enemy.ycor() - enemydrop)

	# Move the bullet
	if bulletstate == "fired":
		bullet.sety(bullet.ycor() + bulletspeed)

	# Border Checking for Bullet
	if bullet.ycor()+bulletspeed > 275:
		bullet.hideturtle()
		bulletstate = "ready"

	if isCollision(bullet,enemy):
		bullet.hideturtle()
		bullet.setposition(0,-400)
		bulletstate= "ready"
		enemy.setposition(-200,250)
		gamepoints += 1
		points.clear()
		points.write("Points: " + str(gamepoints), font=("Arial", 16, "normal"))
		

	if isCollision(enemy,player):
		player.hideturtle()
		gameover.write("Game Over", font=("Arial", 16, "normal"))


