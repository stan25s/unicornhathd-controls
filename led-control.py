import unicornhathd
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
# unicornhathd.rotation = 180
unicornhathd.brightness = 0.6

def get_time_as_pixel_list(h, m):
    h1 = get_character_as_pixels(h[0])
    h2 = get_character_as_pixels(h[1])
    m1 = get_character_as_pixels(m[0])
    m2 = get_character_as_pixels(m[1])
    #Convert to 2d Array
    h1a = [[h1[0], h1[1], h1[2]],
           [h1[3], h1[4], h1[5]],
           [h1[6], h1[7], h1[8]],
           [h1[9], h1[10], h1[11]],
           [h1[12], h1[13], h1[14]],
           [h1[15], h1[16], h1[17]]]
    h2a = [[h2[0], h2[1], h2[2]],
           [h2[3], h2[4], h2[5]],
           [h2[6], h2[7], h2[8]],
           [h2[9], h2[10], h2[11]],
           [h2[12], h2[13], h2[14]],
           [h2[15], h2[16], h2[17]]]
    m1a = [[m1[0], m1[1], m1[2]],
           [m1[3], m1[4], m1[5]],
           [m1[6], m1[7], m1[8]],
           [m1[9], m1[10], m1[11]],
           [m1[12], m1[13], m1[14]],
           [m1[15], m1[16], m1[17]]]
    m2a = [[m2[0], m2[1], m2[2]],
           [m2[3], m2[4], m2[5]],
           [m2[6], m2[7], m2[8]],
           [m2[9], m2[10], m2[11]],
           [m2[12], m2[13], m2[14]],
           [m2[15], m2[16], m2[17]]]
    
    row_number = 0
    mins = False
    
    for x in range(0,16):
        if x == 8:
            mins = True
        if x != 7 and x <= 13:
            for y in range(0,16):
                if x == 0:
                    unicornhathd.set_pixel(x, y, 0, 0, 0)
                else:
                    if y == 0:
                        unicornhathd.set_pixel(x, y, 0, 0, 0)
                    elif y <= 3:
                        if mins == True:
                            unicornhathd.set_pixel(x, y, m1a[x-8][y-1] * 255, m1a[x-8][y-1] * 255, m1a[x-8][y-1] * 255)
                        else:
                            unicornhathd.set_pixel(x, y, h1a[x-1][y-1] * 255, h1a[x-1][y-1] * 255, h1a[x-1][y-1] * 255)
                    elif y == 4:
                        unicornhathd.set_pixel(x, y, 0, 0, 0)
                    elif y <= 7:
                        if mins == True:
                            unicornhathd.set_pixel(x, y, m2a[x-8][y-5] * 255, m2a[x-8][y-5] * 255, m2a[x-8][y-5] * 255)
                        else:
                            unicornhathd.set_pixel(x, y, h2a[x-1][y-5] * 255, h2a[x-1][y-5] * 255, h2a[x-1][y-5] * 255)
    
