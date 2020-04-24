import sys
import os
from datetime import date

#set up log dir
log_path = os.path.dirname(os.path.abspath(__file__))+"\\logs"
if not os.path.exists(log_path):
	os.mkdir(log_path)

function="foo"
while function != "":
	os.system("cls")
	print("Welcome to ducky")
	function = raw_input("$")
	if function == "log":
		#check if first log for today		
		cur_log_path = log_path+"\\"+str(date.today())+".duck"
		if not os.path.exists(cur_log_path):
			#generate today's log file
			with open(cur_log_path, 'w') as f:
				f.write('[Summary]\n\n\n')
				f.write('[Goals]\n\n\n')
				f.write('[Misc]\n\n\n')
		#open log with vim
		os.system("vim "+cur_log_path)


	print("user call function: "+function)