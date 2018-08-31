"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Ricardo Hernandez .
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg

window = rg.TurtleWindow()
cool_turtle = rg.SimpleTurtle('turtle')
cool_turtle.pen = rg.Pen('red', 2)
cool_turtle.speed = 1000

size = 200

for k in range(40):

    cool_turtle.draw_square(size)
    cool_turtle.pen_up()
    cool_turtle.right(20)
    cool_turtle.forward (30)
    cool_turtle.left (30)
    cool_turtle.pen_down()
    size= size - 2



circle_turtle = rg.SimpleTurtle('arrow')
circle_turtle.pen = rg.Pen ('dark gray', 2)
circle_turtle.pen_up()
circle_turtle.left(90)
circle_turtle.forward(50)
circle_turtle.left(90)
circle_turtle.forward(100)


circle_turtle.speed = 30

size= 100

circle_turtle.pen_down()

for k in range (20):

    circle_turtle.draw_regular_polygon(10, size)
    size = size - 5


window.close_on_mouse_click()