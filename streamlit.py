import streamlit as st

## Title
st.title('Streamlit Tutorial')
## Header/Subheader
st.header('This is header')
st.subheader('This is subheader')
## Text
st.text('Hello Streamlit! 이 글은 튜토리얼 입니다.')

## Markdown syntax
st.markdown("# This is a Markdown title")
st.markdown("## This is a Markdown header")
st.markdown("### This is a Markdown subheader")
st.markdown("- item 1\n"
            "   - item 1.1\n"
            "   - item 1.2\n"
            "- item 2\n"
            "- item 3")
st.markdown("1. item 1\n"
            "   1. item 1.1\n"
            "   2. item 1.2\n"
            "2. item 2\n"
            "3. item 3")