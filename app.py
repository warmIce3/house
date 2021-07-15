# turtle: basically lets you draw things on the screen
import turtle

# MACROS
AUTHOR = "warmIce3"
VERSION = "v.1"
SHAPE  = "turtle"

# screen
myscreen = turtle.Screen()
myscreen.bgcolor("cornflower blue")

# creating characters 
player1 = turtle.Turtle()
player1.shape(SHAPE)

def draw_base():
  """
  This is supposed to draw the square below the roof (base)
  """
  player1.seth(270)
  player1.speed(10) #0-10
  player1.seth(270)
  player1.speed(10) #0-10
  player1.color("maroon")
  player1.begin_fill()
  player1.forward(90)
  player1.left(90)
  player1.forward(90)
  player1.left(90)
  player1.forward(90)
  player1.left(90)
  player1.forward(90)
  player1.color("beige")
  player1.end_fill()

def draw_roof():  
  """
  This function is responsible for drawing the roof. Size is 90
  """
  player1.color("maroon")
  player1.begin_fill()
  player1.left(180)
  player1.forward(90)
  player1.left(120)
  player1.forward(90)
  player1.left(120)
  player1.forward(90)
  player1.color("saddle brown")
  player1.end_fill()

def draw_door():
  """
  Draws the door
  """
  player1.seth(270)
  player1.color("maroon")
  player1.forward(90)
  player1.left(90)
  player1.forward(30)
  player1.color(60, 17, 17)
  player1.begin_fill()
  player1.seth(90)
  player1.forward(45)
  player1.right(90)
  player1.forward(30)
  player1.right(90)
  player1.forward(45)
  player1.end_fill()
  player1.left(90)

def draw_dk():
  """
  Draws the doorknob
  """
  player1.forward(5)
  player1.color("yellow")
  player1.begin_fill()
  player1.seth(90)
  player1.penup()
  player1.forward(15)
  player1.circle(5)
  player1.end_fill()
  player1.penup()
  player1.goto(0, 0)
  player1.seth(270)
  player1.forward(90)
  player1.seth(180)
  player1.pendown()

def draw_ground():
  """
  draws the ground
  """
  player1.begin_fill()
  player1.color("yellow green")
  player1.forward(490)
  player1.left(90)
  player1.forward(158)
  player1.left(90)
  player1.forward(1100)
  player1.left(90)
  player1.forward(158)
  player1.left(90)
  player1.forward(610)
  player1.end_fill()
  player1.seth(90)
  
def draw_sun():
  """
  This draws the sun
  """
  player1.penup()
  player1.forward(380)
  player1.color("yellow")
  player1.pendown()
  player1.begin_fill()
  player1.circle(50)
  player1.end_fill()

player1.ht()
# drawing the base
draw_base()
# we use this function to draw the base
draw_roof()
# Function for drawing a door
draw_door()
# Function for drawing the doorknob
draw_dk()
# Function for drawing the ground
draw_ground()
#function to draw the sun
draw_sun()