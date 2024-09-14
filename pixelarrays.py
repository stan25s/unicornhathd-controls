
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