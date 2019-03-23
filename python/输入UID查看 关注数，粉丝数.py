# -*-coding:utf-8-*-
from urllib import request
UID = input('please input your UID :')
vmid = str(UID)

'''用api中的vmid字段进行用户查找'''
url = 'https://api.bilibili.com/x/relation/stat?vmid='+vmid
req = request.Request(url)
page = request.urlopen(req).read()
page = page.decode('utf-8')

'''正则表达式'''
import re
string = page

print('uid :',vmid)

follower_num = re.findall('"follower":([0-9]*)',string,flags=0)
num = int(follower_num[0])
print('follower :',num)

following_num = re.findall('"following":([0-9]*)',string,flags=0)
num = int(following_num[0])
print('following :',num)


input()





