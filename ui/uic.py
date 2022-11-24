#!/usr/bin/python3

import subprocess
import sys




def loadUi(param):
    child = subprocess.Popen(['pyuic5', '-x', param], stdout=subprocess.PIPE)



    exec (str(child.communicate()[0], encoding='utf-8'))