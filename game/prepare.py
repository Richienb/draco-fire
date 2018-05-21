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
