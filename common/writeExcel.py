"""
功能描述：
    实现将接口返回的实际结果和用例执行状态写入excel
解析：
    1-定义写入类（导入包）
    2-打开目标excel
    3-定位目标行
    4-写入数据
    5-关闭，保存
"""



# 1-定义写入类（导入包）
from common.configHttp import configHttp
from  xlutils.copy import copy
# 加载所有的测试用例
import os,xlrd
import xlwt
excel_dir =os.path.dirname(os.path.dirname(os.path.abspath('_file_')))+'/'+'testDate'+'/'+'data.xls'
print(excel_dir)
class writeExcel(object):

    # 属性
    def __init__(self):

        # 2-打开目标excel
        self.weekbook=xlrd.open_workbook(excel_dir)
        # 3-定位目标行
        self.wb=copy(self.weekbook)
        self.ws=self.wb.get_sheet(0)

    # 方法
    def writeData(self,id,real,status):

        # 4-写入数据
        self.ws.write(int(id),5,real)
        self.ws.write(int(id),6,status)


        # 5-关闭，保存
        self.wb.save(excel_dir)





if __name__ == '__main__':
    we =writeExcel()
    we.writeData(1,'001','200')

















