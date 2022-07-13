import ClickEvent
import xlrd
import LevelSeek


file = '1.xls'
# 打开文件
OpenXls = xlrd.open_workbook(filename=file)
# 通过索引获取表格sheet页
sheet1 = OpenXls.sheet_by_index(0)


a=LevelSeek.SoloLevelSeek(sheet1,1)
if a[0] is True:
    imgList = list(str(sheet1.row(1)[1].value).split('-'))
    ClickEvent.mouseClick(imgList[a[1]])





def GameGoOn(Level):

    pass
