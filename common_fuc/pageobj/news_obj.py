####【新增】
#新增按钮得定位
addbtn_ele=("xpath","//*[@id=\"app\"]/div/section/section/main/div/div[3]/div[1]/div/div[1]/div[2]/div/button")
#新闻名称
newname_ele=("xpath","//*[@id=\"app\"]/div/section/section/main/div/form/div[1]/div/div[1]/input")
#显示日期
newdate_ele=("xpath","//*[@id=\"app\"]/div/section/section/main/div/form/div[2]/div/div[1]/input")
#新闻封面得上传按钮
newupload_ele=("xpath","//*[@id=\"app\"]/div/section/section/main/div/form/div[3]/div/div[2]/div/button")

#摘要
newsummary_ele=("xpath","//*[@id=\"app\"]/div/section/section/main/div/form/div[4]/div/div[1]/input")
#url连接
newurl_ele=("xpath","//*[@id=\"app\"]/div/section/section/main/div/form/div[5]/div/div[1]/input")

#新闻内容富文本框架id
id='ueditor_0'


#保存按钮定位
save_btn_ele=("xpath","//*[@id=\"app\"]/div/section/section/main/div/form/button[3]")

#test01 test02  test04 test05  test06  保存成功弹框上确定按钮
comfirm_btn_ele=("xpath","/html/body/div[4]/div/div[3]/button")


#test03上确定按钮的定位
comfirm_btn03_ele=("xpath","/html/body/div[3]/div/div[3]/button")

#暂存按钮定位

temp_btn=("")
#预览定位


#返回按钮定位
back_ele=("xpath","//*[@id=\"app\"]/div/section/section/main/div/div[1]/div[2]")


#####【查询】
#新闻查询标题输入框点定位
newsele1=("xpath","//*[@id=\"app\"]/div/section/section/main/div/div[4]/div[1]/input")

#发布日期得输入框定位
timele1=("xpath","//*[@id=\"app\"]/div/section/section/main/div/div[4]/div[2]/input[1]")
#发布日期得输入框截止定位
timele2=("xpath","//*[@id=\"app\"]/div/section/section/main/div/div[4]/div[2]/input[2]")

#状态定位\xpath\失效|正常
statusele=("xpath","/html/body/div[5]/div[1]/div[1]/ul/li[2]","/html/body/div[5]/div[1]/div[1]/ul/li[1]")

#新闻查询页面查询按钮定位
checkbtn_ele=("xpath","//*[@id=\"app\"]/div/section/section/main/div/div[4]/button[1]/span")

#重置按钮得定位
clearbtn_ele=("xpath","//*[@id=\"app\"]/div/section/section/main/div/div[4]/button[2]")

#查询弹框上得【确定】按钮定位
check_tk_btn_ele=("xpath","/html/body/div[5]/div/div[3]/button")

#页面下方分页数据的条数定位
pagedata_ele=("xpath","//*[@id=\"app\"]/div/section/section/main/div/div[4]/div[5]/span[1]")

#新闻页面table定位
tabele_ele=("xpath","//*[@id=\"app\"]/div/section/section/main/div/div[4]/div[4]/div[3]/table")

#新闻第一页新闻标题的内容定位
titlexpath_ele=('xpath','//*[@id="app"]/div/section/section/main/div/div[4]/div[4]/div[3]/table/tbody/tr/td[1]/div')


#####【删除】

#删除按钮定位
del_btn_ele=("xpath","//*[@id=\"app\"]/div/section/section/main/div/div[4]/div[4]/div[3]/table/tbody/tr/td[5]/div/button[2]/span")

sql_del='select count(*) from official_website.article where title like "修改测试名称" and article_type like "%新闻%"'
#删除弹框上按钮定位
del_comfirm=("xpath","/html/body/div[3]/div/div[3]/button[2]")
del_dismiss=("xpath","/html/body/div[3]/div/div[3]/button[1]")


####【修改】
edit_btn_ele=("xpath",'//*[@id=\"app\"]/div/section/section/main/div/div[4]/div[4]/div[3]/table/tbody/tr[1]/td[5]/div/button[1]')
#弹框上得按钮定位
edit_tk_btn_ele=("xpath","/html/body/div[3]/div/div[3]/button")

