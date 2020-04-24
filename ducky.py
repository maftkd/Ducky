import sys
import os
from datetime import date
from datetime import datetime
import glob

#constants
blue = "\033[1;34;34m"
cyan = "\033[1;36;36m"
white = "\033[1;37;37m"
dark_gray = "\033[1;30;30m"
red = "\033[1;31;31m"
green = "\033[1;32;32m"
yellow = "\033[1;33;33m"
purple = "\033[1;35;35m"
#change color cuz we fancy bois
os.system('color 6F')

#set up log dir
log_path = os.path.dirname(os.path.abspath(__file__))+"\\logs"
if not os.path.exists(log_path):
	os.mkdir(log_path)

#get cur log (full path) and date (for comparison) for a given date
def getLogPath(date_str):
	global cur_log, cur_date
	cur_log_path = log_path+"\\"+date_str+".duck"
	#the only time a log may  not exist is if it's the first log of the day
	if not os.path.exists(cur_log_path):
		#generate today's log file
		with open(cur_log_path, 'w') as f:
			f.write('[Summary]\n\n\n')
			f.write('[Goals]\n\n\n')
			f.write('[Misc]\n\n\n')
	cur_log = cur_log_path
	cur_date = date_str
	#print("new cur_log = "+str(cur_log))
	#print("new cur_date = "+str(cur_date))

cur_log=""
cur_date=""
getLogPath(str(date.today()))

def displayLog(log):
	head,tail = os.path.split(log)
	print(purple+tail)
	with open(log, 'r') as f:
		lines = f.readlines()			
		for line in lines:
			ANSIcolor=white
			line_raw = line.rstrip('\n')
			if line_raw == "[Summary]":
				ANSIcolor=purple
			elif line_raw == "[Goals]":
				ANSIcolor=purple
			elif line_raw == "[Misc]":
				ANSIcolor=purple
			print(ANSIcolor+line_raw)

#main loop
os.system("cls")
function="foo"
while function != "" and function != "exit" and function != "close":	
	
	#header
	displayLog(cur_log)
	function = raw_input(white+"$")	
	os.system("cls")

	#edit cur log
	if function == "log" or function == "l":		
		os.system("vim "+cur_log)

	#elif function == "read" or function == "r":
		#displayLog(cur_log)
	
	#go to prev log
	elif function == "j":
		ducks = list(filter(os.path.isfile, glob.glob(log_path + "\\*.duck")))
		ducks.sort(key=lambda x: os.path.getmtime(x), reverse=True)
		prev_found=False
		for duck in ducks:
			head,tail = os.path.split(duck)
			date = tail.split('.')[0]
			if date < cur_date:
				getLogPath(date)
				prev_found=True
				break;
		if not prev_found:
			print(red+"no previous entries")

	#go to next log
	elif function == "k":
		ducks = list(filter(os.path.isfile, glob.glob(log_path + "\\*.duck")))
		ducks.sort(key=lambda x: os.path.getmtime(x), reverse=True)
		next_found=False
		for duck in ducks:
			head,tail = os.path.split(duck)
			date = tail.split('.')[0]
			if date > cur_date:
				getLogPath(date)
				next_found=True
				break;
		if not next_found:
			print(red+"no next entries")
	
	#time display
	elif function == "t" or function == "time":
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		print(white+"Current Time is:")
		print(current_time)
	
	#date display
	elif function == "d" or function == "date":
		print(white+"Current Date is:")
		print(str(date.today()))
	else:
		print(red+"error: unkown ducky command")


#change color back
os.system('color 0f')
os.system("cls")