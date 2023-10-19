# -*- coding: utf-8 -*-

import pyautogui as pAuto
import time


## Confirm want the program to run
# Confirm User Input
permission_given = True
check_1 = pAuto.prompt('This program will take temporary control of your computer. If you are ok with this, please enter \'Yes\' into the dialog box.')


# Check permission
try:
    permission_given = check_1.lower() == 'yes'
except:
    permission_given = False


# Make Sure permission is given
message = 'Are you sure?'
confirmations = 2
for i in range(confirmations):
    # Check if user wants to break
    if not permission_given:
        break;
    
    # Set up message for loop
    loop_title = message[0:7] + ' really'*i + message[7:]
    loop_buttons = ['Yes'+'!'*i, 'No :(']
    
    # Check permission
    check_loop = pAuto.confirm(title = loop_title, buttons = loop_buttons)
    permission_given = check_loop == loop_buttons[0]


# Send off
if permission_given:
    pAuto.prompt('Enter your social security number to continue.')
    pAuto.alert('Just kidding!')
    sendoff_title = 'Running after this dialog box is complete. Please do not click or type until the program is finished and ensure that CAPSLOCK is turned off.'
else:
    sendoff_title = 'Canceling...'

pAuto.alert(sendoff_title)
    

## Open Video if permission given
if permission_given:
    
    # Move Mouse to center of the screen to prevent accidental canceling
    screen_size = pAuto.size()
    screen_center = (screen_size[0]/2, screen_size[1]/2)
    pAuto.moveTo(screen_center)

    # This function opens windows searcher
    pAuto.hotkey("win")
    time.sleep(0.1)

    # This opens microsoft edge
    pAuto.write('microsoft edge')
    time.sleep(0.5)
    pAuto.press("enter")
    time.sleep(1)

    # This opens and plays a video link
    pAuto.write('https://drive.google.com/file/d/1rLZbV7TljoCdiJi14i-m29NW-17nYK9T/view?usp=share_link')
    pAuto.press("enter")
    time.sleep(4)
    pAuto.press("space")

