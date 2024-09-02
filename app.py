import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("db_vehicles.csv")

hist_button = st.button('Crear un histograma')
scatter_plot_button = st.button('Creae un gráfico de dispersión')

if hist_button:
    st.write('Crea un histograma del conjunto de datos')
    fig =  px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width= True)

if scatter_plot_button:
    st.write('Crea un diagrama de dispersión del conjunto de datos')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.scatter_chart(fig2, use_container_width= True)
