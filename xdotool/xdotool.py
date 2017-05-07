#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division, print_function
import subprocess, time
import numpy as np

def execCommand(command):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    p.wait()
    return p.stdout.read()

def getMousePos():
    getMouseCommand = "xdotool getmouselocation"
    res = execCommand(getMouseCommand).strip()
    res = {x.split(":",1)[0] : x.split(":",1)[1] for x in res.split(" ")}
    return res

def setMousePos(x, y):
    setMouseCommand = "xdotool mousemove {} {}".format(x, y)
    execCommand(setMouseCommand)

def moveMouse(x, y, t=3, s=100):
    # get the current mouse position
    cpos = getMousePos()
    # build vector from current pos to x, y
    cPoint = np.array([float(cpos["x"]), float(cpos["y"])])
    oPoint = np.array([x, y])
    vect = oPoint - cPoint
    # move mouse along vector
    for i in np.linspace(0, 1, s):
        setMousePos(*(cPoint + vect * i))
        time.sleep(t / s)

def click(btn=1):
    clickCommand = "xdotool click {}".format(btn)
    execCommand(clickCommand)

def type(text):
    typeCommand = "xdotool type '{}'".format(text)
    execCommand(typeCommand)

def notify(text, icon): # icon defaults, see /usr/share/icons
    typeCommand = "notify-send '{}' --icon '{}'".format(text, icon)
    execCommand(typeCommand)

def sendKey(key): # key may for example be Left, Up, Down, Right, F11
    keySendCommand = "xdotool key {}".format(key)
    execCommand(keySendCommand)

#notify("FOOBAR", "myIcon")
#type("Hello World!")
#click()
#moveMouse(100, 100, 3, 100)
#moveMouse(100, 100)
