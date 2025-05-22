import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import openai
import os

# .env 파일에서 환경 변수 로드
load_dotenv()

llm = ChatOpenAI(
temperature=0.5)
mid_prompt = ChatPromptTemplate.from_messages([
       ("system","""    당신은 글쓰기 피드백 도우미입니다.    학생이 현재까지 쓴 글을 읽고, 더 나은 글을 쓸 수 있도록 쉬운 말로 피드백을 제공해주세요.    다만, 학생이 보고 베낄 수 있는 예시를 제공하지는 말아주세요.    초등학생들의 수준에 맞게 피드백을 제공해주세요.     """),    ("human","""     이름 : {name}, 현재까지 쓴 내용 : {input}     """)
       ])
final_prompt = ChatPromptTemplate.from_messages([
       ("system","""    당신은 글쓰기 피드백 도우미입니다.    학생이 현재까지 쓴 글을 읽고, 최소 1점에서 최대 5점까지 점수를 부여하세요.    학생이 더 나은 글을 쓸 수 있도록 마지막 피드백을 제공해주세요.     다음의 형식에 맞게 답변을 생성해줘. 
         점수
           - 점수 및 점수 배점 이유
        ### 피드백
           - 글이 더 나아지기 위한 피드백          
        """),    ("human","""     이름 : {name}, 현재까지 쓴 내용 : {input}     """)
       ])
mid_chain = (mid_prompt              | llm              | StrOutputParser())
final_chain = final_prompt | llm | StrOutputParser()

st.set_page_config(page_title= "✒️피드백 도우미", layout = "wide")
st.title("자동 피드백 도우미")
col1, col2 = st.columns(2)
with col1:
    container1= st.container(border=True)
    mid_feedback_btn = st.button("지금까지의 글 점검하기")
    container2= st.container(border=True)
    with container1:
        name = st.text_input("자신의 이름을 입력해 주세요")
        content = st.text_area("자신이 쓴 글을 입력해주세요.", height=200)
    with container2:
        st.markdown("#### 중간 피드백")
        if(mid_feedback_btn):
            result = mid_chain.invoke  ({
             "name":name,
             "input":content   
            })
            st.markdown(result)
with col2:
    final_feedback_btn =st.button("최종제출하기", type="primary",
    use_container_width =True)
    container=st.container(border=True, height = 500)
    with container:
        st.markdown("#### 최종 점수 및 피드백")
        if(final_feedback_btn):
            result = final_chain.invoke  ({
             "name":name,
             "input":content   
            })
            st.markdown(result)
