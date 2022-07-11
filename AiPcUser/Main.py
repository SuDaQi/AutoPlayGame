import pyautogui
import time
import xlrd
import pyperclip
import random

#鼠标点击事件
def mouseClick(img):
    clickTimes=0.5
    offsetStrength=0.25
    location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
    if location is not None:
        size = pyautogui.locateOnScreen(img, confidence=0.9)
        offset = (int(size[2] * offsetStrength), int(size[3] * offsetStrength))
        pyautogui.click(random.randint(location.x - offset[0], location.x + offset[0]),
                        random.randint(location.y - offset[1], location.y + offset[1]), clicks=clickTimes, interval=0.2,
                        duration=0.2, button="left")
    print("未找到匹配图片,0.1秒后重试")
    time.sleep(0.5)


#遍历图片----------------
img=('111.jpg-222.jpg-333.jpg')
imgList=list(str(img).split('-'))
i=0
while i<len(imgList):
    mouseClick(img[i])
    print(i)
    i+=1
#-----------------------

