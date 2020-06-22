#上传图片路径
path=(r'‪C:\Users\user\Desktop\3.png')

#value
namevalue=('自动化测试',"非正常添加",'自动化测试1')
datevalue=('2019-12-04',)
summaryvalue=('自动化测试--新增新闻',)
urlvalue=('http://www.baidu.com','www.baidu.com','1111')
contextvalue=('测试富文本里输入内容，测试哦测试哦',)

#图片存放地址
image=r"D:\soft\1.exe"

#sql
sql_add="SELECT title,created_date,case TIMESTAMPDIFF(YEAR,now(), created_date) >= 1 WHEN  1 then '失效' else '正常'  end , case published  when 1 then '是' else'否' end FROM official_website.article where  article_type like '%新闻%' and title like '%自动化测试%'"
select07="SELECT title,created_date,case TIMESTAMPDIFF(YEAR,now(), created_date) >= 1 WHEN  1 then '失效' else '正常'  end , case published  when 1 then '是' else'否' end FROM official_website.article where  article_type like '%新闻%' and title like '%自动化测试1%'"
select08="SELECT title,created_date,case TIMESTAMPDIFF(YEAR,now(), created_date) >= 1 WHEN  1 then '失效' else '正常'  end , case published  when 1 then '是' else'否' end FROM official_website.article where  article_type like '%新闻%' and title like '%非正常添加%'"


