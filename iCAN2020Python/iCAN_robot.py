#!/usr/bin/python
# coding=utf-8
import RPi.GPIO as GPIO
import os
import time
import threading

import sys 
import cv2 
import datetime

MOTOR11 = 19 
MOTOR12 = 26 
MOTOR21 = 20
MOTOR22 = 21 
FALL1 = 25 
HUMAN1 = 24
PIN = 11



GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN,GPIO.IN)
GPIO.setup(MOTOR11, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MOTOR12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MOTOR21, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MOTOR22, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(FALL1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(HUMAN1, GPIO.IN,pull_up_down=GPIO.PUD_UP)
 

class MyThread(threading.Thread):
	def Front():
		GPIO.output(MOTOR11, 1)
		GPIO.output(MOTOR12, 0)
		GPIO.output(MOTOR21, 0)
		GPIO.output(MOTOR22, 1)
    
	def Back():
		GPIO.output(MOTOR11, 0)
		GPIO.output(MOTOR12, 1)
		GPIO.output(MOTOR21, 1)
		GPIO.output(MOTOR22, 0)

	def RightTurn():
		GPIO.output(MOTOR11, 1)
		GPIO.output(MOTOR12, 0)
		GPIO.output(MOTOR21, 1)
		GPIO.output(MOTOR22, 0)

	def LeftTurn():
		GPIO.output(MOTOR11, 0)
		GPIO.output(MOTOR12, 1)
		GPIO.output(MOTOR21, 0)
		GPIO.output(MOTOR22, 1)

	def Stop():
		GPIO.output(MOTOR11, 1)
		GPIO.output(MOTOR12, 1)
		GPIO.output(MOTOR21, 1)
		GPIO.output(MOTOR22, 1)

	def CAM():
		now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
		cc =cv2.VideoCapture(0)
		rr, img = cc.read()
		cv2.imwrite(now + '.jpg', img)


	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		print("  === start sub thread ===")
		count   = 0 
		while True:
		time.sleep(0.1)
		val = GPIO.input(PIN)
if val == 1:
	count += 1
if count > 30: 
	os.system('/usr/local/etc/aquestalkpi/AquesTalkPi "シャットダウンします" -g 100 | aplay -D plughw:0,0 -q')
	break
elif count > 0:
                                
for i in range(300):
	time.sleep(0.1)
if HUMAN1 == 0:
	Stop()
	time.sleep(0.5)
	CAM()
	time.sleep(0.5)

elif FALL1 == 1:
	Stop()
	time.sleep(0.5)
	Back()
	time.sleep(0.5)
	RightTurn()
	time.sleep(0.4)

else:
	Front()
	
th = MyThread()
th.setDaemon(True)
th.start()

while True:
	stdent = raw_input()
	print(stdent)
	if stdent == 'q':
	break


GPIO.cleanup()
