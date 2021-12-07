# @Author ：黄贝尔
# @Time ：2021/5/7__11:21
# #coding:utf-8
import traceback

from selenium.webdriver import ActionChains

from utils.exceltools import Excel_tools
from selenium import webdriver
from config.config import Chromepath, excelpath
from utils.logg import Loggings
import time
from utils.find_element import find_element, find_elements

log=Loggings()
driver=None
#实例化excel
ex = Excel_tools()
#读取excel路径
ex.read_work_book(excelpath)
#读取excel内表格
ex.read_work_sheet('测试用例')
#打开浏览器，用的是chrome浏览器测试，chrome驱动要和chrome大版本对应
#http://npm.taobao.org/mirrors/chromedriver/       chrome驱动下载地址，下载好后，在原路径直接替换
def open_browser(driver_name,*args):
    global driver
    if driver_name.lower()=='chrome':
        driver=webdriver.Chrome(Chromepath)
    else:
        log.error('找不到浏览器驱动\r\n' + traceback.format_exc())
        print('找不到浏览器驱动')
#打开网页
def get_url(url,*args):
    try:
        driver.get(url)
    except Exception as e:
        log.error(traceback.format_exc())
        print(e)

#找到元素，然后鼠标移动到该元素上点击
def move_click(ele_type,ele_vaule,*args):
    try:
        a=find_element(driver,ele_type,ele_vaule)
        ActionChains(driver).move_to_element(a).click().perform()  # 鼠标悬停到XX元素并且点击
    except Exception as e:
        log.error(traceback.format_exc())
        print(e)

#鼠标悬停到元素上
def action(ele_type,ele_vaule,*args):
    try:
        ActionChains(driver).move_to_element(find_element(driver, ele_type, ele_vaule)).perform()  # 鼠标悬停到XX元素
    except Exception as e:
        log.error(traceback.format_exc())
        print(e)

#网页最大化
def max_window():
    try:
        driver.maximize_window()
    except Exception as e:
        log.error(traceback.format_exc())
        print(e)

#强制睡眠
def sleep(seconds,*args):
    time.sleep(seconds)

#切换到iframe中
def switch_frame(ele_type,ele_vaule,*args):
    try:
        i_frame=find_element(driver,ele_type,ele_vaule)
        driver.switch_to.frame(i_frame)
    except Exception as e:
        log.error(traceback.format_exc())
        print(e)

#输入框内输入值
def input_content(ele_type,ele_vaule,values,*args):
    try:
        find_element(driver, ele_type, ele_vaule).send_keys(values)
    except Exception as e:
        log.error(traceback.format_exc())
        print(e)

#刷新页面
def refresh():
    try:
        driver.refresh()
    except Exception as e:
        log.error(traceback.format_exc())
        print(e)

#清除输入框内容
def clear(ele_type,ele_vaule,*args):
    try:
        find_element(driver,ele_type,ele_vaule).clear()
    except Exception as e:
        log.error(traceback.format_exc())
        print(e)

#点击
def click(ele_type,ele_vaule,*args):
    try:
        find_element(driver, ele_type, ele_vaule).click()
    except Exception as e:
        log.error(traceback.format_exc())
        print(e)

#断言网页标题
def assert_b_title(row,values,*args):
    try:
        assert values in driver.title
        if ex.get_specific_data(row, 6) != 'fail':
            ex.write_specific_data(row, 6, 'pass')
    except Exception as e:
        ex.write_specific_data(row, 6, 'fail')
        log.error(f'第{str(row)}行用例断言错误\r\n'+traceback.format_exc())
        print(e)

#
def input_subject(ele_type,ele_vaule,values,*args):
    try:
        a,b=ele_vaule.split(',')
        find_elements(driver,ele_type,a)[int(b)].send_keys(values)
    except Exception as e:
        log.error(traceback.format_exc())
        print(e)

#切换到默认页，用来从ifarame中退出
def switch_default(*args):
    try:
        driver.switch_to.default_content()
    except Exception as e:
        log.error(traceback.format_exc())
        print(e)

#切换到最新页
def switch_to_window(*args):
    try:
        driver.switch_to.window(driver.window_handles[-1])
    except Exception as e:
        log.error(traceback.format_exc())
        print(e)

#切换到倒数第二页
def switch_tos_window(*args):
    try:
        driver.switch_to.window(driver.window_handles[-2])
    except Exception as e:
        log.error(traceback.format_exc())
        print(e)

#切换到第一个窗口
def switch_to_default_window(*args):
    try:
        driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        log.error(traceback.format_exc())
        print(e)

#断言网页源码
def assert_b_pagesource(row,values,*args):
    try:
        assert values in driver.page_source
        if ex.get_specific_data(row, 6) != 'fail':
            ex.write_specific_data(row, 6, 'pass')
    except Exception as e:
        ex.write_specific_data(row, 6, 'fail')
        log.error(f'第{str(row)}行用例断言错误\r\n'+traceback.format_exc())
        print(e)

#断言URL
def assert_b_url(row,values,*args):
    try:
        print(driver.current_url)
        assert values in driver.current_url
        if ex.get_specific_data(row, 6) != 'fail':
            ex.write_specific_data(row, 6, 'pass')
    except Exception as e:
        ex.write_specific_data(row, 6, 'fail')
        log.error(f'第{str(row)}行用例断言错误\r\n' + traceback.format_exc())
        print(e)

#断言元素
def assert_ele(row,ele_type,ele_vaule,values,*args):
    try:
        #print(find_element(driver,ele_type,ele_vaule).text)
        assert values == find_element(driver,ele_type,ele_vaule).text
        if ex.get_specific_data(row, 6) != 'fail':
            ex.write_specific_data(row, 6, 'pass')
    except Exception as e:
        ex.write_specific_data(row, 6, 'fail')
        log.error(f'第{str(row)}行用例断言错误\r\n' + traceback.format_exc())
        print(e)


def roll_to_element(values): #向下滚动X像素
    driver.execute_script(f'window.scrollBy(0,{values})')

#回退
def back():
    driver.back()

#退出浏览器
def close_browser():
    driver.quit()


if __name__ == '__main__':
    input_subject('class name','nui-ipt-input,2','cctester')




