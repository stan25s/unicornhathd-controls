import unicornhathd
import displayclock
import displaycal
import displaybin
import keyboard
import time
#import math
#import colorsys
#import random

from datetime import datetime
from array import *

print("""Unicorn HAT HD: Control Module

This program runs several different display modes
based on a numerical input.

Press Ctrl+C to Exit!

""")
mode = 'clock'

current_time = ""
current_date = ""
seconds = 0
unicornhathd.brightness = 0.6
     
#def set_bin_date_pixels(d, m, wd):
    
# TODO - set the time or date within the while loops for each mode in this file and then pass the value to the relevant update() function.
    

try:
    while True:
        
        #This loop keeps looping through the different display modes
        try:
            while mode == "clock":
                #Get current time, convert this to arrays of pixels
                #And then set the pixels in the UHHD matrix, then show.
                displayclock.update()

                time.sleep(0.1) #No point updating any more frequently than 10 times per second.

        except keyboard.is_pressed("1"): #When key 1 is pressed, change to next mode.
            current_time = ""
            current_date = ""
            mode = "date"

        try:
            while mode == "date":
                #Get current date, convert day, month and weekday into matrix of pixels
                #And then set the pixels in the UHHD matrix, then show.
                displaycal.update()

                time.sleep(60) #No point updating date as frequently as we would time, only update every 1 minute.

        except keyboard.is_pressed("1"):
            unicornhathd.clear()
            current_time = ""
            current_date = ""
            mode = "binary"
            
        try:
            while mode == "binary":
                #Get current time, convert this to arrays of pixels
                #And then set the pixels in the UHHD matrix, then show.
                displaybin.update()

                time.sleep(0.1) #No point updating any more frequently than 10 times per second.
                
        except keyboard.is_pressed("1"):
            unicornhathd.clear()
            mode = "clock"

except KeyboardInterrupt:
    unicornhathd.off()
