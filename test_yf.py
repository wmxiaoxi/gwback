#
# from selenium  import  webdriver
# driver=webdriver.Chrome()
from test_data.news_check_data import *

# #不可改变的是数值，元组，字符串
# from math import ceil
#
# a,b=8,5
# print(a+b,a-b,a*b,a/b,a//b,a%b)
# str='rubbo'
# print(str*2)
# print(str+"test")
# print('rubbo\n111')
# print(r'rubbo\n111')
#
#
#
# list=['abcd','786','runobb',70.2]
# tinylist=[123,'runoob']
# print(list)
# print(list[0])
# print(list[1:3])
# print(list[2:])
# print(tinylist*2)
# print(list+tinylist)
#
#
# tuple=('abcd',786,2.23)
# tinytuple=(123,'rubnoo')
# print(tuple)
# print(tuple[0])
# print(tuple[2:])
# print(tinytuple*2)
# print(tuple+tinytuple)
# tup1=()
# tup2=(20,)
#
#
# #集合
# student={'tom','jim',',mary','Jack','jim'}
# print(student)#输出集合，自动去掉重复的
# #set可以进行集合运算
# a=set('abracadabra')
# b=set('alacazam')
# print(a)
# print(a-b)#a和b的差集
# print(a|b)#a和b的并集
# print(a&b)#a和b的交集
# print(a^b)#a和b不同时存在的元素
#
# dict={}
# dict['one']="1-菜鸟教程"
# dict[2]="2-菜鸟工具"
# tindydict={'name':'rubnoo',"code":1}
# print(dict['one'])
# print(dict[2])
# print(tindydict)
# print(tindydict.keys())#输出所有键
# print(tindydict.values())#输出所有值
#
# #注释
# '''
# print(22222222222)
# '''
#
#
# #算术运算符
# 1+2   #相加
# 1-2   #相减
# 1*2   #相乘
# 1/2   #相除
# 1//2  #取整数
# 1%2   #取余数
# 1**2  #返回x的y次幂
#
# #比较运算符
# 1==1
# 1!=2
# 2>1
# 1<2
# a>=b
# b<=a
#
# #简单的赋值运算
# c=a+b
# c+=a #就等于c=c+a
# c-=a#就等于c=c-a
# c*=a#就等于c=c*a
# c/=a#就等于c=c/a
# c//=a#就等于c=c//a
# c%=a#就等于c=c%a
# c*=a#就等于c=c**a
#
# #逻辑运算符 and  or  not
#
# ceil(4.1)#返回上入的整数
# abs()
#
#
#
import codecs
import os
#coding:utf-8
# fp=open(r"C:\Users\wmxia\Desktop\常用网址.txt",'r')
# lines=fp.readlines()
# user=[]
# for data in lines:
#     user.append(data)
# print(user)




# #浏览器的操作

# driver.refresh()
# driver.forward()
# driver.back()
# driver.set_window_size(500,980)
# driver.maximize_window()
# driver.minimize_window()
# driver.get_screenshot_as_png()
# driver.get_screenshot_as_file("d:\\test\\1.jpg")
# driver.close()#关闭部分窗口
# driver.quit()#关闭进程，所有窗口

# #元素定位
# driver.find_element_by_id()
# driver.find_element_by_name()
# driver.find_element_by_class_name()
# driver.find_element_by_xpath()
# driver.find_element_by_css_selector()
# driver.find_element_tag_name()
# driver.find_element_by_link_text()
# driver.find_element_by_partial_link_text()

