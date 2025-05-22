import streamlit as st

col1,col2 = st.columns(2)

with col1 : 
    con = st.container(border=True)
    with con:
            st.markdown("1번열")

with col2 : 
    st.markdown("2번열")