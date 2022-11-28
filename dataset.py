import altair as alt
import copy
import numpy as np
import pandas as pd
import scipy.stats as stats
import streamlit as st

def datasetdisplay():
    alt.renderers.set_embed_options(scaleFactor=2)

    #st.set_page_config(layout="wide")

    #st.title("Design to WIN Simulator")
    col1, mid, col2 = st.columns([100,5,20])
    with col1:
        st.title('Intel - Design to win simulator for Brand: Pink')
    with col2:
        st.image('c5logo.jpg', width=150)
    st.markdown(
        "A Digital Twin Simulator for understanding effects of multiple variables on CLV analysis "
    )
    st.sidebar.title("Control Panel")
    left_col, middle_col, right_col = st.columns(3)

    tick_size = 12
    axis_title_size = 16

    data=pd.read_excel('regressormodeldata.xlsx')
    pinkdata=data.loc[data['Brand']=='Pink_CCG']

    st.sidebar.subheader("Inventory ")
    numberofaccounts = st.sidebar.number_input(
        "Number of Accounts",
        min_value=1,
        max_value=None,
        value=8,
        step=1,
        help="How many Accounts do you want to see the analysis for?",
    )
    st.table(data=pinkdata.head(numberofaccounts))