# #xpath定位,没有id name xpath可以用其他属性来定位
# driver.find_element_by_xpath("//*[@id='kw']") #xpath id name  class 定位
# driver.find_element_by_xpath("//input[@id='kw']")#标签定位
# driver.find_element_by_xpath("//form[@id='form']/span/input")#层级定位,先定位到爸爸再往下定位；先定位到爷爷 在往下定位；
# driver.find_element_by_xpath("//select[@id='nr'/option[1]]")#一个父亲生的，多胞胎兄弟，则索引定位,这里的索引从1开始
# driver.find_element_by_xpath("//*[@id='kw'&@autocomplete='off']")#xpath逻辑运算
# driver.find_element_by_xpath("//*[contains(text(),'hao123')]")#xpath模糊匹配，比如hao123
# driver.find_element_by_xpath("//*[starts-with(@id,'ueditor_')]")
# driver.find_element_by_xpath("//*[ends-with(@id,'ueditor_')]")
# driver.find_element_by_xpath("//*[contains(@id,'kw')]")
# driver.find_element_by_xpath("//*[matchs(text(),'hao123')]")
#
# #css标签 id  class定位
# driver.find_element_by_css_selector('#kw')##号表示id; .表示class;css直接用标签名称，无任何标示符
# driver.find_element_by_css_selector('.s_ipt')
# driver.find_element_by_css_selector('input')
# #css其他定位
# driver.find_element_by_css_selector("[name='wd']")
# #css可以通过标签和属性组合来定位
# driver.find_element_by_css_selector("input#kw")
# #层级定位
# driver.find_element_by_css_selector("form#form>span>input")
# #索引定位
# driver.find_element_by_css_selector('select#nr>option:nth child=(1)')
# #逻辑运算定位
# driver.find_element_by_css_selector("input[id='kw'][name='wd']")

# ##sbumit()一般用于模拟回车键
# from selenium.webdriver.common.keys import Keys
# driver.find_element_by_css_selector("input[id='kw'][name='wd']").send_keys(Keys.ENTER)
# driver.find_element_by_css_selector("input[id='kw'][name='wd']").send_keys(Keys.CONTROL,'c')
# driver.find_element_by_css_selector("input[id='kw'][name='wd']").send_keys(Keys.TAB)

#鼠标悬停


# #checkbox
# checkboxs=driver.find_elements_by_xpath(".//*[@type='checkbox']")
# for i in checkboxs:
#     i.click()
#
# #是否被选中
# r=driver.find_element_by_id("kw").is_selected()

# #js处理日历的只读属性
# js='document.getElementById('').removeAttribute("reaaonly")'
# driver.execute_script(js)


#
# #table定位
# driver.find_element_by_xpath('.//*[@id="table”/tr[2]/td[1]]')


#多窗口处理
#处理文件上传
#处理浏览器弹框
#获取元素属性
#爬取原页码
#判断title
# title_is()
# title_contains()
#判断元素
#绕过验证码
#cookie相关操作
#显式等待
#冒泡排序
#判断弹框存在
#判断文本
#js解决click失效
#异常后截图
#读取excel
#unnitest断言
#unittest装饰器
#unittest生成报告
#jekines




#
# import random
# a=random.randint(0,9)
# print (a)

# import re
# driver.get("http://www.cnblogs.com/yoyoketang/")
# page=driver.page_source
# print(page)
# url_list=re.findall("href=\"(.*?)\"",page,re.S)
# url_all=[]
# for url in url_list:
#     if "http" in url:
#         print(url)
#         url_all.append(url)
#     print(url_all)
#     driver.get_screenshot_as_file("d:\\test\123.jpg")


# #去除readonly的属性并传值
# js="document.getElementById('').removeAttribute('readonly');"
# driver.execute_script(js)
# js_value='doucument.getElementById().value="2016-12-25"'


from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.common.action_chains import ActionChains
import requests
import re
import time
from bs4 import BeautifulSoup
# driver.get('http://www.cnblogs.com/yoyoketang')r
# title=e.title_contains('上海-悠悠 ')
# print  (title(driver))
# driver.get("https://home.cnblogs.com/u/yoyoketang")
# cookies=driver.get_cookies()
# print(cookies)
# driver.quit()
#ActionChains.double_click().perform()    #双击



import json

