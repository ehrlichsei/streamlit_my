from datetime import datetime
import pandas as pd
import streamlit as st


def run_text():
    st.markdown("# run_text")
    st.divider()
    # 标题和文本
    st.title('我的第一个 Streamlit 应用')
    st.write("这是一个简单的示例应用")
    st.markdown("Hello, **world!**")
    st.markdown("## 这是一个markdown标题")
    st.caption('这是一段说明')
    code = '''def hello():
        print("Hello, Streamlit!")'''
    st.code(code, language='python')
    st.divider() 
    st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
        ''')