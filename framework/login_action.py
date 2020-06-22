
from common_fuc.basic_method import *
from common_fuc.pageobj.login_obj import *

newmethod=method()
def login(uername,password):
     #newmethod.open1(url)
     newmethod.sleep(3)
     newmethod.send_keys(uername,ele[0],ele[1])
     newmethod.send_keys(password,ele[0],ele[2])
     newmethod.click(btn_ele[0],btn_ele[1])



