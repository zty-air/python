import requests
from lxml import etree
import time
Main_url="https://www.biquge9.com"
def Get_Url(url):#获取主页
    header ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"}
    re=requests.get(url,headers=header)
    return re
def download_noval(noval_url):
    global Main_url
    e=etree.HTML(noval_url)
    data=e.xpath("//div[@class='listmain']/dl/dd/a/@href")
    first_noval_url= str(Main_url+data[0])#获取第一个章节的url
    noval_end=str(data[len(data)-1])
    del data#删除列表
    noval_end_pos=int(str(noval_end.rindex('/')))#获取最后章节中最后一个/的位置
    noval_start_pos=int(str(first_noval_url.rindex('/')))#获取第一章节中最后一个/的位置
    noval_start=int(first_noval_url[noval_start_pos+1:first_noval_url.rindex('.')])#截取第一章的页数
    noval_end=int(noval_end[noval_end_pos+1:noval_end.rindex('.')])#截取最后一章的页数
    noval_ulr_list=[]
    for i in  range(noval_start,noval_end+1):#由于是半开半闭区间所以+1 以防最后一章获取不到
        noval_ulr_list.append(first_noval_url[:noval_start_pos+1]+str(i)+'.html')#+1为了获取到/,组成完整的url地址
    # print(noval_ulr_list)
    def download(url):
        # url="https://www.biquge9.com/book/1460/1.html"
        data=Get_Url(url).text
        e=etree.HTML(data)
        title=str(e.xpath("//h1/text()"))
        content=title+'\n'+str(e.xpath('//div[@id="chaptercontent"]/text()'))
        # print(title,'\n',str(content).replace('\u3000',' '))
        print(f"downloading {title} \n")
        with open("test.txt",'a+',encoding='utf8') as f:
            f.write(str(content).replace(''',''','\n'))
        f.close()
    count=0
    for  i in noval_ulr_list:
        count+=1
        download(i)
        if count%10==0:
            time.sleep(0.09)

def downloaded_url(url):
    global Main_url
    e=etree.HTML(url)
    data=e.xpath('//div[@class="bookbox"][1]/div/div/a/@href')#选取第一个作为本次任务
    url=Main_url+data[0]#data类型为list+原本网址
    # print(url)
    download_noval(Get_Url(url).text)




novel_name ="完美世界"
url=f"https://www.biquge9.com/s?q=%{novel_name}"
result=Get_Url(url).text
downloaded_url(result)