print("Loading Game... (Importing Modules And Upgrading Pip Modules)")
import turtle
import ros
try:
	ros.pipupdate()
except:
	pass

ros.paraspace()

print("To Continue, Solve The Captcha")

if ros.captcha() == False:
	print("Access Denied! You Are A Bot!")
	ros.exitexecution()
	
ros.delay(2)
ros.paraspace(3)

print("A Game By...")
ros.delay(3)
ros.paraspace(2)

print("Shards Inc")
ros.delay(3)

print("And...")
ros.delay(2)

print("ROS Inc")
ros.delay(3)
