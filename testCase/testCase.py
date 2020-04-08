'''
功能描述
获取测试数据，完成接口测试的请求，断言结果


解析：
 1-调用- readExcel 模块，获取测试数据
 2-根据接口测试数据，进行请求
       2.1 -get请求 -get方法
       2.2 -post 请求 -post方法
 3-断言每个接口返回的结果
       3.1 -成功
       3.2 -失败

 4-写入我们Excel
'''
from common.readExcel import readExcel
import requests
import unittest,os
from ddt import  ddt,data,unpack
from  common.configHttp import configHttp
from  common.writeExcel import writeExcel
# python 编写的测试用例必须继承unittest.TestCase

@ddt
class MyTestCase(unittest.TestCase):
    # 获取测试数据
    td = readExcel()
    test_data=td.read()
    @data(*test_data)
    @unpack
    def testRun(self,id,url,desc,method,param,expect,real,status):
         # 接口地址，接口方法，接口参数，预期结果

        print('传入对的参数为：',id,url,desc,method,param,expect,real,status)
        # 调用Run方法，进行接口请求
        chttp =configHttp()
        status_code,error_code=chttp.run(id,url,desc,method,param)
        we =writeExcel()
        print(type(id),id,'-----')

        # 断言每个接口返回的结果

        if str(status_code) =='200':
            if str(error_code) == expect:
                status='Success'
                we.writeData(id,error_code,status)
                return True
            else:
                status ='Fail'
                we.writeData(id,error_code,status)
                return False
        else:
            status = 'Fail'
            we.writeData(id,error_code,status)
            return  False
if __name__ == '__main__':

    unittest.main
