import ros
from turtle import *

print("A Game By...")
ros.delay(3)
ros.paraspace(2)

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

print("shinyA Inc")
ros.delay(3)

print("And...")
ros.delay(2)

print("ROS Inc")
ros.delay(3)