# #接口测试
# par={"keywords":"yoyoketang"}
# r=requests.get('http://www.cnblogs.com/yoyoketang',params=par)
# print(r.url)
# plyload={"yoyo":"hello world","python":"22629743"}
# data_json=json.dumps(plyload)
# r=requests.post('http://httpbin.org/post',json=data_json)
# print(r.text)
# print(r.url)

import time
import datetime
# localtime=time.localtime()
# print(localtime)
# localtime1=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())   #time.strptime()
# print(type(localtime1))


# import requests
#
# h={
#     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#     "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
#     "Accept-Encoding":"gzip,deflate"
# }
# data={"name":"hello",
#       "age":23}
# r=json.dumps(data)
# r1=requests.post("http://www.baidu.com",r,headers=h)
#
# print(r1.text)



# #冒泡方法1
# #coding:utf-8
# li=[1, 3, 10, 9, 21, 35, 4, 6]
# n=[7,6,5,4,3,2,1]
# for i in n:
#     for j in range(i):
#         if li[j]>li[j+1]:
#             li[j],li[j+1]=li[j+1],li[j]
# print(li)
#
#
#
# #冒泡方法2
# list=[1, 3, 10, 9, 21, 35, 4, 6]
# list.sort()
# print(list)





# a=[-9,2,3,-4,5,6,6,1]
#
# def f(x):
#     return abs(x)
# a.sort(key=f)
# print(a)

# #按字符长度倒叙排列
# b=["hello","helloworld","he","hao","good"]
# b.sort(key=lambda x:len(x),reverse=True)
# print(b)


# #list里面是元组 倒数第一个的排序
# c=[("d",9),("b",7),("c",8)]
# c.sort(key=lambda x:x[1])
# print(c)

# #list里面是字典，按照字典的值进行排序
# d = [{"a": 9}, {"b": 2}, {"d":5}]
# d.sort(key=lambda x:list(x.values()))
# print(d)
#

##sorted的用法,直接调用
# #1.字典
# f = {"a": 9, "b": 2, "d": 5}
# g = sorted(f.items(), key=lambda x: x[1])
# print(g)


# #2.字符串
# c="hello world"
# c1=sorted(c)
# print(c1)




##3.列表里元组
# list=[("a", 9), ("b", 2), ("d", 5)]
# list1=sorted(list,key=lambda x:x[1])
# print(list1)



# # coding:utf-8
# import threading
# import time
#
# def chi():
#     print("%s 吃着火锅开始：" % time.ctime())
#     time.sleep(1)
#     print("%s 吃着火锅：涮羊肉" % time.ctime())
#     time.sleep(1)
#     print("%s 吃着火锅：涮牛肉" % time.ctime())
#     time.sleep(1)
#     print("%s 吃着火锅：贡丸" % time.ctime())
#     time.sleep(1)
#     print("%s 吃火锅结束！" % time.ctime())
# def ting():
#     print("%s 哼着小曲1！" % time.ctime())
#     time.sleep(2)
#     print("%s 哼着小曲2！" % time.ctime())
#     time.sleep(2)
#     print("%s 哼着小曲3！" % time.ctime())
#     time.sleep(2)
#     print("%s 哼着小曲4！" % time.ctime())
#     time.sleep(2)
#     print("%s 哼着小曲5！" % time.ctime())
#     time.sleep(2)
#
# # 创建线程数组
# threads=[]
# # 创建线程t1，并添加到线程数组
# t1=threading.Thread(target=chi())
# threads.append(t1)
#
# # 创建线程t2，并添加到线程数组
#
# t2=threading.Thread(target=ting())
# threads.append(t2)
# if __name__ == '__main__':
#     # 启动线程
#     for i in threads:
#         i.start()