def get_character_as_pixels(x):
    pixel_list = [0] * 18
    if x == '0':
        pixel_list[0] = 1
        pixel_list[1] = 1
        pixel_list[2] = 1
        pixel_list[3] = 1
        pixel_list[5] = 1
        pixel_list[6] = 1
        pixel_list[8] = 1
        pixel_list[9] = 1
        pixel_list[11] = 1
        pixel_list[12] = 1
        pixel_list[14] = 1
        pixel_list[15] = 1
        pixel_list[16] = 1
        pixel_list[17] = 1
    elif x == '1':
        pixel_list[2] = 1
        pixel_list[5] = 1
        pixel_list[8] = 1
        pixel_list[11] = 1
        pixel_list[14] = 1
        pixel_list[17] = 1
    elif x == '2':
        pixel_list[0] = 1
        pixel_list[1] = 1
        pixel_list[2] = 1
        pixel_list[3] = 1
        pixel_list[5] = 1
        pixel_list[8] = 1
        pixel_list[9] = 1
        pixel_list[10] = 1
        pixel_list[11] = 1
        pixel_list[12] = 1
        pixel_list[15] = 1
        pixel_list[16] = 1
        pixel_list[17] = 1
    elif x == '3':
        pixel_list[0] = 1
        pixel_list[1] = 1
        pixel_list[2] = 1
        pixel_list[3] = 1
        pixel_list[5] = 1
        pixel_list[8] = 1
        pixel_list[9] = 1
        pixel_list[10] = 1
        pixel_list[11] = 1
        pixel_list[14] = 1
        pixel_list[15] = 1
        pixel_list[16] = 1
        pixel_list[17] = 1
    elif x == '4':
        pixel_list[0] = 1
        pixel_list[2] = 1
        pixel_list[3] = 1
        pixel_list[5] = 1
        pixel_list[6] = 1
        pixel_list[8] = 1
        pixel_list[9] = 1
        pixel_list[10] = 1
        pixel_list[11] = 1
        pixel_list[14] = 1
        pixel_list[17] = 1
    elif x == '5':
        pixel_list[0] = 1
        pixel_list[1] = 1
        pixel_list[2] = 1
        pixel_list[3] = 1
        pixel_list[6] = 1
        pixel_list[9] = 1
        pixel_list[10] = 1
        pixel_list[11] = 1
        pixel_list[14] = 1
        pixel_list[15] = 1
        pixel_list[16] = 1
        pixel_list[17] = 1
    elif x == '6':
        pixel_list[0] = 1
        pixel_list[1] = 1
        pixel_list[2] = 1
        pixel_list[3] = 1
        pixel_list[5] = 1
        pixel_list[6] = 1
        pixel_list[9] = 1
        pixel_list[10] = 1
        pixel_list[11] = 1
        pixel_list[12] = 1
        pixel_list[14] = 1
        pixel_list[15] = 1
        pixel_list[16] = 1
        pixel_list[17] = 1
    elif x == '7':
        pixel_list[0] = 1
        pixel_list[1] = 1
        pixel_list[2] = 1
        pixel_list[3] = 1
        pixel_list[5] = 1
        pixel_list[8] = 1
        pixel_list[10] = 1
        pixel_list[13] = 1
        pixel_list[16] = 1
    elif x == '8':
        pixel_list[0] = 1
        pixel_list[1] = 1
        pixel_list[2] = 1
        pixel_list[3] = 1
        pixel_list[5] = 1
        pixel_list[6] = 1
        pixel_list[8] = 1
        pixel_list[9] = 1
        pixel_list[10] = 1
        pixel_list[11] = 1
        pixel_list[12] = 1
        pixel_list[14] = 1
        pixel_list[15] = 1
        pixel_list[16] = 1
        pixel_list[17] = 1
    else:
        pixel_list[0] = 1
        pixel_list[1] = 1
        pixel_list[2] = 1
        pixel_list[3] = 1
        pixel_list[5] = 1
        pixel_list[6] = 1
        pixel_list[8] = 1
        pixel_list[9] = 1
        pixel_list[10] = 1
        pixel_list[11] = 1
        pixel_list[14] = 1
        pixel_list[15] = 1
        pixel_list[16] = 1
        pixel_list[17] = 1
    return pixel_list

def set_date_pixels(d, m, w1):
    weekday = ""
    w = int(w1)
    if w == 0:
        weekday = "sun"
    elif w == 1:
        weekday = "mon"
    elif w == 2:
        weekday = "tue"
    elif w == 3:
        weekday = "wed"
    elif w == 4:
        weekday = "thu"
    elif w == 5:
        weekday = "fri"
    elif w == 6:
        weekday = "sat"
    else:
        weekday = "err"

    print(weekday)
    weekday_pixels = [[[0]*3]*4]*4
    weekday_pixels = get_weekday_pixels(weekday)

    for y in range (1, 12):
        for x in range (1, 5):
            if y >= 1 and y < 4:
                unicornhathd.set_pixel(x, y, 
                255 * weekday_pixels[0][x-1][y-1], 
                255 * weekday_pixels[0][x-1][y-1], 
                255 * weekday_pixels[0][x-1][y-1])
            elif y >= 5 and y < 8:
                unicornhathd.set_pixel(x, y, 
                255 * weekday_pixels[1][x-1][y-5], 
                255 * weekday_pixels[1][x-1][y-5], 
                255 * weekday_pixels[1][x-1][y-5])
            elif y >= 9:
                unicornhathd.set_pixel(x, y, 
                255 * weekday_pixels[2][x-1][y-9], 
                255 * weekday_pixels[2][x-1][y-9], 
                255 * weekday_pixels[2][x-1][y-9])
            else:
                unicornhathd.set_pixel(x, y, 0, 0, 0)

    #Then we need to get date as pixels and set these to the display
    d1 = get_character_as_pixels(d[0])
    d2 = get_character_as_pixels(d[1])
    d1a = [[d1[0], d1[1], d1[2]],
           [d1[3], d1[4], d1[5]],
           [d1[6], d1[7], d1[8]],
           [d1[9], d1[10], d1[11]],
           [d1[12], d1[13], d1[14]],
           [d1[15], d1[16], d1[17]]]
    d2a = [[d2[0], d2[1], d2[2]],
           [d2[3], d2[4], d2[5]],
           [d2[6], d2[7], d2[8]],
           [d2[9], d2[10], d2[11]],
           [d2[12], d2[13], d2[14]],
           [d2[15], d2[16], d2[17]]]

    for y in range (1, 8):
        for x in range (6, 12):
            if y >= 1 and y < 4:
                unicornhathd.set_pixel(x, y,
                255 * d1a[x-6][y-1],
                255 * d1a[x-6][y-1],
                255 * d1a[x-6][y-1])
            elif y >= 5 and y < 8:
                unicornhathd.set_pixel(x, y,
                255 * d2a[x-6][y-5],
                255 * d2a[x-6][y-5],
                255 * d2a[x-6][y-5])

    add_day_month_visualisation_pixels(d, m)

