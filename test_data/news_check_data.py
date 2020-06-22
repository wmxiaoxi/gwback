import datetime

#查询条件输入值：标题名称|发布
value=('自动化测试','2019-11-21')

#全部查询
select_full="SELECT title,created_date,case TIMESTAMPDIFF(YEAR,now(), created_date) >= 1 WHEN  1 then '失效' else '正常'  end , case published  when 1 then '是' else'否' end FROM official_website.article where  article_type like '%新闻%'"
#根据新闻标题筛选条件查询
select_name="SELECT title,created_date,case TIMESTAMPDIFF(YEAR,now(), created_date) >= 1 WHEN  1 then '失效' else '正常'  end , case published  when 1 then '是' else'否' end FROM official_website.article where  article_type like '%新闻%' and title like '%自动化%'"

select_date="SELECT title,created_date,case TIMESTAMPDIFF(YEAR,now(), created_date) >= 1 WHEN  1 then '失效' else '正常'  end , case published  when 1 then '是' else'否' end FROM official_website.article where  article_type like '%新闻%' and created_date>='2019-11-21 00:00:00' and created_date<='2019-11-21 23:59:59'"
select_status="select * from (SELECT title,created_date,case TIMESTAMPDIFF(YEAR,created_date,now()) >= 1 WHEN  1 then '失效' else '正常' end as status , case published  when 1 then '是' else'否' end FROM official_website.article where  article_type like '%新闻%') cc where cc.status like '%正常%'"