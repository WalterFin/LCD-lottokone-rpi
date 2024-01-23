#!/bin/bash
import I2C_LCD_driver
from time import *
from random import randint

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("arvotaan numerot", 1)

rivi = []
while len(rivi) < 7:
    mylcd.lcd_display_string("arvotaan numerot:", 1)
    uusi = randint(1, 40)
    if uusi not in rivi:
        rivi.append(uusi)
        uusi2 = str(uusi)
        if uusi < 10:
            uusi2 = " " + str(uusi)
        mylcd.lcd_display_string(uusi2, 2)
        sleep(1)

#jarjestaa lotto rivin
jarjestetty = sorted(rivi)

jrsrivi = ""
for a in jarjestetty:
    jrsrivi = jrsrivi + str(a) + " "
mylcd.lcd_display_string("lottorivi:", 3)
mylcd.lcd_display_string(jrsrivi, 4)

print(rivi)
print(jarjestetty)