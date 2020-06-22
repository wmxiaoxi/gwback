import yaml
import os
#读取yaml文件
path=os.path.abspath('.')
newpath=path+r'\userInfo.yaml'
print(newpath)
f=open(newpath,'r',encoding='utf-8')
data=yaml.load(f,Loader=yaml.FullLoader)
print(data)

