import streamlit as st
from Predict_page import show_predict_page 
from explore_page import show_explore_page

page = st.sidebar.selectbox('Explore or Estimate',('Explore', 'Estimate'))

if page == 'Estimate':
    show_predict_page()

else:
    show_explore_page()





