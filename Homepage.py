# Streamlit Elements includes 45 dataviz components powered by Nivo.
from streamlit_elements import elements, mui, html,nivo
import streamlit as st
import pandas as pd
import numpy as np
import time


st.set_page_config(
    page_title="é£è°±æ¨è",
    page_icon="ð³",
)


#éèstreamlitèªå¸¦çåè½æé®ï¼å³è¾¹çèåæ çé¡µè
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.markdown('# ð  é£è°±æ¨è')


st.markdown(
        "#### ðª è¾å¥æ°æ®ï¼äºè§£èº«ä½æéè¦çç©è´¨"
    )


#éæ©æ§å«
st.selectbox("ðè¯·éæ©æ¨çæ§å«",("ç·","å¥³"))
#è¾å¥å¹´é¾
number_age = st.number_input("ðè¯·è¾å¥æ¨çå¹´é¾",1,150,22)
#è¾å¥èº«é«
number_height = st.number_input("ðè¯·è¾å¥æ¨çèº«é«ï¼cmï¼",30,250,175)
#è¾å¥ä½é
number_weigh = st.number_input("ðè¯·è¾å¥æ¨çä½éï¼kgï¼",5,200,75)


#è®¡ç®BMIå¹¶ä¿çä¸ä½å°æ°
number_bmi = number_weigh / ((number_height/100) * (number_height/100))
number_bmi = round(number_bmi,1)


if st.button('å¼å§æ¨è'):
    st.write('æ¨çBMIæ¯:',number_bmi)
    if number_bmi >= 18.5 and number_bmi <= 23.9 : 
        st.write("æ¨çä½éå¨æ­£å¸¸èå´â")
    elif number_bmi <18.5 :
        st.write("æ¨çä½éåä½")
    elif number_bmi >23.9 :
        st.write("æ¨çä½éåé«")


    #ç»å¶é·è¾¾å¾
    with elements("nivo_charts"):

        DATA = [
            { "taste": "fruity", "chardonay": 93, "carmenere": 61, "syrah": 114 },
            { "taste": "bitter", "chardonay": 91, "carmenere": 37, "syrah": 72 },
            { "taste": "heavy", "chardonay": 56, "carmenere": 95, "syrah": 99 },
            { "taste": "strong", "chardonay": 64, "carmenere": 90, "syrah": 30 },
            { "taste": "sunny", "chardonay": 119, "carmenere": 94, "syrah": 103 },
        ]

        #å¾å½¢å¤è§åæ°
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
                
                 



