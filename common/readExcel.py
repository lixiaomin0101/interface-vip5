import xlrd
import os

current_dir =os.path.abspath('_file_')
base_dir = os.path.dirname(os.path.dirname(current_dir))
excle_dir =base_dir+'/'+"testDate"

class readExcel(object):
    def __init__(self):
        # 读取Excel
        self.readbook = xlrd.open_workbook(excle_dir+'/'+'data.xls')
        self.data_list=[]
    # 定义方法
    def read(self):
        # readbook = xlrd.open_workbook('/Applications/work/untitled/interfaceTestVip5/testDate/data.xls')
        # # 获取sheet下标，也就是列表对象
        sheet =self.readbook.sheet_by_index(0)
        # 获取行数
        nrow =sheet.nrows
        # 读取数据
        for  i in range(0,nrow):
            # 获取列表中第一行的值
            rowdata =sheet.row_values(i)
            self.data_list.append(rowdata)
        # 打印数据NameError: name '_file_' is not defined

        return self.data_list


if __name__ == '__main__':
    re =readExcel()
    print(re.read())