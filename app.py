import altair as alt
import copy
import numpy as np
import pandas as pd
import scipy.stats as stats
import streamlit as st
import plotly.express as px
import plotly as plt

def mainapp():
    alt.renderers.set_embed_options(scaleFactor=2)

    #st.set_page_config(layout="wide")

    #st.title("Design to WIN Simulator")
    col1, mid, col2 = st.columns([100,5,20])
    with col1:
        st.title('Intel - Design to Win simulator for Sample Account')
    with col2:
        st.image('c5logo.jpg', width=150)
    st.markdown(
        "A Digital Twin Simulator for understanding effects of multiple variables on CLV analysis "
    )
    st.sidebar.title("Control Panel")
    left_col, middle_col, right_col = st.columns(3)

    tick_size = 12
    axis_title_size = 16
   
    st.sidebar.subheader("Market Research Values")
    
    #NPS: 
    #CUSTOMERINDEX: 
    #EASE:
    #TRUST:
    #EFFECTIVENESS:
    #DESIGN_TO_DEAL:
    #
    npsmultiplier = st.sidebar.slider(
    "NPS Score",
    min_value=0,
    max_value=10,
    value=8,
    step=1,
    help="Select NPS Score value to see the variability ",
    )

    #st.sidebar.subheader("Decision criteria")
    customerindexmetric = 8

    trustmetric = st.sidebar.slider(
    "Trust",
    min_value=0,
    max_value=10,
    value=7,
    step=1,
    help="Set Trust value to understand how CLV changes with Trust",
    )

    easemetric = st.sidebar.slider(
    "Ease",
    min_value=0,
    max_value=10,
    value=7,
    step=1,
    help="Set Ease value to understand how CLV changes with Ease",
    )

    effectivenessmetric = st.sidebar.slider(
    "Effectiveness",
    min_value=0,
    max_value=10,
    value=8,
    step=1,
    help="Set Effectiveness Metric to understand how CLV changes with Effectiveness",
    )

    st.sidebar.subheader("Design Win to Deal Win Metrics")
    dealwinmetric = st.sidebar.slider(
    "Design Win to Deal Win",
    min_value=0,
    max_value=100,
    value=30,
    step=10,
    help="Set your proportion of design win to deal win ratio",
    )

    st.markdown("Illustrative Values!")
    data=pd.read_excel('df.xlsx')
    #fig1=px.box(data,x='Country_Brand_Segment',y=['CLV4','CLV6','CLV12'],)
    #st.plotly_chart(fig1)
    
    dat1 = data[data['Country_Brand_Segment']=='SG_Pink_CCG']
    #a = dat1['CLV4'][0]     
    #b = dat1['CLV6'][0]
    #c = dat1['CLV12'][0]
    a=(1000272.3*(npsmultiplier)+11001.001*(customerindexmetric)+1002.2*(easemetric)+103.4*(trustmetric)+10022.9*(effectivenessmetric)+10002.9*(dealwinmetric))*1.8/0.0185
    b=(5000514.2*(npsmultiplier)+12345.01*(customerindexmetric)+ 2234.75*(easemetric) + 234.7*(trustmetric)+ 12456.1*(effectivenessmetric)+20006.1*(dealwinmetric))*1.8/0.0185
    c=(12034581.7*(npsmultiplier)+110077.2*(customerindexmetric)+725273*(easemetric)+415.2*(trustmetric)+7841.9*(effectivenessmetric)+24063.9*(dealwinmetric))*1.8/0.0185
    #b=((1000272.3*2.6*npsmultiplier)+(1001.001*1.2*customerindexmetric)+(1002.2*2.2*easemetric)+(103.4*1.6*trustmetric)+(10022.9*2.5*effectivenessmetric)+(1002.9*5.2*dealwinmetric))*100
    #c=((1000272.3*5.6*npsmultiplier)+(1001.001*2.6*customerindexmetric)+(1002.2*5.2*easemetric)+(103.4*3.6*trustmetric)+(10022.9*5.5*effectivenessmetric)+(1002.9*7.2*dealwinmetric))*100
    
    
    diction = {}
    diction = {'x':['CLV4','CLV6','CLV12']}
    diction['y'] = [a,b,c]
    new_df = pd.DataFrame.from_dict(diction)

    fig2 = px.line(new_df, x="x", y="y",width=20, height=10,
                labels={
                        "x": "CLV Trend Over Months",
                        "y": "CLV Amount Over Months"},
                        title="CLV Trend for Account 1")
    fig2.update_xaxes(title_font_family="Calibri")
    fig2.update_yaxes(title_font_family="Calibri")
    #st.plotly_chart(fig2)

    dat2 = data[data['Country_Brand_Segment']=='CN_Pink_CCG']
    #a = (dat2['CLV4'][1]*((npsmultiplier*0.2)+(customerindexmetric*0.2)+(easemetric*0.3)+(trustmetric*0.4)+(effectivenessmetric*0.1)+(dealwinmetric*1.2)))/19
    #b = (dat2['CLV6'][1]*((npsmultiplier*0.6)+(customerindexmetric*0.5)+(easemetric*0.4)+(trustmetric*0.5)+(effectivenessmetric*0.5)+(dealwinmetric*1.2)))/19
    #c = (dat2['CLV12'][1]*((npsmultiplier*0.8)+(customerindexmetric*0.9)+(easemetric*0.5)+(trustmetric*0.6)+(effectivenessmetric*0.9)+(dealwinmetric*1.2)))/19
    a=((1000272.3*(npsmultiplier)+11001.001*(customerindexmetric)+1002.2*(easemetric)+103.4*(trustmetric)+10022.9*(effectivenessmetric)+10002.9*(dealwinmetric))*1000)/9/16.17
    b=((5000514.2*(npsmultiplier)+12345.01*(customerindexmetric)+ 2234.75*(easemetric) + 234.7*(trustmetric)+ 12456.1*(effectivenessmetric)+20006.1*(dealwinmetric))*1000)/9/16.17
    c=((12034581.7*(npsmultiplier)+110077.2*(customerindexmetric)+725273*(easemetric)+415.2*(trustmetric)+7841.9*(effectivenessmetric)+24063.9*(dealwinmetric))*1000)/9/16.17

    diction = {}
    diction = {'x':['CLV4','CLV6','CLV12']}
    diction['y'] = [a,b,c]
    new_df = pd.DataFrame.from_dict(diction)

    fig3 = px.line(new_df, x="x", y="y",width=20, height=10,
                labels={
                        "x": "CLV Trend Over Months",
                        "y": "CLV Amount Over Months"},
                        title="CLV Trend for Account 2")
    fig3.update_xaxes(title_font_family="Calibri")
    fig3.update_yaxes(title_font_family="Calibri")
    #st.plotly_chart(fig3)

    dat3 = data[data['Country_Brand_Segment']=='PL_Pink_CCG']
    #a = dat3['CLV4'][2]
    #b = dat3['CLV6'][2]
    #c = dat3['CLV12'][2]

    a=((1000272.3*(npsmultiplier)+11001.001*(customerindexmetric)+1002.2*(easemetric)+103.4*(trustmetric)+10022.9*(effectivenessmetric)+10002.9*(dealwinmetric))*1000)/11/18.59
    b=((5000514.2*(npsmultiplier)+12345.01*(customerindexmetric)+ 2234.75*(easemetric) + 234.7*(trustmetric)+ 12456.1*(effectivenessmetric)+20006.1*(dealwinmetric))*1000)/11/18.59
    c=((12034581.7*(npsmultiplier)+110077.2*(customerindexmetric)+725273*(easemetric)+415.2*(trustmetric)+7841.9*(effectivenessmetric)+24063.9*(dealwinmetric))*1000)/11/18.59

    diction = {}
    diction = {'x':['CLV4','CLV6','CLV12']}
    diction['y'] = [a,b,c]
    new_df = pd.DataFrame.from_dict(diction)

    fig4 = px.line(new_df, x="x", y="y",width=20, height=10,
                labels={
                        "x": "CLV Trend Over Months",
                        "y": "CLV Amount Over Months"},
                        title="CLV Trend for Account 3")
    fig4.update_xaxes(title_font_family="Calibri")
    fig4.update_yaxes(title_font_family="Calibri")

    
    dat4 = data[data['Country_Brand_Segment']=='HK_Pink_CCG']
    #a = dat4['CLV4'][3]
    #b = dat4['CLV6'][3]
    #c = dat4['CLV12'][3]

    a=((1000272.3*(npsmultiplier)+11001.001*(customerindexmetric)+1002.2*(easemetric)+103.4*(trustmetric)+10022.9*(effectivenessmetric)+10002.9*(dealwinmetric))*1000)/7.5/29.30
    b=((5000514.2*(npsmultiplier)+12345.01*(customerindexmetric)+ 2234.75*(easemetric) + 234.7*(trustmetric)+ 12456.1*(effectivenessmetric)+20006.1*(dealwinmetric))*1000)/7.5/29.30
    c=((12034581.7*(npsmultiplier)+110077.2*(customerindexmetric)+725273*(easemetric)+415.2*(trustmetric)+7841.9*(effectivenessmetric)+24063.9*(dealwinmetric))*1000)/7.5/29.30

    diction = {}
    diction = {'x':['CLV4','CLV6','CLV12']}
    diction['y'] = [a,b,c]
    new_df = pd.DataFrame.from_dict(diction)

    fig5 = px.line(new_df, x="x", y="y",width=20, height=10,
                labels={
                        "x": "CLV Trend Over Months",
                        "y": "CLV Amount Over Months"},
                        title="CLV Trend for Account 4")
    fig5.update_xaxes(title_font_family="Calibri")
    fig5.update_yaxes(title_font_family="Calibri")   

    dat5 = data[data['Country_Brand_Segment']=='US_Pink_CCG']
    #a = dat5['CLV4'][4]
    #b = dat5['CLV6'][4]
    #c = dat5['CLV12'][4]

    a=((1000272.3*(npsmultiplier)+11001.001*(customerindexmetric)+1002.2*(easemetric)+103.4*(trustmetric)+10022.9*(effectivenessmetric)+10002.9*(dealwinmetric))*1000)/17/24.53
    b=((5000514.2*(npsmultiplier)+12345.01*(customerindexmetric)+ 2234.75*(easemetric) + 234.7*(trustmetric)+ 12456.1*(effectivenessmetric)+20006.1*(dealwinmetric))*1000)/17/24.53
    c=((12034581.7*(npsmultiplier)+110077.2*(customerindexmetric)+725273*(easemetric)+415.2*(trustmetric)+7841.9*(effectivenessmetric)+24063.9*(dealwinmetric))*1000)/17/24.53

    diction = {}
    diction = {'x':['CLV4','CLV6','CLV12']}
    diction['y'] = [a,b,c]
    new_df = pd.DataFrame.from_dict(diction)

    fig6 = px.line(new_df, x="x", y="y",width=20, height=10,
                labels={
                        "x": "CLV Trend Over Months",
                        "y": "CLV Amount Over Months"},
                        title="CLV Trend for Account 5")
    fig6.update_xaxes(title_font_family="Calibri")
    fig6.update_yaxes(title_font_family="Calibri")   

    dat6 = data[data['Country_Brand_Segment']=='MY_Pink_CCG']
    #a = dat6['CLV4'][5]
    #b = dat6['CLV6'][5]
    #c = dat6['CLV12'][5]

    a=((1000272.3*(npsmultiplier)+11001.001*(customerindexmetric)+1002.2*(easemetric)+103.4*(trustmetric)+10022.9*(effectivenessmetric)+10002.9*(dealwinmetric))*1000)/18/23.25
    b=((5000514.2*(npsmultiplier)+12345.01*(customerindexmetric)+ 2234.75*(easemetric) + 234.7*(trustmetric)+ 12456.1*(effectivenessmetric)+20006.1*(dealwinmetric))*1000)/18/23.25
    c=((12034581.7*(npsmultiplier)+110077.2*(customerindexmetric)+725273*(easemetric)+415.2*(trustmetric)+7841.9*(effectivenessmetric)+24063.9*(dealwinmetric))*1000)/18/23.25


    diction = {}
    diction = {'x':['CLV4','CLV6','CLV12']}
    diction['y'] = [a,b,c]
    new_df = pd.DataFrame.from_dict(diction)

    fig7 = px.line(new_df, x="x", y="y",width=20, height=10,
                labels={
                        "x": "CLV Trend Over Months",
                        "y": "CLV Amount Over Months"},
                        title="CLV Trend for Account 6")
    fig7.update_xaxes(title_font_family="Calibri")
    fig7.update_yaxes(title_font_family="Calibri")

    dat7 = data[data['Country_Brand_Segment']=='IN_Pink_CCG']
    #a = dat7['CLV4'][6]
    #b = dat7['CLV6'][6]
    #c = dat7['CLV12'][6]
    
    a=((1000272.3*(npsmultiplier)+11001.001*(customerindexmetric)+1002.2*(easemetric)+103.4*(trustmetric)+10022.9*(effectivenessmetric)+10002.9*(dealwinmetric))*1000)/40/27.63
    b=((5000514.2*(npsmultiplier)+12345.01*(customerindexmetric)+ 2234.75*(easemetric) + 234.7*(trustmetric)+ 12456.1*(effectivenessmetric)+20006.1*(dealwinmetric))*1000)/40/27.63
    c=((12034581.7*(npsmultiplier)+110077.2*(customerindexmetric)+725273*(easemetric)+415.2*(trustmetric)+7841.9*(effectivenessmetric)+24063.9*(dealwinmetric))*1000)/40/27.63

    
    diction = {}
    diction = {'x':['CLV4','CLV6','CLV12']}
    diction['y'] = [a,b,c]
    new_df = pd.DataFrame.from_dict(diction)

    fig8 = px.line(new_df, x="x", y="y",width=20, height=10,
                labels={
                        "x": "CLV Trend Over Months",
                        "y": "CLV Amount Over Months"},
                        title="CLV Trend for Account 7")
    fig8.update_xaxes(title_font_family="Calibri")
    fig8.update_yaxes(title_font_family="Calibri")

    dat8 = data[data['Country_Brand_Segment']=='BR_Pink_CCG']
    #a = dat8['CLV4'][7]
    #b = dat8['CLV6'][7]
    #c = dat8['CLV12'][7]
    
    a=((1000272.3*(npsmultiplier)+11001.001*(customerindexmetric)+1002.2*(easemetric)+103.4*(trustmetric)+10022.9*(effectivenessmetric)+10002.9*(dealwinmetric))*1000)/42/30.62
    b=((5000514.2*(npsmultiplier)+12345.01*(customerindexmetric)+ 2234.75*(easemetric) + 234.7*(trustmetric)+ 12456.1*(effectivenessmetric)+20006.1*(dealwinmetric))*1000)/42/30.62
    c=((12034581.7*(npsmultiplier)+110077.2*(customerindexmetric)+725273*(easemetric)+415.2*(trustmetric)+7841.9*(effectivenessmetric)+24063.9*(dealwinmetric))*1000)/42/30.62


    diction = {}
    diction = {'x':['CLV4','CLV6','CLV12']}
    diction['y'] = [a,b,c]
    new_df = pd.DataFrame.from_dict(diction)

    fig9 = px.line(new_df, x="x", y="y",width=20, height=10,
                labels={
                        "x": "CLV Trend Over Months",
                        "y": "CLV Amount Over Months"},
                        title="CLV Trend for Account 8")
    fig9.update_xaxes(title_font_family="Calibri")
    fig9.update_yaxes(title_font_family="Calibri")


    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig2)
        st.plotly_chart(fig4)
        st.plotly_chart(fig6)
        st.plotly_chart(fig8)
    with col2:
        st.plotly_chart(fig3)
        st.plotly_chart(fig5)
        st.plotly_chart(fig7)
        st.plotly_chart(fig9)



    