##os用法
import os
# #获取当前路径，返回字符串
# print(os.getcwd())
# #返回绝对路径，path为.为当前目录，..为上一层目录;
# print(os.path.abspath('..'))
# #返回path中的文件夹部分，结果不包含'\'就是把最后\右边节点去掉
# print(os.dirname(os.getcwd()))
# #和dirname类似，只是basename去除\左边的节点
# print(os.basename(os.getcwd()))
# #列出当前目录下的路径
# print(os.listdir(os.getcwd()))
#判断地址是否存在
#print(os.path.exists(r'C:\Users\wmxia\Desktop\11.txt'))
#创建目录文件
# os.makedirs(r'C:\Users\wmxia\Desktop\111.txt')
#删除文件,文件夹是空的才会被删除否则报错
# os.rmdir(r'C:\Users\wmxia\Desktop\111.txt')
#删除指定的文件
#os.remove()
#判断path是否是文件
# os.path.isfile(path)
#os.path.isdir(path)


#有+表示读写模式，有b表示二进制相关文件，r是读（文件不存在，则报错，w是写（如果文件不存在，创建新文件，这里创建新文件的规则是：如果path不包含路径，文件不存在，则创建；如果path包含路径，路径存在，文件不存在，创建文件；如果path包含路径，路径不存在，则报错），a是在文件后面写
#f = open(r'C:\Users\wmxia\Desktop\11\text.txt', 'w')
#f = open(u'C:/Users/wmxia/Desktop/11/text.txt', 'w')

##open用法 readline readlines
# f=open(r"C:\Users\wmxia\Desktop\常用网址.txt")
# print(f.read())




# driver.maximize_window()
# driver.minimize_window()
# driver.refresh()
# driver.forward()
# driver.back()
# driver.set_window_size()
# driver.find_element_by_xpath().clear()
# driver.find_element_by_xpath().send_keys()
# driver.find_element_by_xpath().click()
# driver.find_element_by_xpath().submit()
# ActionChains.double_click()
# ActionChains.move_to_element().perform()
# ActionChains.drag_and_drop().perform()
#
#
# from selenium.webdriver.common.keys import Keys
# driver.find_element_by_xpath().send_keys(Keys.CONTROL,'a')
# driver.find_element_by_xpath().send_keys(Keys.BACKSPACE)
# driver.find_element_by_xpath().send_keys(Keys.TAB)



#九九乘法表
# i=1
# j=1
# while i <=9:
#     while j <=9:
#         if i-j>=0:
#
#             print(str(i)+'*'+str(j))
#         j=j+1
#     else:
#         i=i+1
#         j=1

#
# #举个例子
# driver.get("http://192.168.17.214/#/login")
# driver.minimize_window()
# target=driver.find_element_by_xpath("//input[@name='username']")
# ActionChains(driver).double_click(target).perform()
# target.send_keys('admin')
#
# driver.find_element_by_xpath("//*[@name='password']").send_keys('admin123')
# e=driver.find_element_by_xpath("//*[@role='checkbox']").is_selected()
# print(e)
# if e==False:
#     driver.find_element_by_xpath("//*[@role='checkbox']").click()
#     time.sleep(10)
#     driver.find_element('xpath','//*[@id="login"]/form/div[3]/div/button').click()
#     assert driver.title=='瀚叶数据'
#     time.sleep(10)
#     #handle = driver.current_window_handle
#     #print(handle)
#     table = driver.find_element_by_xpath("//*[@id=\"app\"]/div/section/section/main/div/div[4]/div[4]/div[3]")
#     tr_ele=table.find_elements_by_tag_name("tr")
#     list=[]
#     for i in tr_ele:
#         list.append(i.text)
#





# text1 = ele.find_elements("tag name","tr")
# list = []
# for i in text1:
#     list.append(i.text)
#     newlist = list[0].split('\n')
# print(newlist[0])



# #去重
# a=[1,2,3,4,5,6,7,8,9,9]
# new=[]
# for i in a:
#      if  i  not in new:
#          new.append(i)
# print

