# @Author ：黄贝尔
# @Time ：2021/5/7__11:24
# #coding:utf-8
import os
import time
# print(os.path.dirname(__file__))
parentDirPath = os.path.dirname(os.path.dirname(__file__))

elementLocationPath = os.path.join(parentDirPath, u'config\config.ini')

Chromepath=os.path.join(parentDirPath, u'chromedriver.exe')

#NBBKZIBDBVDTURJG    TG笔记本
auth_code = 'LXHRNCHDCWUYAQGG'#邮箱授权码
#配置用例excel路径
excelpath=os.path.join(parentDirPath, u'data\\TUMI_CN.xlsx')
#excelpath=os.path.join(parentDirPath, u'data\\TUMI_HK.xlsx')
#报告路径
reportpath=os.path.join(parentDirPath, u'report\\{}Test_report.html'.format(time.strftime('%Y-%m-%d')))
#日志路径
logpath=os.path.join(parentDirPath, u'config\\log')


if __name__ == '__main__':
    print(Chromepath)
    print(elementLocationPath)
    print(parentDirPath)
    print(reportpath)
    print(logpath)
