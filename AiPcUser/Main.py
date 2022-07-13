import pyautogui
import time
import xlrd
import pyperclip
import random

file = '1.xls'
# 打开文件
OpenXls = xlrd.open_workbook(filename=file)
# 通过索引获取表格sheet页
sheet1 = OpenXls.sheet_by_index(0)

#-----------------------
#逻辑定位

def SoloLevelSeek(sheet1,Level):
    #读取图片列表
    imgList = list(str(sheet1.row(Level)[1].value).split('-'))
    i = 0
    while i < len(imgList):
        img = pyautogui.locateCenterOnScreen(imgList[i], confidence=0.9)
        if img is not None:
            print(f"捕捉到当前游戏的进度,{Level}级第{i+1}步.{img}")

        i += 1
        if i == len(imgList)-1 and img is None:
            print(f"没有监测到游戏窗口,停止在{Level}级第{i+1}步.")

SoloLevelSeek(sheet1,1)

#鼠标点击事件
def mouseClick(img):
    clickTimes=0.5
    offsetStrength=0.25
    imgPos = pyautogui.locateCenterOnScreen(img, confidence=0.9)
    if imgPos is not None:
        size = pyautogui.locateOnScreen(img, confidence=0.9)
        offset = (int(size[2] * offsetStrength), int(size[3] * offsetStrength))
        pyautogui.click(random.randint(imgPos.x - offset[0], imgPos.x + offset[0]),
                        random.randint(imgPos.y - offset[1], imgPos.y + offset[1]),
                        clicks=clickTimes, interval=0.2,duration=0.2, button="left")
    print("定位错误")
    time.sleep(0.5)




def TotalLevelSeek(imgNumLocation):

    pass

def GameGoOn(Level):

    pass
