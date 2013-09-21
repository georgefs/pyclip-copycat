import subprocess
import csv
import os

import platform

SYSTEM = platform.system()

COMMAND_MAPPING = {
    'Linux': {"PASTE_CMD": ['xclip', '-o', '-selection', 'clipboard'], 'COPY_CMD': ['xclip', '-selection', 'clipboard']},
    'Darwin': {"PASTE_CMD": ['pbpaste'], 'COPY_CMD': ['pbcopy']},
    'Windows': {"PASTE_CMD": ['paste'], 'COPY_CMD': ['clip']},
}

PASTE_CMD = COMMAND_MAPPING.get(SYSTEM).get('PASTE_CMD')
COPY_CMD = COMMAND_MAPPING.get(SYSTEM).get('COPY_CMD')


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
