!/usr/bin/python3
# -*- coding: utf-8 -*

import RPi.GPIO as GPIO
import time
import ping3

PORT_L = 26 #red
PORT_C = 19 #yellow
PORT_R = 13 #green

GPIO.setmode(GPIO.BCM)
GPIO.setup(PORT_L, GPIO.OUT)
GPIO.setup(PORT_C, GPIO.OUT)
GPIO.setup(PORT_R, GPIO.OUT)


target_domain = "servers_name"

flag = 1
sleeptime = 30
try:
    while True:
        #p=pings.Ping()
        #res = p.ping(target_domain)
        res = ping3.ping(target_domain, timeout = 0.5, unit ='ms', ttl = 64)

        if (res > 0.5) :
            if flag == 1:
                #print("yellow")
                GPIO.output(PORT_L, GPIO.LOW) #黄信号
                GPIO.output(PORT_C, GPIO.HIGH)
                GPIO.output(PORT_R, GPIO.LOW)
                flag = 0
                time.sleep(sleeptime)

            else:
                #print("green")
                GPIO.output(PORT_L, GPIO.LOW) #青信号
                GPIO.output(PORT_C, GPIO.LOW)
                GPIO.output(PORT_R, GPIO.HIGH)
                flag = 0
                time.sleep(sleeptime)

        else:
            if flag == 1:
                #print("red")
                flag = 1
                GPIO.output(PORT_L, GPIO.LOW)
                GPIO.output(PORT_C, GPIO.LOW)
                GPIO.output(PORT_R, GPIO.LOW)
                for num in range(sleeptime):
                    GPIO.output(PORT_L, GPIO.HIGH) #赤信号
                    time.sleep(0.5)
                    GPIO.output(PORT_L, GPIO.LOW) #赤信号消灯
                    time.sleep(0.5)
            else:
                #print("yellow")
                GPIO.output(PORT_L, GPIO.LOW) #黄信号
                GPIO.output(PORT_C, GPIO.HIGH)
                GPIO.output(PORT_R, GPIO.LOW)
                flag = 1
                time.sleep(sleeptime)

except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()
