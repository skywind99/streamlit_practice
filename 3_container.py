import streamlit as st

con1 = st.container(border= True)
con2 = st.container(border=True )
with con1:
    btn = st.button("눌러보세요")
    if(btn):
        st.markdown("아무일도 없어요")
with con2:
    btn = st.button("누르면 안돼요")
    if(btn):
        st.markdown("아무일도 없어요")
