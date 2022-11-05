import schedule
import time
import pyautogui

def screen_shot():
    ''' function for take screen shot evry 15 seconds and save it'''
    screen = pyautogui.screenshot()
    screen.save('J:\Abdo_BackEnd\Django_FullStack_Project\\Python_Dev\\01_Python_Basics\\screen.png')
    print("screen shot is done....".title())

schedule.every(10).seconds.do(screen_shot)
while True:
    schedule.run_pending()
    time.sleep(1) # wait one minute 
    
# Screen Shot Is Done
# Screen Shot Is Done
# Screen Shot Is Done