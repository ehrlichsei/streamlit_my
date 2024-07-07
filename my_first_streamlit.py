import streamlit as st

from my_text.my_text import run_text

from my_column.my_table_visualizer import run_table_visualizer
from my_column.my_image_column import run_image_column
from my_column.my_datetime_column import run_datetime_column

from my_chart.my_map import run_map

# from my_input.my_form import run_form
from my_input.my_button import run_button

if __name__ == '__main__':
    run_text()

    run_datetime_column()
    run_image_column()
    run_table_visualizer()

    run_map()

    run_button()