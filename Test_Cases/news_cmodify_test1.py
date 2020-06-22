import unittest
from framework.news_check_action import *
from framework.news_emodify_action import *
from framework.news_add_action import *
from test_data.news_add_data import *
from test_data.news_modify_data import *


class TestNews_edit(unittest.TestCase):
    #修改名称
    def test_01edit(self):
        check(value[0],newsele1[0],newsele1[1])
        click_checkbtn(checkbtn_ele[0],checkbtn_ele[1])
        row1 = rowcount(pagedata_ele[0], pagedata_ele[1])
        try:
            row1 != 0
            edit_btn(edit_btn_ele[0],edit_btn_ele[1])
            edit_name(editname_value[0], newname_ele[0], newname_ele[1])
            news_addbtn(save_btn_ele[0],save_btn_ele[1])
            newmethod.sleep(3)
            news_click_add(edit_tk_btn_ele[0], edit_tk_btn_ele[1])
            count=((dbrow(sql_edit01))[0][0])
            assert count==1
        except Exception as e:
            raise e




