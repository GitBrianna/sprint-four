import streamlit as st 

import pandas as pd

import plotly.express as px



load_data = pd.read_csv('vehicles_us.csv')

st.header('How long were vehicles listed before vehicle was sold?')

ls_days = px.histogram(load_data, x='days_listed', title='Duration Of Vehicles Listed', nbins=50)
ls_days.update_layout(xaxis_title='Number Of Days Listed', yaxis_title='Number Of Vehicles')
st.plotly_chart(ls_days)

st.header('Does vehicle year affect price?')

year_vs_price = px.scatter(load_data, x='model_year', y='price', title='Price VS Model Year')
year_vs_price.update_layout(xaxis_title='Vehicle Year', yaxis_title='Vehicle Price')
st.plotly_chart(year_vs_price)

st.header('Does vehicle mileage affect price?')

mil_vs_price = px.scatter(load_data, x='odometer', y='price', title='Price VS Mileage')

mil_vs_price.update_layout(xaxis_title='Vehicle Mileage', yaxis_title='Vehicle Price')

st.plotly_chart(mil_vs_price)


st.header('Select a vehicle type')

vehicle_type = st.selectbox(
    "Choose a vehicle type:", 
    sorted(load_data['type'].unique()))

filtered_vtype = load_data[load_data['type'] == vehicle_type]

st.header("Condition distribution for selected vehicle type")

cond_chart = px.histogram(
    filtered_vtype,
    x="condition",
    title=f"Condition distribution for {vehicle_type}"
)

st.plotly_chart(cond_chart)