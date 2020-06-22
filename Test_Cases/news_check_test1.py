import unittest

from test_data.news_check_data import *
from framework.news_check_action import *

class  TestNews_check (unittest.TestCase):

    # 全部数据查询
    def test01_check(self):
        #点击重置按钮
        click_clearbtn(clearbtn_ele[0],clearbtn_ele[1])
        # 根据查询条件获取页面查询出的条数
        row1 = rowcount(pagedata_ele[0], pagedata_ele[1])
        print(row1)
        # 根据查询条件获取数据库数据
        titlecondb = dbrow(select_full)
        # 获取数据库根据条件查询出条数
        row2 = len(titlecondb)
        # 查询出第一页面数据的title和数据库查出的进行对比
        if row1 != 0:
            # 判断数据库条数和页面条数是否相等
            assert row1==row2
            nametext(select_full)
        else:
            self.assertEqual(row1, row2)



    #新闻根据名称来查询
    def test02_check_name(self):
        # 点击重置按钮
        click_clearbtn(clearbtn_ele[0], clearbtn_ele[1])
        #输入查询条件新闻标题
        check(value[0],newsele1[0],newsele1[1])
        #点击查询按钮
        click_checkbtn(checkbtn_ele[0],checkbtn_ele[1])
        #根据查询条件获取页面查询出的条数
        row1=rowcount(pagedata_ele[0],pagedata_ele[1])
        #根据查询条件获取数据库数据
        titlecondb = dbrow(select_name)
        #获取数据库根据条件查询出条数
        row2=len(titlecondb)
        #查询出第一页面数据的title和数据库查出的进行对比
        if row1 != 0:
            # 判断数据库条数和页面条数是否相等
            self.assertEqual(row1, row2)
            nametext(select_name)
        else:
            self.assertEqual(row1, row2)



    #根据发布日期来查询
    def test03_check_date(self):
        # 点击重置按钮
        click_clearbtn(clearbtn_ele[0], clearbtn_ele[1])
        # 输入查询条件时间
        check(value[1], timele1[0], timele1[1])
        check(value[1], timele2[0], timele2[1])
        click_checkbtn(checkbtn_ele[0],checkbtn_ele[1])
        # 根据查询条件获取页面查询出的条数
        row1 = rowcount(pagedata_ele[0], pagedata_ele[1])
        # 根据查询条件获取数据库数据
        titlecondb = dbrow(select_date)
        # 获取数据库根据条件查询出条数
        row2 = len(titlecondb)
        # 查询出第一页面数据的title和数据库查出的进行对比
        if row1 != 0:
            # 判断数据库条数和页面条数是否相等
            self.assertEqual(row1, row2)
            nametext(select_date)
        else:
            self.assertEqual(row1, row2)




    #根据状态来查询
    def test04_check_status(self):
        # 点击重置按钮
        click_clearbtn(clearbtn_ele[0], clearbtn_ele[1])
        #选择状态
        findele(statusele[0],statusele[2])
        newmethod.sleep(3)
        click_checkbtn(checkbtn_ele[0], checkbtn_ele[1])
        # 根据查询条件获取页面查询出的条数
        row1 = rowcount(pagedata_ele[0], pagedata_ele[1])
        # 根据查询条件获取数据库数据
        titlecondb = dbrow(select_status)
        # 获取数据库根据条件查询出条数
        row2 = len(titlecondb)
        # 查询出第一页面数据的title和数据库查出的进行对比
        if row1 != 0:
            # 判断数据库条数和页面条数是否相等
            self.assertEqual(row1, row2)
            nametext(select_status)
        else:
            self.assertEqual(row1, row2)




    #不输入查询条件，点击【查询】有提示信息
    def test_05check_empty(self):
        # 点击重置按钮
        click_clearbtn(clearbtn_ele[0], clearbtn_ele[1])
        # 点击查询按钮
        click_checkbtn(checkbtn_ele[0], checkbtn_ele[1])
        newmethod.sleep(3)
        newmethod.click(check_tk_btn_ele[0],check_tk_btn_ele[1])
        newmethod.sleep(3)







#分页查看





#查看主页面上数据的正确性
















# login(username[0], password[0])
# check(value[0],newsele1[0],newsele1[1],checkbtn[0],checkbtn[1])
# row1 = rowcount(pagedata[0], pagedata[1])
# ele=newmethod.find_element(tabele[0],tabele[1])
# text1=ele.find_elements("tag name","tr")
# list=[]
# for i in text1:
#     list.append(i.text)
# list=list[0].split('\n')
# newtuple=(list[0],datetime.datetime.strptime(list[1],"%Y-%m-%d %H:%M:%S"),list[3])
# print(newtuple)
# titlecondb = dbrow(selectname)
# newmethod.assert_keyword(newtuple,titlecondb)














