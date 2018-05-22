print("Loading Game... (Importing Modules)")
import turtle
import ros

ros.paraspace()

while True:
	print("To Continue, Solve The Captcha")
	if ros.captcha() == False:
		print("Access Denied! You Are A Bot!")
		print('', end='\n')
	else:
		break
