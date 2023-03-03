from pyecharts.charts import Line
from pyecharts.options import( TitleOpts,VisualMapOpts,ToolboxOpts,LegendOpts

                        )

line=Line()
#设置x轴数据
line.add_xaxis(["中国","美国","法国"])
#设置y轴数据
line.add_yaxis("GDP",[30,20,10])
line.set_global_opts(
    #设置主标题
    title_opts=TitleOpts(title="世界各国GDP",pos_bottom="1%",pos_left="center"),
    #是视觉映射组件，用于进行『视觉编码』，也就是将数据映射到视觉元素（视觉通道）
    visualmap_opts=VisualMapOpts(is_show=True),
    #设置图表工具箱是否显示
    toolbox_opts=ToolboxOpts(is_show=True),
    #设置图标标签
    legend_opts=LegendOpts(is_show=False),
)   
 

#生成html文件
line.render()