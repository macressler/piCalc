#!/usr/bin/python

import keypad as GPIO_Keypad

import time

try:  
    keypad = GPIO_Keypad.keypad(columnCount = 7)
    arrows = GPIO_Keypad.keypad(columnCount = 2)
    # Loop while waiting for a keypress
    var = 1
    while var == 1:
        digit = keypad.getKey()
        #arrows = keypad.getKey()
        if digit != None:
            print digit
        #if arrows != None:
            #print arrows
        
        if digit != None:
            time.sleep(1)
  
except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    print "\n", counter # print value of counter
    GPIO_Keypad.cleanup()  
  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print "Other error or exception occurred!"  
  
finally:  
    GPIO_Keypad.cleanup() # this ensures a clean exit  
