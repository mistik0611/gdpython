import turtle
import time
import random

# Icon color selection
try:
    cubeColor = input("Select a color: ")
except ValueError:
    print("Invalid color, please try again") # Doesn't work for some reason
# Setting up the game screen
gameScreen = turtle.Screen()
gameScreen.title("Geometry Dash in Python Project")
gameScreen.screensize(800,600)
gameScreen.bgcolor("dodgerblue")
gameScreen.tracer(0)
turtle.penup()
turtle.goto(-400,-50)
turtle.pendown()
turtle.goto(400, -50)
gameOver = False
# Creating the player icon
cube = turtle.Turtle()
cube.shape("square")
cube.shapesize(2)
cube.color(cubeColor)
cube.penup()
cube.goto(-200, -29)
# Creating the deadly spikes
spike = turtle.Turtle()
spike.shape("triangle")
spike.shapesize(2)
spike.color("black")
spike.right(30)
spike.penup()
spike.goto(100,-38)
startTime = time.time()
# Jumping and gravity variables
jumpPower = 10
gravity = -0.4
cubeSpeed = 0
groundHeight = -29
onAir = False
# Jumping function
def jump():
    global cubeSpeed, onAir
    if not onAir: # Can only jump if touching ground
        cubeSpeed = jumpPower
        onAir = True
# Key bindings
gameScreen.listen()
gameScreen.onkeypress(jump, "Up")
# Game loop
while not gameOver:
    
    # Spike movement
    spike.setx(spike.xcor() - 2.5)
    if spike.xcor() < -400:
        spike.hideturtle()
        spike.goto(random.randint(0, 400), -38)
        spike.showturtle()
    # Cube movement
    cubeSpeed += gravity # Add gravity to speed
    if onAir:
        cube.sety(cube.ycor() + cubeSpeed)
    else:
        cube.sety(groundHeight)
    # Collision with ground
    if cube.ycor() <= groundHeight:
        cube.sety(groundHeight)
        cubeSpeed = 0
        onAir = False
    # Collision detection
    if cube.distance(spike) < 20:
        gameOver = True
        endTime = time.time()
        gameTime = endTime - startTime
        # Game over screen
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(0, 0)
        turtle.write(f"Game Over!\nTime: {gameTime:.2f} seconds", align="center", font=("Arial", 24, "bold"))
        # Exit key binding, only works after game over
        if gameOver == True:
            turtle.onkeypress(exit, "Escape")
    gameScreen.update() # Manually update the screen
    time.sleep(0.01) # Slow down the game

gameScreen.mainloop()