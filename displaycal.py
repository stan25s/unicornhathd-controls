import unicornhathd
import pixelarrays
from datetime import datetime

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
    d1 = pixelarrays.get_character_as_pixels(d[0])
    d2 = pixelarrays.get_character_as_pixels(d[1])
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

def update(current_date): 
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