import os
import subprocess
import time
import getpass

   
print getpass.getuser()  
def find():
	os.system("cd /")  
	os.system("cd /home")
	os.system("cd %s") % username
	


def execute():
	print ("You are about to run a malicous script")
	print ("Are you sure you want to do this")
	time.sleep(3)
	e = raw_input('Y or N')
	if e == Y:
		print("Gamming")
		find()
	elif e == y:
		print ("gamming")
		find()
	else:
		quit() 

execute()







