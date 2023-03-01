# Streamlit Elements includes 45 dataviz components powered by Nivo.
from streamlit_elements import elements, mui, html,nivo
import streamlit as st
import pandas as pd
import numpy as np
import time


st.set_page_config(
    page_title="食谱推荐",
    page_icon="🍳",
)


#隐藏streamlit自带的功能按钮，右边的菜单栏的页脚
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.markdown('# 🏠 食谱推荐')


st.markdown(
        "#### 💪 输入数据，了解身体所需要的物质"
    )


#选择性别
st.selectbox("👇请选择您的性别",("男","女"))
#输入年龄
number_age = st.number_input("👇请输入您的年龄",1,150,22)
#输入身高
number_height = st.number_input("👇请输入您的身高（cm）",30,250,175)
#输入体重
number_weigh = st.number_input("👇请输入您的体重（kg）",5,200,75)


#计算BMI并保留一位小数
number_bmi = number_weigh / ((number_height/100) * (number_height/100))
number_bmi = round(number_bmi,1)


if st.button('开始推荐'):
    st.write('您的BMI是:',number_bmi)
    if number_bmi >= 18.5 and number_bmi <= 23.9 : 
        st.write("您的体重在正常范围✌")
    elif number_bmi <18.5 :
        st.write("您的体重偏低")
    elif number_bmi >23.9 :
        st.write("您的体重偏高")


    #绘制雷达图
    with elements("nivo_charts"):

        DATA = [
            { "taste": "fruity", "chardonay": 93, "carmenere": 61, "syrah": 114 },
            { "taste": "bitter", "chardonay": 91, "carmenere": 37, "syrah": 72 },
            { "taste": "heavy", "chardonay": 56, "carmenere": 95, "syrah": 99 },
            { "taste": "strong", "chardonay": 64, "carmenere": 90, "syrah": 30 },
            { "taste": "sunny", "chardonay": 119, "carmenere": 94, "syrah": 103 },
        ]

        #图形外观参数
        with mui.Box(sx={"height": 500}):
            nivo.Radar(
                data=DATA,
                keys=[ "chardonay", "carmenere", "syrah" ],
                indexBy="taste",
                valueFormat=">-.2f",
                margin={ "top": 70, "right": 80, "bottom": 40, "left": 80 },
                borderColor={ "from": "color" },
                gridLabelOffset=36,
                dotSize=10,
                dotColor={ "theme": "background" },
                dotBorderWidth=2,
                motionConfig="wobbly",
                legends=[
                    {
                        "anchor": "top-left",
                        "direction": "column",
                        "translateX": -50,
                        "translateY": -40,
                        "itemWidth": 80,
                        "itemHeight": 20,
                        "itemTextColor": "#999",
                        "symbolSize": 12,
                        "symbolShape": "circle",
                        "effects": [
                            {
                                "on": "hover",
                                "style": {
                                    "itemTextColor": "#000"
                                }
                            }
                        ]
                    }
                ],
                theme={
                    "background": "#FFFFFF",
                    "textColor": "#31333F",
                    "tooltip": {
                        "container": {
                            "background": "#FFFFFF",
                            "color": "#31333F",
                        }
                    }
                }
            )   
                
                 



