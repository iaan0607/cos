import streamlit as st
import pandas as pd
import numpy as np

st.title('portpolio')

tab1,tab2,tab3,tab4 = st.tabs(["Football","Basketball","Baseball","Boxing"])

with tab1:
  st.header("Football")
with tab2:
  st.header("Basketball")
with tab3:
  st.header("Baseball")
with tab4:
  st.header("Boxing")

 
