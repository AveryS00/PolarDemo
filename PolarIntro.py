# A script that draws circles tangentially around a circle centered on the user's click.
# Allows options to adjust the radius of the circles, recursions, and number of circles
# drawn.

# Avery Smith

#########################################################################################
#                                     Set Up                                            #
#########################################################################################

from graphics import *
import math
from random import seed, randint


MAX_WIDTH = 1200
MAX_HEIGHT = 800

seed()
win = GraphWin('Circles', width = MAX_WIDTH, height = MAX_HEIGHT)
isRunning = True

# Exit Box
exitBox = Rectangle(Point(MAX_WIDTH*20/21, 0), Point(MAX_WIDTH, MAX_HEIGHT/21))
exitBox.setFill('red')
exitBox.draw(win)

# Exit text to fill the box
exitText = Text(Point((MAX_WIDTH+MAX_WIDTH*20/21)/2, MAX_HEIGHT/41), 'Exit')
exitText.draw(win)

# Text for radius input
radText = Text(Point(MAX_WIDTH/16 + 1, MAX_HEIGHT/32), 'Radius')
radText.draw(win)

# Entry for radius input
radBox = Entry(Point(MAX_WIDTH/16, MAX_HEIGHT/16), 5)
radBox.setText('100')
radBox.draw(win)

# Recursions text
recText = Text(Point(MAX_WIDTH*3/16 + 170, MAX_HEIGHT/32), 'Number of Recursions (more than 6 can be problematic)')
recText.draw(win)

# Entry for recursions input
recBox = Entry(Point(MAX_WIDTH*3/16, MAX_HEIGHT/16), 5)
recBox.setText('3')
recBox.draw(win)

# Number of circles input
circBox = Entry(Point(MAX_WIDTH*9/16, MAX_HEIGHT/16), 5)
circBox.setText('8')
circBox.draw(win)

# Number of circles text
circText = Text(Point(MAX_WIDTH*9/16 + 75, MAX_HEIGHT/32), 'Number of Circles generated')
circText.draw(win)


#########################################################################################
#                                     Functions                                         #
#########################################################################################

# An alternative to the range function that allows for floating point types.
# Credit to https://stackoverflow.com/questions/7267226/range-for-floats
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
# circle's edge. Each row of circles will have a random color.
def recursiveCircles(num, numCirc, radi, cent, window):
  click = win.checkMouse()
  global isRunning
  if isRunning and (click == None or not pointWithin(click, exitBox.getP1(), exitBox.getP2())):
    if num > 0:
      color = randColor()
      for i in frange (0, 2*math.pi, math.pi/(numCirc/2)):
        center2 = addPoints(toCartesian(radi, i), cent)
        cir2 = Circle(center2, radi/2)
        cir2.setOutline(color)
        cir2.draw(window)
        recursiveCircles(num - 1, numCirc, radi/2, center2, window)
  else:
    isRunning = False
      

# Choose a random color from red, green, and blue.
def randColor():
  randNum = randint(1,3)
  if randNum == 1:
    return 'red'
  elif randNum == 2:
    return 'green'
  else:
    return 'blue'
  

#########################################################################################
#                                     Run                                               #
#########################################################################################

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

win.close()