# # 按从小到大排序
# # 按从大大小排序
# # 去除重复数字
# c=[1, 3, 6, 9, 7, 3, 4, 6]
# c.sort()
# print(c)
# new=[]
# for i in c:
#     if i not in new:
#         new.append(i)
# print(new)


# c=[1, 3, 6, 9, 7, 3, 4, 6]
# c.sort(reverse=True)
# print(c)
# new=[]
# for i in c:
#     if i not in new:
#         new.append(i)
# print(new)
#


#
# #求1000以内的完全数有哪些？
#
# a=[]
# for i in range(1,1000):
#     s = 0
#     for j in range(1,i-1):
#         if i%j==0:
#             s=s+j
#     if s==i:
#         print(i)
#         a.append(i)
#
# print("1000以内完全数：%s" % a)




# # coding:utf-8
# import pytest
# # 函数式
#
# def setup_module():
#      print("所有用例打开前会执行一次")
#
# def teardown_module():
#     print("所有用例结束后会执行一次")
#
# def setup_function():
#     print("setup_function：每个用例开始前都会执行")
#
# def teardown_function():
#     print("teardown_function：每个用例结束后都会执行")
#
# def test_one():
#     print("正在执行----test_one")
#     x = "this"
#     assert 'h' in x
#
#
# def test_two():
#     print("正在执行----test_two")
#     a = "hello"
#     b = "hello world"
#     assert a in b
#
#
# #-s打印过程，-q只显示结果不显示过程
# if __name__ == "__main__":
#     pytest.main(["-s", "test_yf.py"])



# import  pytest
# @pytest.fixture(autouse=True)
# def test():
#      a=1
#      b=2
#      c=a+b
#      return c
#
# def test_02(test):
#     d=1
#     f=test
#     p=d+f
#     print(p)
# #@pytest.mark.usefixtures('test')
# class TestCase:
#    def test_03(self,test):
#         print(test)
#
# if  __name__=="__main__":
#
#     pytest.main(["-s",'test_yf.py'])




#
# import  pytest
# @pytest.fixture(scope='module', autouse=True)
# def test1():
#     print('\n开始执行module')
# @pytest.fixture(scope='class', autouse=True)
# def test2():
#     print('\n开始执行class')
# @pytest.fixture(scope='function', autouse=True)
# def test3():
#     print('\n开始执行function')
#
#
# def test_a():
#     print('---用例a执行---')
# def test_d():
#     print('---用例d执行---')
#
# class TestCase:
#     def test_b(self):
#         print('---用例b执行---')
#     def test_c(self):
#         print('---用例c执行---')
#
# if __name__=="__main__":    pytest.main(["-s","test_yf.py"])







import unittest
from unittest import mock

#
# class SubClass(object):
#     def add(self, a, b):
#         """两个数相加"""
#         pass
#
# class TestSub(unittest.TestCase):
#
#     def test_sub(self):
#         sub = SubClass()  # 初始化被测函数类实例
#         sub.add = mock.Mock(return_value=10)  # mock add方法 返回10
#         result = sub.add(5, 9)  # 调用被测函数
#         self.assertEqual(result, 10)  # 断言实际结果和预期结果
#
#
# if __name__ == '__main__':
#     unittest.main()