def add_day_month_visualisation_pixels(d, m):
    days_in_month = {
        "01" : 31, "02" : 29, "03" : 31,
        "04" : 30, "05" : 31, "06" : 30,
        "07" : 31, "08" : 31, "09" : 30,
        "10" : 31, "11" : 30, "12" : 31
    }

    day_int = int(d)
    month_int = int(m)

    day_counter = 1
    month_counter = 1

    for x in range (6, 8):
        for y in range (9, 15):
            if month_counter <= month_int:
                unicornhathd.set_pixel(x, y, 54, 150, 230)
            else:
                unicornhathd.set_pixel(x, y, 10, 25, 50)
            month_counter = month_counter + 1
    
    for x in range (9, 15):
        for y in range (9, 15):
            if day_counter <= day_int and day_counter <= days_in_month[m]:
                unicornhathd.set_pixel(x, y, 255, 204, 90)
            elif day_counter > day_int and day_counter <= days_in_month[m]:
                unicornhathd.set_pixel(x, y, 30, 25, 5)
            day_counter = day_counter + 1


def get_weekday_pixels(w):
    array_pixels = []
    for c in w:
        array_pixels.append(get_char_pixels(c))
    return array_pixels

def get_char_pixels(c):
    if c == 'm':
        return [[1, 1, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]]
    elif c == 'o':
        return [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]]
    elif c == 'n':
        return [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1]]
    elif c == 't':
        return [[1, 1, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0]]
    elif c == 'u':
        return [[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]]
    elif c == 'e':
        return [[1, 1, 1], [1, 1, 0], [1, 0, 0], [1, 1, 1]]
    elif c == 'w':
        return [[1, 0, 1], [1, 0, 1], [1, 1, 1], [1, 1, 1]]
    elif c == 'd':
        return [[1, 1, 0], [1, 0, 1], [1, 0, 1], [1, 1, 0]]
    elif c == 'h':
        return [[1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]]
    elif c == 'f':
        return [[1, 1, 1], [1, 0, 0], [1, 1, 0], [1, 0, 0]]
    elif c == 'r':
        return [[1, 1, 1], [1, 1, 1], [1, 1, 0], [1, 0, 1]]
    elif c == 'i':
        return [[1, 1, 1], [0, 1, 0], [0, 1, 0], [1, 1, 1]]
    elif c == 's':
        return [[1, 1, 1], [1, 0, 0], [0, 1, 1], [1, 1, 1]]
    elif c == 'a':
        return [[0, 1, 0], [1, 0, 1], [1, 1, 1], [1, 0, 1]]
    else:
        return [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]

