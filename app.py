'''
Description: 
Author: lunyang
Github: 
Date: 2022-02-02 14:29:24
LastEditors: lunyang
LastEditTime: 2022-02-02 17:29:36
'''
import streamlit as st
from multipage import MultiPage
from pages import home, machine_learning

st.set_page_config(page_title="ML", page_icon=":tiger:", layout="wide")
st.title('Machine Learning Application')

app = MultiPage()

# add applications
app.add_page('Home', home.app)
app.add_page('Machine Learning', machine_learning.app)

# Run application
if __name__ == '__main__':
    app.run()