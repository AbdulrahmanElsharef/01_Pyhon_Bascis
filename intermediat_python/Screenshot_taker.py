import pyautogui


def screen_shot():
    screen = pyautogui.screenshot()
    screen.save(
        'J:\Abdo_BackEnd\Django_FullStack_Project\\Python_Dev\\01_Python_Basics\\new_screen.png')
    print("screen shot is done".title())


screen_shot()
