from graphics import *
import math
from random import seed, randint

# Set up

# Define window width and height
# IMPORTANT, X AND Y COORDINATES START FROM THE TOP LEFT OF THE SCREEN
MAX_WIDTH = 1200
MAX_HEIGHT = 800

seed()
win = GraphWin('Circles', width = MAX_WIDTH, height = MAX_HEIGHT)
isRunning = True

# Create an exit rectangle
exitBox = Rectangle(Point(MAX_WIDTH*20/21, 0), Point(MAX_WIDTH, MAX_HEIGHT/21))
exitBox.setFill('red')
exitBox.draw(win)

# Exit text
exitText = Text(Point((MAX_WIDTH+MAX_WIDTH*20/21)/2, MAX_HEIGHT/41), 'Exit')
exitText.draw(win)

# Create text for the radius box
radText = Text(Point(MAX_WIDTH/16 + 1, MAX_HEIGHT/32), 'Radius')
radText.draw(win)

# Create a box to allow for radius change
radBox = Entry(Point(MAX_WIDTH/16, MAX_HEIGHT/16), 5)
radBox.setText('100')
radBox.draw(win)

# Create text for the recursions box
recText = Text(Point(MAX_WIDTH*3/16 + 170, MAX_HEIGHT/32), 'Number of Recursions (more than 6 can be problematic)')
recText.draw(win)

# Create a box to allow number of recursions to change
recBox = Entry(Point(MAX_WIDTH*3/16, MAX_HEIGHT/16), 5)
recBox.setText('3')
recBox.draw(win)

# Choose how many extra circles per circle
circBox = Entry(Point(MAX_WIDTH*9/16, MAX_HEIGHT/16), 5)
circBox.setText('8')
circBox.draw(win)

# Number of Circles text
circText = Text(Point(MAX_WIDTH*9/16 + 75, MAX_HEIGHT/32), 'Number of Circles generated')
circText.draw(win)


# Functions

# An alternative to the range function that allows for floating point types.
# Range only accepts integers but we want to work with pi.
def frange(x, y, jump):
  while x < y:
    yield x
    x += jump


# Converts Polar coordinates to cartesian
def toCartesian(radius, theta):
  x = radius * math.cos(theta)
  y = radius * math.sin(theta)
  return Point(x,y)

# Converts cartesian coordinates to polar,is not currently used
# but is included anyways for demonstration purposes.
def toPolar(x, y):
  r = math.sqrt(math.exp(x,2)+math.exp(y,2))
  theta = math.atan(x/y)
  return Point(r,theta)

# Adds together two coordinates
def addPoints(p1, p2):
  return Point(p1.x + p2.x, p1.y + p2.y)

# Checks whether the first point is within the other two points
def pointWithin(p1, p2, p3):
  if p1.x > p2.x and p1.x < p3.x \
     and p1.y > p2.y and p1.y < p3.y:
    return True
  else:
    return False

# Recursively creates smaller circles with centers along the current
# circle's edge. Each row of circles will have a random color, but you can
# change it so each circle is a random color by moving the color variable
# into the for loop.
def recursiveCircles(num, numCirc, radi, cent, window):
  if num > 0:
    color = randColor()
    # The number of circles generated is 2 times the number that pi
    # is being divided by.
    for i in frange (0, 2*math.pi, math.pi/(numCirc/2)):
      center2 = addPoints(toCartesian(radi, i), cent)
      cir2 = Circle(center2, radi/2)
      cir2.setOutline(color)
      cir2.draw(window)
      recursiveCircles(num - 1, numCirc, radi/2, center2, window)

# Choose a random color from red, green, and blue.
def randColor():
  randNum = randint(1,3)
  if randNum == 1:
    return 'red'
  elif randNum == 2:
    return 'green'
  else:
    return 'blue'
  

# Main/Run

while isRunning:
  center = win.getMouse()
  if center != None and pointWithin(center, exitBox.getP1(), exitBox.getP2()):
    win.close()
    isRunning = False
  elif center != None:
    # Create the first circle
    circ = Circle(center, int(radBox.getText()))
    circ.setOutline(randColor())
    circ.draw(win)

    # Create the rest
    recursiveCircles(int(recBox.getText()) - 1, int(circBox.getText()), int(radBox.getText()), center, win)
