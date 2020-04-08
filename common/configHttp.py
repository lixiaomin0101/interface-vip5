

'''
功能：封装requests方法，接收用例传来的参数，进行请求，返回用例需要的数据
解析：
    get
    post
    statuscode
    real
实现逻辑：
    1-接收入参（接口测试数据）
    2-判断接口类型（方法）
        2.1-get调用get方法
        2.1-post调用post方法
    3-将接口实际返回的结果返回到testcase
        3.1-statuscode
        3.2-错误码
        3.3-……
        return a,b,c
'''
import requests,json,time,os
from common.readExcel import readExcel
class  configHttp(object):
# 属性
# 判断接口类型方法（方法）
#     get -调用get方法
#     post-调用post方法
    def run(self,id,url,name,method,param):
        if method=='get' or method=='GET':
            status_code,error_code=self.get(url,param)
            return status_code,error_code
        if method=='post' or method=='POST':
            status_code,error_code=self.post(url,param)
            return status_code,error_code
        if method=='put' or method=='PUT':
            status_code,error_code=self.put(url,param)
            return status_code,error_code

# param  --请求发送的数据
# 方法xs
    def get(self,url,param):
        # 根据请求方法调用不同的请求方式
        result =requests.get(url=url,params=param)
        print('+++++',result.text)
        status_code =result.status_code
        error_code  =result.json()['errorCode']
        return  status_code,error_code
        # print(status_code,error_code)
    def post(self,url,param):
        reslut =requests.post(url=url,params=param)
        status_code=reslut.status_code
        error_code =reslut.json()['errorCode']
        return status_code,error_code


    def put(self,url,param):
        reslut =requests.put(url=url,params=param)
        status_code=reslut.status_code
        error_code =reslut.json()['errorCode']
        return status_code,error_code
#
# ch =configHttp()
# ch.get('https://www.wanandroid.com/user/logout/json','')
# #
if __name__ == '__main__':

    ch = configHttp()
    re = readExcel()
    data = re.read()
