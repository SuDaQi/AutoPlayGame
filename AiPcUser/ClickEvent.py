import pyautogui
import random




#鼠标点击事件
def mouseClick(img):
    clickTimes=2
    offsetStrength=0.25
    imgPos = pyautogui.locateCenterOnScreen(img, confidence=0.9)
    size = pyautogui.locateOnScreen(img, confidence=0.9)
    offset = (int(size[2] * offsetStrength), int(size[3] * offsetStrength))
    pyautogui.click(random.randint(imgPos.x - offset[0], imgPos.x + offset[0]),
                    random.randint(imgPos.y - offset[1], imgPos.y + offset[1]),
                    clicks=clickTimes, interval=0.2,duration=0.2, button="left")
    print('这步完成')
