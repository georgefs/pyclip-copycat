import subprocess
import csv
import os

OS=os.uname()[0]

if OS=='Linux':
	PASTE_CMD = ['xclip', '-o', '-selection', 'clipboard']
	COPY_CMD = ['xclip', '-selection', 'clipboard']
elif OS=='Darwin':
	PASTE_CMD = ['pbpaste']
	COPY_CMD = ['pbcopy']

def paste(selection=None):
	pipe = subprocess.Popen(PASTE_CMD, stdout=subprocess.PIPE)
	outdata, errdata = pipe.communicate()
	return outdata

def copy(text):
	pipe = subprocess.Popen(COPY_CMD, stdin=subprocess.PIPE)
	pipe.communicate(text)

def paste_table():
	text = paste()
	data = list(csv.reader(text.split('\n'), delimiter='\t'))
	return data
