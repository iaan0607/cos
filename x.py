import streamlit as st
import pandas as pd
import numpy as np

st.title('portpolio')
tab1,tab2 = st.tabs(["about me","sports"])

with tab1:
  st.header("i am human")
  
with tab2:
  st.header("football")
  taba,tabb,tabc,tabd = st.tabs(["EPL","LALIGA","SERIE A","K LEAGUE"])
  with taba:
  st.header("EPL")
  with tabb:
  st.header("LALIGA")
  with tabc:
  st.header("SERIE A")
  with tabd:
  st.header("K LEAGUE")
      
 

 
