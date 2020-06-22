from framework.login_action import  *
from test_data.news_check_data import  *
from  common_fuc.my import *
from common_fuc.pageobj.news_obj import *




#查询函数
def check(value,loc1,loc2):
    #login(username[0], password[0])  #如果使用run.all，连登录test全部执行，这边的函数隐掉，如果分开执行此处要加上

    newmethod.sleep(4)
    newmethod.send_keys(value,loc1,loc2)


#选择状态得下拉列表
def findele(*loc):
    newmethod.click("xpath","//*[@id=\"app\"]/div/section/section/main/div/div[4]/div[3]/div/input")
    newmethod.sleep(4)
    newmethod.click(*loc)



#点击查询按钮
def click_checkbtn(*loc):
    newmethod.click(*loc)


# 点击重置按钮
def click_clearbtn(*loc):
    newmethod.click(*loc)


#获取页面数据条数
def rowcount(*loc):
    newmethod.move(*loc)
    pagename=newmethod.find_element(*loc).get_attribute("outerText")
    pagename=pagename.split("共 ")[1]
    count=int(pagename.split(" 条")[0])
    return count

#获取数据库数据符合条件元组
def dbrow(selectname):
    newsql=ssql('192.168.17.214',3306,'wangmin','cndsdis','official_website')
    newmethod.sleep(5)
    dbcount=newsql.select_data(selectname)
    return dbcount

#获取查询出页面的第一页行内容，取第一条内容与数据库字段比较
def nametext(sql):
    ele=newmethod.find_element(tabele_ele[0], tabele_ele[1])
    text1 = ele.find_elements("tag name","tr")
    list = []
    for i in text1:
        list.append(i.text)
    newlist = list[0].split('\n')
    global newtuple,titlecondb
    newtuple = (newlist[0], datetime.datetime.strptime(newlist[1], "%Y-%m-%d %H:%M:%S"),newlist[2], newlist[3])
    titlecondb = dbrow(sql)


def nametext1():
    ele=newmethod.find_element(tabele_ele[0], tabele_ele[1])
    text1 = ele.find_elements("tag name","tr")
    list = []
    for i in text1:
        list.append(i.text)
    newlist = list[0].split('\n')
    return newlist[0]


def assert_result_in():
    newmethod.assert_keyword(newtuple, titlecondb)

def assert_result_notin():
    newmethod.assert_keyword1(newtuple, titlecondb)


