def set_bin_time_pixels(h, m, s):
    
    hour_bin = format(h, 'b')
    print("hour: " + hour_bin)
    while len(hour_bin) < 6:
        hour_bin = '0' + hour_bin
        #hour_bin = hour_bin + '0'
        
    min_bin = format(m, 'b')
    print("min: " + min_bin)
    while len(min_bin) < 6:
        min_bin = '0' + min_bin
        #min_bin = min_bin + '0'
        
    sec_bin = format(s, 'b')
    print("sec: " + sec_bin)
    while len(sec_bin) < 6:
        sec_bin = '0' + sec_bin
        #sec_bin = sec_bin + '0'
        
    print(hour_bin + " - " + str(h))
    print(min_bin + " - " + str(m))
    print(sec_bin + " - " + str(s))
    
    index = 0
    for x in range (14, 3, -2):
        unicornhathd.set_pixel(x, 1, 55 + (200 * int(hour_bin[index])), 55 + (200 * int(hour_bin[index])), 55 + (200 * int(hour_bin[index])))
        index = index + 1
        
    index = 0
    for x in range (14, 3, -2):
        unicornhathd.set_pixel(x, 3, 55 + (200 * int(min_bin[index])), 55 + (200 * int(min_bin[index])), 55 + (200 * int(min_bin[index])))
        index = index + 1
        
    index = 0
    for x in range (14, 3, -2):
        unicornhathd.set_pixel(x, 5, 55 + (200 * int(sec_bin[index])), 55 + (200 * int(sec_bin[index])), 55 + (200 * int(sec_bin[index])))
        index = index + 1
     
#def set_bin_date_pixels(d, m, wd):
    

try:
    while True:
        
        #This loop keeps looping through the different display modes
        try:
            while mode == 'clock':
                #Get current time, convert this to arrays of pixels
                #And then set the pixels in the UHHD matrix, then show.
                now = datetime.now()
                
                if current_time != now.strftime("%H:%M"):
                    #only update the display if the time has changed since previous check
                    current_time = now.strftime("%H:%M")
                    current_hour = now.strftime("%H")
                    current_minute = now.strftime("%M")
                    #print("Current Time = ", current_time)
                    
                    unicornhathd.clear()
                    
                    get_time_as_pixel_list(current_hour, current_minute)

                current_seconds = now.strftime("%S")
                seconds_int = int(current_seconds)

                counter = 0

                if seconds != seconds_int:
                    seconds = seconds_int
                    if seconds >= 0:
                        for y in range(10, 15):
                            for x in range(2, 14):
                                if counter < seconds:
                                    #unicornhathd.set_pixel(x, y, random.randint(100,255), 0, random.randint(0,50))
                                    unicornhathd.set_pixel(x, y, 200, 0, 30)
                                counter += 1
                unicornhathd.rotation(180)
                unicornhathd.show()
        except keyboard.is_pressed("2"):
            unicornhathd.clear()
            current_time = ""
            mode = "date"
        try:
            while mode == "date":
                #Get current time, convert this to arrays of pixels
                #And then set the pixels in the UHHD matrix, then show.
                now = datetime.now()
                
                if current_date != now.strftime("%d:%m"):
                    #only update the display if the time has changed since previous check
                    current_date = now.strftime("%d:%m")
                    current_day = now.strftime("%d")
                    current_month = now.strftime("%m")
                    current_day_of_week = now.strftime("%w")
                    #print("Current Time = ", current_time)
                    
                    unicornhathd.clear()
                    
                    set_date_pixels(current_day, current_month, current_day_of_week)

                    unicornhathd.rotation(180)
                    unicornhathd.show()
                time.sleep(60)
        except keyboard.is_pressed("1"):
            unicornhathd.clear()
            mode = "clock"
            
        try:
            while mode == "binary":
                #Get current time, convert this to arrays of pixels
                #And then set the pixels in the UHHD matrix, then show.
                now = datetime.now()
                
                if current_date != now.strftime("%d:%m"):
                    #only update the display if the time has changed since previous check
                    current_date = now.strftime("%d:%m")
                    current_day = now.strftime("%d")
                    current_month = now.strftime("%m")
                    current_day_of_week = now.strftime("%w")
                    #print("Current Time = ", current_time)
                    
                    unicornhathd.clear()
                    
                    #set_bin_date_pixels(current_day, current_month, current_day_of_week)
                
                current_seconds = now.strftime("%S")
                seconds_int = int(current_seconds)
                current_time = now.strftime("%H:%M")
                current_hour = int(now.strftime("%H"))
                current_minute = int(now.strftime("%M"))
                    
                set_bin_time_pixels(current_hour, current_minute, seconds_int)
                unicornhathd.show()
                
        except keyboard.is_pressed("1"):
            unicornhathd.clear()
            mode = "clock"
except KeyboardInterrupt:
    unicornhathd.off()
