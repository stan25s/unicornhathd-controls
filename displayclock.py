import unicornhathd
import pixelarrays
from datetime import datetime

def get_time_as_pixel_list(h, m):
    h1 = pixelarrays.get_character_as_pixels(h[0])
    h2 = pixelarrays.get_character_as_pixels(h[1])
    m1 = pixelarrays.get_character_as_pixels(m[0])
    m2 = pixelarrays.get_character_as_pixels(m[1])
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
    

def update():
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