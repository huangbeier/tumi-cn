# @Author ：黄贝尔
# @Time ：2021/5/7__14:08
# #coding:utf-8
from config.config import auth_code,excelpath
from action.eleAction import *
from utils.send_mail import SendMail
from utils.exceltools import Excel_tools
from utils.logg import Loggings
log=Loggings()
ex=Excel_tools()
#在这里替换需要读取的表格路径，替换完毕后直接执行此方法,去config文件里面中修改excelpath的值
ex.read_work_book(excelpath)

def test_run():
    try:
        ex.read_work_sheet('测试用例')
        #不需要发的测试结果在表格内将序号注释
        row_nums=ex.get_max_rows()
        mail = SendMail('smtp.163.com')
        send_address = "beier0917@163.com"
        send_password = auth_code
        #receive_address = ['sai.song@tuogo.com.cn','beier.huang@tuogo.com.cn','jiale.chen@tuogo.com.cn','yi.zhang@tuogo.com.cn','feng.wang@tuogo.com.cn','hz.liu@tuogo.com.cn','cerci.zhang@tuogo.com.cn']
        receive_address = ['beier.huang@tuogo.com.cn']
        title = "测试报告"
        for i in range(2,row_nums+1):
            #不要动,EXCEL模板格式也别动
            ex.read_work_sheet('测试用例')
            info=ex.get_specific_data(i,5)
            if info=='y':
                case_step_page=ex.get_specific_data(i,4)
                ex.read_work_sheet(case_step_page)
                step_nums=ex.get_max_rows()
                log.debug(f'执行{case_step_page}用例')
                for j in range(2, step_nums + 1):

                    case =ex.get_row_data(j)
                    case_id=case[0]
                    case_step=case[1]
                    case_keyword=case[2]
                    case_ele_type=case[3]
                    case_ele_value=case[4]
                    case_value=case[5]
                    expression=''

                    #根据需求拼接表达式
                    if 'assert_b_' in case_keyword:
                        expression=case_keyword+'('+str(i)+',"'+case_value+'")'
                        log.info(expression)
                    elif 'assert_ele' in case_keyword:
                        if isinstance(case_value,int):
                            expression = case_keyword + '("' + str(i)+'","'+ case_ele_type + '","' + case_ele_value + "',"+str(case_value)+")"
                        elif "'" in case_ele_value and '"' in case_value :
                            expression = case_keyword + '(' + str(i) + ',"' + case_ele_type + '","' + case_ele_value + '",' + "'" + case_value + "')"
                        elif "'" in case_ele_value or "'" in case_value :
                            expression = case_keyword +'(' + str(i)+',"' + case_ele_type + '","' + case_ele_value + '",'+'"' + case_value + '")'
                        else:
                            expression = case_keyword + '(' + str(i) + ',"' + case_ele_type + '","' + case_ele_value + '",' + "'" + case_value + "')"
                        log.info(expression)
                    elif case_ele_type is None and case_ele_value is None and case_value:
                        if isinstance(case_value,int):
                            expression=case_keyword+'('+str(case_value)+')'
                        else:
                            expression = case_keyword + '("' + case_value + '")'
                        log.info(expression)
                    elif case_ele_type is None and case_ele_value is None and case_value is None:
                        expression=case_keyword+'()'
                        log.info(expression)
                    elif case_ele_type and case_ele_value and case_value is None:
                        expression=case_keyword+'("'+case_ele_type+'","'+case_ele_value+'")'
                        log.info(expression)
                    elif case_ele_type and case_ele_value and case_value :
                        if isinstance(case_value, int):
                            expression = case_keyword + '("' + case_ele_type + '","' + case_ele_value + '",'+str(case_value)+')'
                        else:
                            expression = case_keyword + '("' + case_ele_type + '","' + case_ele_value + '","' + case_value + '")'
                        log.info(expression)
                    try:
                        eval(expression)
                    except Exception as  e:
                        log.error(e)

        content = mail.get_content()
        #需要发送邮件的话解除注释
        mail.send_mail(send_address, send_password, receive_address, title, content)
    except Exception as e:
        #raise e
        print(e)


if __name__ == '__main__':
    test_run()

