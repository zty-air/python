from pyecharts.charts import Line
from pyecharts.options import TitleOpts,VisualMapOpts,ToolboxOpts
import json
def Usa_Data():
    with open("python\dataview\折线图数据\美国.txt","r",encoding="utf8") as f:
        usa_data=f.read() 
        usa_data=usa_data.replace("jsonp_1629344292311_69436(","")[:-2]
        usa_data = json.loads(usa_data)
    f.close()
    return usa_data
def Jp_Data():
    with open("python\dataview\折线图数据\日本.txt","r",encoding="utf8") as fj:
        Jp_data=fj.read() 
        Jp_data= Jp_data.replace("jsonp_1629350871167_29498(","")[:-2]
        Jp_data= json.loads( Jp_data)
    fj.close()
    return Jp_data
def In_Data():
    with open("python\dataview\折线图数据\印度.txt","r",encoding="utf8") as fi:
        In_data=fi.read() 
        In_data=  In_data.replace("jsonp_1629350745930_63180(","")[:-2]
        In_data= json.loads( In_data)
    fi.close()
    return In_data
 
usa=Usa_Data()
usa_x=usa['data'][0]['trend'][ "updateDate"][:314]
usa_y=usa['data'][0]['trend'][ "list"][0]["data"][:314]


jp=Jp_Data()
jp_y=jp['data'][0]['trend'][ "list"][0]["data"][:314]

indan=In_Data()
indan_y=indan['data'][0]['trend'][ "list"][0]["data"][:314]


line=Line()
line.add_xaxis(usa_x)
line.add_yaxis("美国",usa_y)
line.add_yaxis("日本",jp_y)
line.add_yaxis("印度",indan_y)
line.set_global_opts(
    title_opts=TitleOpts(title="美日印三国2021年疫情图表",pos_bottom="1%",pos_left="center"),
    # visualmap_opts=VisualMapOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
)
line.render()

# print(usa_y)
# print()
# print(indan_y)
# print()
# print(jp_y)


