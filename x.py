import streamlit as st
import pandas as pd
import numpy as np

st.title('portpolio')
tab1,tab2 = st.tabs(["about me","sports"])

with tab1:
  st.header("i am human")
  
with tab2:
  st.header("sports")
  tab1,tab2,tab3,tab4 = st.tabs(["Football","Basketball","Baseball","Boxing"])

  with tab1:
    st.header("Football")
    taba,tabb,tabc,tabd = st.tabs(["EPL","LALIGA","SERIE A","K LEAGUE"])
    with taba:
      st.header("EPL")
    with tabb:
      st.header("LALIGA")
    with tabc:
      st.header("SERIE A")
    with tabd:
      st.header("K LEAGUE")
      
  with tab2:
    st.header("Basketball")
  with tab3:
    st.header("Baseball")
  with tab4:
    st.header("Boxing")

 
