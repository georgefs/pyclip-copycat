#!/usr/bin/env python

from distutils.core import setup
import platform


def build_params():
    params = {
      'name':'pyclip-copycat',
      'version':'0.2',
      'description':'easily interact with clipboard from Python fork from pyclip',
      'author':'george.li',
      'author_email':'goblin.george@gmail.com',
      'url':'https://github.com/georgefs/pyclip',
      'py_modules':['clipboard'],
	  'license':'MIT',
    }

    #add windows paste command
    if platform.system() == 'Windows':
        params['scripts'] = ['paste.exe']

    return params

setup(
    **build_params()
)
