import requests
from lxml import etree
import threading
import time
import os
def get_url(url_1):
    url=url_1
    header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"}
    req=requests.get(url,headers=header)
    return req
def get_picture(requ):
    req=requ
    e=etree.HTML(req.text)
    e=e.xpath("//div[@class='tab-cont']/div/div/img/@data-src")
    return e
def download_picture(e):
    sum=200
    threads=[]
    for i  in e:
        #e=i.replace("1366x768.jpg","2732x2048.jpg") 
        #e=i.replace("640x960.jpg","1080x1920.jpg") 
        e=i.replace("1024x768.jpg","2732x2048.jpg")
        name="D:\\python\\2023\python\\picture\\图片\\"+e[62:70]+'_'+i[71:72]+'.jpg'
        pic=get_url(e).content
        print(e)
        # print(f"Downloading picture \b{name}")
        # with open(f"{name}",'ab') as f:
        #     f.write(pic)
        # f.close()
        if sum==0:
            break
        sum-=1
def make_directory():
    if not os.path.exists("python\picture\横板图片"):
        os.makedirs("python/picture/横板图片")
    if not os.path.exists("python\picture\竖板图片"):
        os.makedirs("python/picture/竖板图片")
 
make_directory()
re_req=get_url("https://yys.163.com/media/picture.html")
download_picture(get_picture(re_req))

