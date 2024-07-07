import streamlit as st
import pandas as pd
import numpy as np

def run_table_visualizer():
    st.markdown("# TableVisualizer")
    st.divider()

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