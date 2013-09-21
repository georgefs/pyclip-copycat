#!/usr/bin/env python

from distutils.core import setup
import platform


def build_params():
    params = {
      'name':'pyclip',
      'version':'0.2',
      'description':'easily interact with clipboard from Python',
      'author':'Zhehao Mao',
      'author_email':'zhehao.mao@gmail.com',
      'url':'https://github.com/zhemao/pyclip',
      'py_modules':['clipboard'],
	  'license':'MIT',
    }

    #add windows paste command
    if platform.system() == 'Windows':
        params['scripts'] = ['paste.exe']

setup(
    **build_params()
)
