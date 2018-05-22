#!/usr/bin/python

from paver.easy import *
import paver.doctools
import os
import glob
import shutil

@task
def setup():
  sh('python setup.py -q install')
  pass

@task
def test():
  sh('nosetests --with-coverage --cover-erase --cover-branches --cover-package=file_writer,string_writer,converter,writer,lower_case_converter,upper_case_converter,stupid_remover,duplicate_remover  test')
  pass

@task
def clean():
  for pycfile in glob.glob("*/*/*.pyc"): os.remove(pycfile)
  for pycache in glob.glob("*/__pycache__"): os.removedirs(pycache)
  for pycache in glob.glob("./__pycache__"): shutil.rmtree(pycache)
  pass

@task
@needs(['setup', 'clean', 'test'])
def default():
  pass
