# coding:utf-8
from framework.news_check_action import *
from test_data.news_add_data import *
from framework.news_add_action import *
import unittest
from selenium.webdriver.common.keys import Keys
import os
from common_fuc.pageobj import *

class  TestNews_add (unittest.TestCase):

    #成功添加
    def test01_success_add(self):
        news_addbtn(addbtn_ele[0],addbtn_ele[1])
        news_name(namevalue[0],newname_ele[0],newname_ele[1])
        news_date(datevalue[0],newdate_ele[0],newdate_ele[1])
        newmethod.find_element(newdate_ele[0],newdate_ele[1]).send_keys(Keys.ENTER)
        sleep(3)
        news_click_add(newupload_ele[0],newupload_ele[1])
        sleep(3)
        os.system(r'D:\soft\1.exe')
        sleep(5)
        news_sumarry(summaryvalue[0],newsummary_ele[0],newsummary_ele[1])
        news_url(urlvalue[0],newurl_ele[0],newurl_ele[1])
        save(save_btn_ele[0],save_btn_ele[1])
        news_click_add(comfirm_btn_ele[0], comfirm_btn_ele[1])
        sleep(2)
        click_clearbtn(clearbtn_ele[0], clearbtn_ele[1])
        # 输入查询条件新闻标题
        check(namevalue[0], newsele1[0], newsele1[1])
        # 点击查询按钮
        click_checkbtn(checkbtn_ele[0], checkbtn_ele[1])
        time.sleep(10)
        assert nametext1()==namevalue[0]
        #assert_result_in()


    # #测试新闻标题不能为空
    # def test02_add(self):
    #     click_clearbtn(clearbtn_ele[0], clearbtn_ele[1])
    #     row1_02=rowcount(pagedata_ele[0],pagedata_ele[1])
    #     news_addbtn(addbtn_ele[0], addbtn_ele[1])
    #     news_date(datevalue[0], newdate_ele[0], newdate_ele[1])
    #     newmethod.find_element(newdate_ele[0], newdate_ele[1]).send_keys(Keys.ENTER)
    #     sleep(3)
    #     news_click_add(newupload_ele[0], newupload_ele[1])
    #     sleep(3)
    #     os.system(r'D:\soft\1.exe')
    #     sleep(5)
    #     news_sumarry(summaryvalue[0], newsummary_ele[0], newsummary_ele[1])
    #     news_url(urlvalue[0], newurl_ele[0], newurl_ele[1])
    #     save(save_btn_ele[0], save_btn_ele[1])
    #     news_click_add(comfirm_btn_ele[0], comfirm_btn_ele[1])
    #     sleep(3)
    #     #点击返回
    #     news_click_add(back_ele[0],back_ele[1])
    #     click_clearbtn(clearbtn_ele[0], clearbtn_ele[1])
    #     row2_02=rowcount(pagedata_ele[0],pagedata_ele[1])
    #     assert row1_02 == row2_02
    #
    #
    # #测试日期不能为空
    # def test03_add(self):
    #     click_clearbtn(clearbtn_ele[0], clearbtn_ele[1])
    #     row1_03 = rowcount(pagedata_ele[0], pagedata_ele[1])
    #     news_addbtn(addbtn_ele[0], addbtn_ele[1])
    #     news_name(namevalue[0], newname_ele[0], newname_ele[1])
    #     sleep(3)
    #     news_click_add(newupload_ele[0], newupload_ele[1])
    #     sleep(3)
    #     os.system(r'D:\soft\1.exe')
    #     sleep(5)
    #     news_sumarry(summaryvalue[0], newsummary_ele[0], newsummary_ele[1])
    #     news_url(urlvalue[0], newurl_ele[0], newurl_ele[1])
    #     # news_context(id,contextvalue)
    #     save(save_btn_ele[0], save_btn_ele[1])
    #     news_click_add(comfirm_btn03_ele[0], comfirm_btn03_ele[1])
    #     sleep(2)
    #     # 点击返回
    #     news_click_add(back_ele[0],back_ele[1])
    #     sleep(3)
    #     click_clearbtn(clearbtn_ele[0], clearbtn_ele[1])
    #     row2_03 = rowcount(pagedata_ele[0], pagedata_ele[1])
    #     assert row1_03 == row2_03
    #
    # #测试图片不能为空
    # def test04_add(self):
    #     click_clearbtn(clearbtn_ele[0], clearbtn_ele[1])
    #     row1_04 = rowcount(pagedata_ele[0], pagedata_ele[1])
    #     news_addbtn(addbtn_ele[0], addbtn_ele[1])
    #     news_name(namevalue[0], newname_ele[0], newname_ele[1])
    #     news_date(datevalue[0], newdate_ele[0], newdate_ele[1])
    #     newmethod.find_element(newdate_ele[0], newdate_ele[1]).send_keys(Keys.ENTER)
    #     sleep(3)
    #     news_sumarry(summaryvalue[0], newsummary_ele[0], newsummary_ele[1])
    #     news_url(urlvalue[0], newurl_ele[0], newurl_ele[1])
    #     # news_context(id,contextvalue)
    #     save(save_btn_ele[0], save_btn_ele[1])
    #     news_click_add(comfirm_btn_ele[0], comfirm_btn_ele[1])
    #     sleep(2)
    #     # 点击返回
    #     news_click_add(back_ele[0],back_ele[1])
    #     sleep(3)
    #     click_clearbtn(clearbtn_ele[0], clearbtn_ele[1])
    #     row2_04 = rowcount(pagedata_ele[0], pagedata_ele[1])
    #     assert row1_04 == row2_04
    #
    #
    #
    # #测试url，context不能都为空
    # def test06_add(self):
    #     click_clearbtn(clearbtn_ele[0], clearbtn_ele[1])
    #     row1_06 = rowcount(pagedata_ele[0], pagedata_ele[1])
    #     news_addbtn(addbtn_ele[0], addbtn_ele[1])
    #     news_name(namevalue[0], newname_ele[0], newname_ele[1])
    #     news_date(datevalue[0], newdate_ele[0], newdate_ele[1])
    #     newmethod.find_element(newdate_ele[0], newdate_ele[1]).send_keys(Keys.ENTER)
    #     sleep(3)
    #     news_click_add(newupload_ele[0], newupload_ele[1])
    #     sleep(3)
    #     os.system(r'D:\soft\1.exe')
    #     sleep(5)
    #     news_sumarry(summaryvalue[0], newsummary_ele[0], newsummary_ele[1])
    #     save(save_btn_ele[0], save_btn_ele[1])
    #     news_click_add(comfirm_btn_ele[0], comfirm_btn_ele[1])
    #     sleep(2)
    #     # 点击返回
    #     news_click_add(back_ele[0],back_ele[1])
    #     sleep(3)
    #     click_clearbtn(clearbtn_ele[0], clearbtn_ele[1])
    #     row2_06 = rowcount(pagedata_ele[0], pagedata_ele[1])
    #     assert row1_06 == row2_06
    #
    # #测试url为空,context不为空，成功添加
    #
    # def test07_add(self):
    #     click_clearbtn(clearbtn_ele[0], clearbtn_ele[1])
    #     news_addbtn(addbtn_ele[0], addbtn_ele[1])
    #     news_name(namevalue[2], newname_ele[0], newname_ele[1])
    #     news_date(datevalue[0], newdate_ele[0], newdate_ele[1])
    #     newmethod.find_element(newdate_ele[0], newdate_ele[1]).send_keys(Keys.ENTER)
    #     sleep(3)
    #     news_click_add(newupload_ele[0], newupload_ele[1])
    #     sleep(5)
    #     os.system(r'D:\soft\1.exe')
    #     sleep(5)
    #     news_sumarry(summaryvalue[0], newsummary_ele[0], newsummary_ele[1])
    #     sleep(3)
    #
    #     #frame=newmethod.find_element("xpath","//iframe[starts-with(@id,\"ueditor_\")]")
    #     #newmethod.switch_frame(frame)
    #     #newmethod.find_element("xpath","/html/body").send_keys("测试富文本里输入内容，测试哦测试哦")
    #
    #
    #     frame=context_frame("xpath","//iframe[starts-with(@id,\"ueditor_\")]")
    #     news_context_loc(frame)
    #     news_context(contextvalue[0],"xpath","/html/body")
    #
    #     sleep(3)
    #     newmethod.default()
    #     save(save_btn_ele[0], save_btn_ele[1])
    #     news_click_add(comfirm_btn_ele[0], comfirm_btn_ele[1])
    #     sleep(3)
    #     click_clearbtn(clearbtn_ele[0], clearbtn_ele[1])
    #     check(namevalue[2],newsele1[0],newsele1[1])
    #     #点击查询按钮
    #     click_checkbtn(checkbtn_ele[0],checkbtn_ele[1])
    #     row1_07 = rowcount(pagedata_ele[0], pagedata_ele[1])
    #     row2_07=len(dbrow(select07))
    #     assert row1_07 ==row2_07==1
    #
    # #url,context都不为空,测试不能同时添加
    #
    # def test08_add(self):
    #     click_clearbtn(clearbtn_ele[0], clearbtn_ele[1])
    #     news_addbtn(addbtn_ele[0], addbtn_ele[1])
    #     news_name(namevalue[1], newname_ele[0], newname_ele[1])
    #     news_date(datevalue[0], newdate_ele[0], newdate_ele[1])
    #     newmethod.find_element(newdate_ele[0], newdate_ele[1]).send_keys(Keys.ENTER)
    #     sleep(3)
    #     news_click_add(newupload_ele[0], newupload_ele[1])
    #     sleep(3)
    #     os.system(r'D:\soft\1.exe')
    #     sleep(6)
    #     news_sumarry(summaryvalue[0], newsummary_ele[0], newsummary_ele[1])
    #     news_url(urlvalue[0], newurl_ele[0], newurl_ele[1])
    #     sleep(3)
    #
    #     frame=context_frame("xpath","//iframe[starts-with(@id,\"ueditor_\")]")
    #     news_context_loc(frame)
    #     news_context(contextvalue[0],"xpath","/html/body")
    #
    #     sleep(3)
    #     newmethod.default()
    #     save(save_btn_ele[0], save_btn_ele[1])
    #     news_click_add(comfirm_btn_ele[0], comfirm_btn_ele[1])
    #     sleep(4)
    #     # 点击返回
    #     #newmethod.find_element("xpath","//*[@id=\"app\"]/div/section/section/main/div/div[1]/div[2]").click()
    #     #news_click_add('xpath','//*[@id=\"app\"]/div/section/section/main/div/div[1]/div[2]')
    #     news_click_add(back_ele[0], back_ele[1])
    #     sleep(3)
    #     click_clearbtn(clearbtn_ele[0], clearbtn_ele[1])
    #     check(namevalue[1], newsele1[0], newsele1[1])
    #     sleep(4)
    #     #点击查询按钮
    #     click_checkbtn(checkbtn_ele[0],checkbtn_ele[1])
    #     row1_08 = rowcount(pagedata_ele[0], pagedata_ele[1])
    #     row2_08 =len(dbrow(select08))
    #     assert row1_08==row2_08==0
    #
    #
    #
    # #添加的url地址不正确，添加失败
    # def test09_add(self):
    #     click_clearbtn(clearbtn_ele[0], clearbtn_ele[1])
    #     news_addbtn(addbtn_ele[0], addbtn_ele[1])
    #     news_name(namevalue[1], newname_ele[0], newname_ele[1])
    #     news_date(datevalue[0], newdate_ele[0], newdate_ele[1])
    #     newmethod.find_element(newdate_ele[0], newdate_ele[1]).send_keys(Keys.ENTER)
    #     sleep(3)
    #     news_click_add(newupload_ele[0], newupload_ele[1])
    #     sleep(3)
    #     os.system(r'D:\soft\1.exe')
    #     sleep(5)
    #     news_sumarry(summaryvalue[0], newsummary_ele[0], newsummary_ele[1])
    #     news_url(urlvalue[1], newurl_ele[0], newurl_ele[1])
    #     sleep(3)
    #     save(save_btn_ele[0], save_btn_ele[1])
    #     news_click_add(comfirm_btn_ele[0], comfirm_btn_ele[1])
    #     sleep(6)
    #     # 点击返回
    #     news_click_add(back_ele[0], back_ele[1])
    #     sleep(3)
    #     click_clearbtn(clearbtn_ele[0], clearbtn_ele[1])
    #     check(namevalue[1], newsele1[0], newsele1[1])
    #     #点击查询按钮
    #     click_checkbtn(checkbtn_ele[0],checkbtn_ele[1])
    #     row1_09 = rowcount(pagedata_ele[0], pagedata_ele[1])
    #     row2_09 =len(dbrow(select08))
    #     assert row1_09==row2_09==0
    #
    #
    #     #测试描述简介不能为空
    #     def test10_add(self):
    #         click_clearbtn(clearbtn_ele[0], clearbtn_ele[1])
    #         row1_10 = rowcount(pagedata_ele[0], pagedata_ele[1])
    #         news_addbtn(addbtn_ele[0], addbtn_ele[1])
    #         news_name(namevalue[0], newname_ele[0], newname_ele[1])
    #         news_date(datevalue[0], newdate_ele[0], newdate_ele[1])
    #         newmethod.find_element(newdate_ele[0], newdate_ele[1]).send_keys(Keys.ENTER)
    #         sleep(3)
    #         news_click_add(newupload_ele[0], newupload_ele[1])
    #         sleep(3)
    #         os.system(r'D:\soft\1.exe')
    #         sleep(5)
    #         #news_sumarry(summaryvalue[0], newsummary_ele[0], newsummary_ele[1])
    #         news_url(urlvalue[0], newurl_ele[0], newurl_ele[1])
    #         # news_context(id,contextvalue)
    #         save(save_btn_ele[0], save_btn_ele[1])
    #         news_click_add(comfirm_btn_ele[0], comfirm_btn_ele[1])
    #         sleep(2)
    #         # 点击返回
    #         news_click_add(back_ele[0],back_ele[1])
    #         sleep(3)
    #         click_clearbtn(clearbtn_ele[0], clearbtn_ele[1])
    #         row2_10 = rowcount(pagedata_ele[0], pagedata_ele[1])
    #         assert row1_10 == row2_10
    #
    #
    #
    #
    # #     #测试添加的图片格式不正确，添加失败，此场景现未实现













