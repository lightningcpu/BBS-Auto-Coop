import time
import cv2
import numpy as np
from PIL import ImageGrab
import pyautogui
from pynput.mouse import Listener

mk1 = 0
mk2 = 0
mk3 = 0
mk4 = 0
    
template1 = cv2.imread(r'Images\looking.png')
template2 = cv2.imread(r'Images\clear.png')
ulttemp = cv2.imread(r'Images\ult2.png')
tickplate = cv2.imread(r'Images\tickets.png')
failplate = cv2.imread(r'Images\failsafe.png')
connect = cv2.imread(r'Images\connection.png')
begin = cv2.imread(r'Images\start.png')

def temp1():
    x = True
    while x:
        screen1 = np.array(ImageGrab.grab(bbox=(0, 40, 1024, 620)))
        result = cv2.matchTemplate(screen1, template1, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        if max_val < .85:
            time.sleep(17)
            pyautogui.click(x=800, y=590)
            time.sleep(0.5)
            pyautogui.click(x=722, y=440)
            print('CLosed')
            x = False
            
            
def temp2():
    y = True
    while y:
        screen2 = np.array(ImageGrab.grab(bbox=(0, 40, 1024, 620)))
        result = cv2.matchTemplate(screen2, template2, cv2.TM_CCOEFF_NORMED)
        failsafe = cv2.matchTemplate(screen2, failplate, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        _, max_val2, _, _ = cv2.minMaxLoc(failsafe)
        if max_val >= .60:
            time.sleep(2)
            print('CLosed')
            y = False
        elif max_val2 > .75:
            time.sleep(0.8)
            pyautogui.click(x=725, y=562)
            time.sleep(1)
            pyautogui.click(x=662, y=437)
            time.sleep(2.5)
            pyautogui.click(x=711, y=582)         

def ult():
    z = True
    while z:
        screen3 = np.array(ImageGrab.grab(bbox=(0, 40, 1024, 620)))
        result = cv2.matchTemplate(screen3, ulttemp, cv2.TM_CCOEFF_NORMED)
        failsafe = cv2.matchTemplate(screen3, failplate, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        _, max_val2, _, _ = cv2.minMaxLoc(failsafe)
        if max_val > .35:
            time.sleep(8.5)
            pyautogui.click(x=968, y=402)
            time.sleep(2)
            pyautogui.click(x=968, y=402)
            time.sleep(1)
            pyautogui.click(x=968, y=402)
            print('Ult worked')
            z = False
        elif max_val2 > .70:
            time.sleep(0.8)
            pyautogui.click(x=725, y=562)
            time.sleep(1)
            pyautogui.click(x=662, y=437)
            time.sleep(2.5)
            pyautogui.click(x=711, y=582)


def tickets():
    screen4 = np.array(ImageGrab.grab(bbox=(0, 40, 1024, 620)))
    result = cv2.matchTemplate(screen4, tickplate, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)
    if max_val >= .60:
        time.sleep(1)
        print('Not enough tickets!')
        gettickets()
        start()
        time.sleep(3)
        temp1()
        time.sleep(1)
    else:
        print('Tickets good')


def checkconnect():
    a = True
    while a:
        screen5 = np.array(ImageGrab.grab(bbox=(0, 40, 1024, 620)))
        failsafe = cv2.matchTemplate(screen5, connect, cv2.TM_CCOEFF_NORMED)
        result = cv2.matchTemplate(screen5, begin, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(failsafe)
        _, max_val2, _, _ = cv2.minMaxLoc(result)
        if max_val > .55:
            time.sleep(2)
            print('Check Connect Accured!!!')
            pyautogui.click(x=662, y=437)
            time.sleep(7)
            select()
            start()
            time.sleep(7)
            temp1()
            time.sleep(1)
            tickets()
            time.sleep(1)
            checkconnect()
            a = False
        elif max_val2 >= .30:
            time.sleep(1)
            print('Connection good')
            a = False
            
            
def gettickets():
    pyautogui.click(x=516, y=436)
    time.sleep(0.5)
    pyautogui.click(x=27, y=67) #Back
    time.sleep(0.5)
    pyautogui.click(x=655, y=438) #Accept
    time.sleep(5)
    pyautogui.click(x=512, y=439) #Click ok on room close
    time.sleep(7)
    pyautogui.click(x=982, y=72) #Menu
    time.sleep(0.5)
    pyautogui.click(x=952, y=577) #Soul badge
    time.sleep(0.5)
    pyautogui.click(x=575, y=350) #Power-up quests
    time.sleep(5)
    pyautogui.click(x=300, y=280) #Select some quest
    time.sleep(3)
    pyautogui.click(x=725, y=539) #Difficulty button
    time.sleep(1.5)
    pyautogui.click(x=750, y=568) #Prepare button
    time.sleep(1.5)
    pyautogui.click(x=661, y=571) #Start quest
    time.sleep(5)
    pyautogui.click(x=750, y=568) #Buy tickets
    time.sleep(0.7)
    pyautogui.click(x=661, y=445)
    time.sleep(0.5)
    pyautogui.click(x=525, y=442)
    time.sleep(0.7)
    pyautogui.click(x=446, y=439)
    time.sleep(0.5)
    pyautogui.click(x=668, y=432)
    time.sleep(5)
    pyautogui.click(x=518, y=442)
    time.sleep(0.5)
    pyautogui.click(x=982, y=68) #Menu
    time.sleep(0.5)
    pyautogui.click(x=820, y=575) #Co-op
    time.sleep(0.5)
    pyautogui.click(x=515, y=315) #Co-op select
    time.sleep(5)
    select()
    

def select():
    scroll(m)
    pyautogui.click(x=mk1, y=mk2)
    time.sleep(0.5)
    if na == 1:
        extrascroll()
        pyautogui.click(x=mk3, y=mk4)
        time.sleep(0.5)
    else:
        pyautogui.click(x=mk3, y=mk4)
        time.sleep(0.5)


def scroll(m):
    xx = 1
    while xx <= m:
        pyautogui.click(x=325, y=535)
        time.sleep(0.7)
        pyautogui.click(x=308, y=167)
        time.sleep(0.7)
        xx += 1


def extrascroll():
    time.sleep(1)
    pyautogui.click(x=320, y=165)
    time.sleep(0.3)
    pyautogui.click(x=320, y=165)
    time.sleep(0.3)
    for i in range(5):
        pyautogui.scroll(-20)

        
def on_click(x, y, button, pressed):
    global mk1
    global mk2
    mk1 = x
    mk2 = y
    return False


def on_click2(q, r, button, pressed):
    global mk3
    global mk4
    mk3 = q
    mk4 = r
    return False

   
def start():
        pyautogui.click(x=369, y=332)
        time.sleep(0.7)
        pyautogui.click(x=682, y=442)
        time.sleep(10.5)
        pyautogui.click(x=786, y=152)
        time.sleep(0.5)
        pyautogui.click(x=660, y=560)


def end():
    pyautogui.click(x=502, y=587) #Click tap here
    time.sleep(7)
    pyautogui.click(x=512, y=558) #Close player rank reward
    time.sleep(1)
    pyautogui.click(x=506, y=585) #Tap screen
    time.sleep(6)
    pyautogui.click(x=172, y=581) #Retry button

m = int(input('How many scrollings(0-3): '))
if 0 < m <= 3:
    scroll(m)

print('Click on the quest')
with Listener(on_click=on_click) as listener:
    listener.join()

    
time.sleep(1)
na = int(input("Extrascroll? 1/yes, 0/no: "))
if na == 1:
         extrascroll()


print('Click on the difficulty')
with Listener(on_click=on_click2) as listener:
    listener.join()
    
time.sleep(1)
while True:
    start()
    time.sleep(7)
    temp1()
    time.sleep(1.2)
    tickets()
    time.sleep(1)
    checkconnect()
    time.sleep(1)
    ult()
    time.sleep(1)
    temp2()
    time.sleep(5)
    end()
    time.sleep(6)
