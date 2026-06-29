import streamlit as st 

import pandas as pd

import plotly.express as px



load_data = pd.read_csv('vehicles_us.csv')



mil_vs_price = px.scatter(load_data, x='odometer', y='price', title='Price VS Milage')

mil_vs_price.update_layout(xaxis_title='Vehicle Milage', yaxis_title='Vehicle Price')

st.plotly_chart(mil_vs_price)



v_type = px.histogram(load_data, x='type', title='Count Of Vehicle Types')

v_type.update_layout(

    xaxis_title='Vehicle Type',

    yaxis_title='Number of listings')

show_chart = st.checkbox('Show Histogram')

if show_chart:
    st.plotly_chart(v_type)