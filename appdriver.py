import altair as alt
import copy
import numpy as np
import pandas as pd
import scipy.stats as stats
import streamlit as st
from app import mainapp
from dataset import datasetdisplay

st.set_page_config(layout="wide")
page = st.sidebar.selectbox("What Page Would You Like To See", ("Dataset", "CLV Simulator"))

if page == 'Dataset':
    datasetdisplay()
if page == 'CLV Simulator':
    mainapp()
