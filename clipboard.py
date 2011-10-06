import subprocess
import csv

def paste():
	pipe = subprocess.Popen(['xclip', '-o'], stdout=subprocess.PIPE)
	outdata, errdata = pipe.communicate()
	return outdata

def copy(text):
	pipe = subprocess.Popen(['xclip', '-selection', 'CLIPBOARD'], 
			stdin=subprocess.PIPE)
	pipe.communicate(text)

def paste_table():
	text = paste()
	data = list(csv.reader(text.split('\n'), delimiter='\t'))
	return data
