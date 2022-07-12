import pyautogui
import time
import xlrd
import pyperclip
import random

file = '1.xls'
# 打开文件
wb = xlrd.open_workbook(filename=file)
# 通过索引获取表格sheet页
sheet1 = wb.sheet_by_index(0)
imgList = str(sheet1.row(1)[1].value).split('-')
a = pyautogui.locateCenterOnScreen(imgList[1], confidence=0.9)
print(a)


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


#遍历图片并定位----------------
<<<<<<< HEAD
flie = '1.xls'
steel = xlrd.open_workbook(filename=flie).sheet_by_index(0)

img=('111.jpg-222.jpg-333.jpg')
imgList=list(str(img).split('-'))
a= pyautogui.locateCenterOnScreen(imgList[1], confidence=0.9)
print(a)
=======
img=('111.jpg-222.jpg-333.jpg')
imgList=list(str(img).split('-'))
#a = pyautogui.locateCenterOnScreen(r'C:\Users\ycwb0484\Desktop\waterRPA\', confidence=0.9)
#print(a)
>>>>>>> d07ff3595798310f4bbcdb3f935a621dae497b9e
def TotalLevelSeek(imgList):
    i=0
    while i<len(imgList):
        img = pyautogui.locateCenterOnScreen(imgList[i], confidence=0.9)
        if img is not True:
            return True
        i+=1
        return False
#-----------------------
#逻辑定位
def TotalLevelSeek(imgNumTotal):
    i=0
    Leve=0
    while i<imgNumTotal+1:
        imgPos=pyautogui.locateCenterOnScreen(imgList,confidence=0.9)
        if imgPos is not None:
            Leve=1
            print(f"当前游戏的进度,{i},{Leve}.")
            break
        i+=1
        if i==imgNumTotal:
            print(f"没有监测到游戏窗口,{i},{Leve}.")

def LocationLevelSeek(imgNumLocation):

    pass

def GameGoOn(Level):

    pass


