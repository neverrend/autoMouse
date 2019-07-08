#!/usr/bin/env python3
import pyautogui
import time
import sys

# Main of the program
def main():
    
    print('#############################################')
    print('## This program lets you automate mouse    ##')
    print('## clicks for things like refreshing pages ##')
    print('## still in progess and things todo.       ##')
    print('#############################################')

    # Gets locations and wait time for run function
    location, wait = opt()

    # pro tip right here
    print('\nPress CTRL-C to end.\n')
    
    # Clicky function
    run(location, wait)

# Unused atm, prints minutes and seconds from clock on single line
def timer():
    print(str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec),'\r',
    sys.stdout.flush())

# Clicky function
def run(location, wait):
    click = 0
    while True:
        try:
            #timer()
            # Makes the mouse click @ location
            pyautogui.click(location)
           
            click += 1
            
            # Prints # of clicks on 1 line
            #sys.stdout.write('\rClick #{}'.format(click))
            print('\rClick #%d' % click, end='')
            sys.stdout.flush()
            # Time till next click
            # TODO Display countdown untill next click
            time.sleep(int(wait))
    
        # Clean exit on CTRL - C
        except KeyboardInterrupt:
            try:
                pause = input('\nClick Automation paused. Press Enter to Continue, and CTRL-C to exit.')
                continue
            except KeyboardInterrupt:
                print('\nDone.\n')
                return 0

def opt():
    
    print('')
    ans = input('Do you want to capture your mouse location?(Y\\n): ')
    
    if ans.lower() == 'y':
       
        # Proccess of capturing mouse position and wait time for run function
        while True:

            # Waits for period of time and then captures the mouse position
            wait = input('Enter seconds to wait before capture: ')
            time.sleep(int(wait))
            location = mousePos()
            
            print('\nYour mouse location was: %s \n' % str(location))
            
            # Confirmation of the position
            ans = input('Is this the location you want to automate?(Y\\n): ')
            if ans.lower() == 'y':
                wait = input('What is the interval between clicks?(sec): ')

                # Returns location and interval time between clicks
                return location, wait
            # Do over
            else:
                ans = input('Capture again?(Y\\n): ')
                print('\n')
                if ans.lower() == 'y':
                    continue
                else:
                    leave()
    else:
        leave()

# Function for mouse position
def mousePos():
    mouseLoc = pyautogui.position()
    return mouseLoc

# Quit function
def leave():
    print('Good bye!')
    exit()

# Calls Main func
if __name__ == '__main__':
    main()
