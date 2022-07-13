import pyautogui

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
            return [True,i]

        i += 1
        if i == len(imgList)-1 and img is None:
            print(f"没有监测到游戏窗口,停止在{Level}级第{i+1}步.")
            return [False,i]

