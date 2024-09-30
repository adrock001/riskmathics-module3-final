import streamlit as st
import pandas as pd
from datetime import timedelta


@st.cache_data
def load_data():
    # url = "https://github.com/adrock001/riskmathics-module3-final/blob/main/sales_data_2000.csv?raw=true"
    data = pd.read_csv("DataSet/Datos_proyecto_Limpio.csv")
    return data


df = load_data()

# Agrego los indicadores adicionales
# El ratio de liquidez es Current_Ratio
# El ratio de Deuda a Patrimonio es Debt_to_Equity_Ratio
# Cobertura de Gastos Financieros es Interest_Coverage_Ratio

# !!!Nota: No se calcularon los indicadores por que ya vienen en el dataset!!!
# Incluso se utilizaron en el relleno de nulos de la parte de la limpieza de datos

st.title("Analisis de Solvencia")

st.sidebar.header("Filtros")

st.header("Muestra de la informacion")
st.write(df.sample(5))

st.header("Filtros")

industry = st.selectbox("Ramo", df["Industry"].unique())
countries = st.multiselect("Paises", df["Country"].unique())
sizes = st.multiselect("Tamaño", df["Company_Size"].unique())

if industry:
    df = df[df["Industry"] == industry]
if countries:
    df = df[df["Country"].isin(countries)]
if sizes:
    df = df[df["Company_Size"].isin(sizes)]

df["Company_ID"] = df["Company_ID"] + " (" + df["Country"] + ")"

st.header("Graficas")

st.header("Ratio de Liquidez")
st.bar_chart(
    df, y="Current_Ratio", x="Company_ID", color="Company_Size", horizontal=True)
st.header("Ratio de Deuda a Patrimonio")
st.bar_chart(
    df, y="Debt_to_Equity_Ratio", x="Company_ID", color="Company_Size", horizontal=True)
st.header("Cobertura de Gastos Financieros")
st.bar_chart(
    df, y="Interest_Coverage_Ratio",x="Company_ID",color="Company_Size", horizontal=True)