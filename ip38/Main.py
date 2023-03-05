import requests
from lxml import etree
while True:
    tel=input("Enter the number\n")
    #tel="15025709895"
    if (len(tel)!=11 or tel[0]!='1'):
        print("tel is error try again :",len(tel))     
    else:
        url=f"https://www.ip138.com/mobile.asp?mobile={tel}&action=mobile"
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"}
        res=requests.get(url=url, headers=headers)
        e=etree.HTML(res.text)
        data=e.xpath("//tr/td[1]/text()")
        data_area=e.xpath("//tr/td[2]/span/text()")
        data_s=e.xpath("//tr/td[2]/a/text()")
        moble={data[0]:data_s[0],data[1]:data_area[0],data[2]:data_s[3],data[3]:data_s[0][:3],data[4]:data_s[4],data[5]:data_s[5]}
        print(moble)
        break

 