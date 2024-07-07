import streamlit as st
import pandas as pd
import numpy as np

# 标题和文本
st.title('我的第一个 Streamlit 应用')
st.write("这是一个简单的示例应用")

# 创建数据框
df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

# 显示数据框
st.write(df)

# 添加交互组件
if st.button('显示图表'):
    st.line_chart(df)