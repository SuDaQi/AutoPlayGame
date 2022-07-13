import ClickEvent
import xlrd
import LevelSeek



file = '1.xls'
# 打开文件
OpenXls = xlrd.open_workbook(filename=file)
# 通过索引获取表格sheet页
sheet1 = OpenXls.sheet_by_index(0)





if LevelSeek.SoloLevelSeek(sheet1,1) is True:

    imgList = list(str(sheet1.row(1)[1].value).split('-'))
    ClickEvent.mouseClick(imgList[0])





def GameGoOn(Level):

    pass
