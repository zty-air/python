import requests
from lxml import etree
import threading
import time
import os
def get_url(url):
    header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"}
    req=requests.get(url, headers=header)
    return req
def get_picture(req):
    e=etree.HTML(req.text)
    urls=e.xpath("//div[@class='tab-cont']/div/div/img/@data-src")
    urls=[url.replace("1366x768", "2732x2048") for url in urls]
    urls=[url.replace("640x960", "1080x1920") for url in urls]
    urls=[url.replace("1024x768", "2732x2048") for url in urls]
    return urls
def download_picture(url):
    name="python\\picture\\图片\\"+url[62:70]+'_'+url[71:72]+'.jpg'
    pic=get_url(url).content
    # time.sleep(1)
    print(f"Downloading picture {name}")
    with open(f"{name}",'wb') as f:
        f.write(pic)
def make_directory():
    if not os.path.exists("python\picture\图片"):
        os.makedirs("python/picture/图片")
     
make_directory()
req=get_url("https://yys.163.com/media/picture.html")
urls=get_picture(req)
# print(urls)
for url in urls:
    download_picture(url)
    # break

# threads=[]
# for url in urls:
#     threads.append(threading.Thread(target=download_picture, args=(url,)))
#     break
# print (threads)
# for t in threads:
#     t.start()
# for t in threads:
#     t.join()