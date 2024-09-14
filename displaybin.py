import unicornhathd
from datetime import datetime

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

def update(current_time, seconds):
    now = datetime.now()
                
    if current_time != now.strftime("%H:%M") & seconds != now.strftime("%S"): #only update the display if the time has changed since the previous check
        #Note that this is still updating the minute and hour every second, if I could separate out Hour, Min, Sec, then only the relevant pixels would need to be updated.
        unicornhathd.clear()
                
        current_seconds = now.strftime("%S")
        seconds_int = int(current_seconds)
        current_time = now.strftime("%H:%M")
        current_hour = int(now.strftime("%H"))
        current_minute = int(now.strftime("%M"))
                    
        set_bin_time_pixels(current_hour, current_minute, seconds_int)
        unicornhathd.show()