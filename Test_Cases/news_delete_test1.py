import unittest

from test_data.news_delete_data import *
from test_data.news_modify_data import *
from framework.news_del_action import *
#点击弹框上得取消按钮取消删除
class TestNews_del(unittest.TestCase):

#点击弹框上得确定按钮成功删除
    def test_del01(self):
        check(editname_value[0], newsele1[0], newsele1[1])
        click_checkbtn(checkbtn_ele[0], checkbtn_ele[1])
        row1 = rowcount(pagedata_ele[0], pagedata_ele[1])
        try:
            row1 != 0
            del_clik_btn(del_btn_ele[0], del_btn_ele[1])
            newmethod.sleep(4)
            # self.tijiao = newmethod.find_element('xpath',"/html/body/div[3]/div/div[3]/button[2]")
            # self.tijiao.click()
            del_clik_btn(del_comfirm[0], del_comfirm[1])
            count=(dbrow(sql_edit01))[0][0]
            assert count==0
        except Exception as e:
            raise e




    def test_del02(self):
        del02_count1 = len(dbrow(del_sql))
        click_clearbtn(clearbtn_ele[0],clearbtn_ele[1])
        newmethod.sleep(3)
        del_clik_btn(del_btn_ele[0],del_btn_ele[1])
        newmethod.sleep(4)
        del_clik_btn(del_dismiss[0],del_dismiss[1])
        del02_count2=len(dbrow(del_sql))
        assert del02_count1==del02_count2







