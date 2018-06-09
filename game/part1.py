import ros
from turtle import color, begin_fill, forward, left, end_fill, done, pos

print("A Game By...")
ros.delay(3)
ros.paraspace(2)

try:
    color('red', 'yellow')
    begin_fill()
    while True:
      forward(200)
      left(170)
      if abs(pos()) < 1:
          break
    end_fill()
    done()
except TclError:
    print("No Monitor Found!")

print("shinyA Inc")
ros.delay(3)

print("And...")
ros.delay(2)

print("ROS Inc")
ros.delay(3)

print("Draco Fire")