import requests
import unittest
from unittest import mock
# class SubClass(unittest.TestCase):
#     def cal(self):
#         url = 'http://47.98.63.78:8087/valuation/calculateNodes'
#         h = {"Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Encoding": "gzip, deflate",
#              "Content-Type": "application/json"}
#         f = {
#             "tree": '{"root":{"data":{"id":"c0wu48ui6bk0","created":1582795330733,"text":"中心主题"},"children":[{"data":{"id":"c0wu4b0ltr40","created":1582795335455,"text":"分支测试1","resource":[""],"weight":"0.2","uselessWeight":false,"reject":false},"children":[{"data":{"id":"c0wu4lif1800","created":1582795358300,"text":"分支1.1","value":"30","resource":["30"],"obtainValueType":"direct","weight":"1","uselessWeight":false,"reject":false},"children":[]}]},{"data":{"id":"c0wu4c7e9bk0","created":1582795338043,"text":"分支测试2","value":"1","resource":["1"],"obtainValueType":"direct","weight":"0.3","uselessWeight":false,"reject":false},"children":[]},{"data":{"id":"c0wu4de1dk00","created":1582795340621,"text":"分支测试3","value":"1","resource":["1"],"obtainValueType":"direct","weight":"0.05","uselessWeight":false,"reject":false},"children":[]},{"data":{"id":"c0wu4ekpv200","created":1582795343202,"text":"分支测试4","value":"1","resource":["1"],"obtainValueType":"direct","weight":"0.3","uselessWeight":false,"reject":false},"children":[]},{"data":{"id":"c0wu4frevg00","created":1582795345783,"text":"分支测试5","value":"10","resource":["10"],"obtainValueType":"direct","weight":"0.15","uselessWeight":false,"reject":false},"children":[]}]},"template":"default","theme":"fresh-blue","version":"1.4.33"}'
#         }
#         r = requests.post(url, data=f, headers=h)
#         return r
#
#     def test_01(self):
#         sub = SubClass()
#         tt = open(r"C:\Users\wmxia\Desktop\1.txt")
#         line = tt.readline()
#         sub.cal = mock.Mock(return_value=line)
#         result = sub.cal(5, 9)
#         self.assertEqual(result, line)
# if __name__ == '__main__':
#     unittest.main()


#  # coding:utf-8
# import requests
#
# # 先打开登录首页，获取部分cookie
# url = "https://passport.cnblogs.com/user/signin"
# headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
#            }  # get方法其它加个ser-Agent就可以了
#
#
# s=requests.session()
# r = s.get(url, headers=headers,verify=False)
# print(s.cookies)
#
# # 添加登录需要的两个cookie
#
# c=requests.cookies.RequestsCookieJar()
# c.set('.CNBlogsCookie', '3DFAD87DC6436A134ED44EF82E31E6C9A0F2E9933413845B326BA35D5375698CB8752D8FB94439B451E51B9E8F2A28454428AC761CFBC3FF1AA11AF6E9EB2F86DDCF17E5D28C6C0D310E27925181A3F4935608F771697A0FB5898011BF709ECAD80CC9A2')  # 填上面抓包内容
# c.set('.Cnblogs.AspNetCore.Cookies','CfDJ8Nf-Z6tqUPlNrwu2nvfTJEgcdoH2qW0gmIrvkTeGQDjatyDgdBiMRtchgBNTnz2sbvWBouKBntTKlgcpoUtVOLV5zNUFJI6eeSAZYE3x7Z4z2nTtaHCMpkT57_hTM6LOORtm-6Uu_0OEnan2jkKt8a4_MxJsqFtWSuUFso7NKHUzCao1Jxsvq9fLV3IZkdLTRdNbLJdNtXmGtdQw9lNvTCFeQqd67f_gHt7D-wCxtI7eAQwbhIys1BbATVW_JZVE4WDtXoBmuBUtK0rvMKTeXb-wuI1s62CLHJP5Hm7fb71XZE6imDI0h9JIsLcphe9n02SH4_FyP-sdn7vgMbRe_SCCjUr4l7OY0DY9UctDMJSlOGuKb1SHMf889_4oshOAxvkD_SyVbTEDKyBG0tkmMCGwylrKB_dIhdSfkl5NRgoh0JtoAkIWaEaVD4Z3KVolYUiYAPdavQTAJdULd6KbuvtUICaGnaDb_orSa-ouLHB2aF8_WOCjj0tA7WDq6vFUHkOeZJBTzPY3-AC5fLVcpd8LHs_l8qjknBtMcfnAHo8HRW3eiFBJjwohKLFagbJxsQ')  # 填上面抓包内容
# s.cookies.update(c)
# print (s.cookies)








