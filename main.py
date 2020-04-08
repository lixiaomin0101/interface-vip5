'''
# 加载测试用例
# 运行用例并生成报告
# 发送邮件通知
'''
import  unittest,os
from HTMLTestRunner import HTMLTestRunner
from common.configEmail import *

current_dir = os.path.abspath('_file_')
base_dir =os.path.dirname(current_dir)
test_dir =base_dir +'/' +'testCase'

# 加载所有测试用例
def  create_suite():
    discover = unittest.defaultTestLoader.discover(
        start_dir=test_dir,
        pattern='test*.py',
        top_level_dir = None

    )
    return discover


if __name__ == '__main__':
    suite = create_suite()
    # 运行用例并生成报告
    # 创建报告的路径和名称
    file =base_dir +  '/' + 'report'+'/'+ 'testReport.html'

    # 打开写入
    with open(file,'wb') as fp:
        # 创建htmltestrunner实例
        runner = HTMLTestRunner(
            stream=fp,
            title ='接口自动化测试报告',
            description ='报告详情'
        )
        runner.run(suite)

    # 发送邮件
    sendMail()