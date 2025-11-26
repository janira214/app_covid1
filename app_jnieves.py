import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

####################
## ajustar el layout
#################### 

st.set_page_config(layout="wide")

##################
## tamaño del plot
################## 

fig, ax = plt.subplots()

#########
## titulo
######### 

col1, col2, col3 = st.columns([1,3,1])

col1.image("COMP3005/logouprh.png", width = 150)

col2.title("Datos de Covid - Variante Omicrón")

col3.image("COMP3005/covid.png", width = 150)

##############################################
## esto es para que salga una linea horizontal
############################################## 

st.divider()

#################
## datos de covid 
################# 

df_covid = pd.read_csv("https://raw.githubusercontent.com/elioramosweb/archivo_datos/main/datos_diarios-2022-03-22_10_20_15.csv",parse_dates=['date'])

########################
## seleccionar una columna
########################

nombres = list(df_covid.columns)[1:]

columna = st.sidebar.selectbox("Columan de Interés:", nombres)

################################
# indicar si se quiere suavizar
##############################

suavizado = st.sidebar.checkbox('Suavizado')

#####################################
# indicar si se quiere mostrar tabla
####################################

tabla = st.sidebar.checkbox('Mostrar Datos')

df_covid.plot(x='date', y= columna, ax=ax, 
              xlabel= 'Fecha',
              ylabel= columna)

col1, col2 = st.columns(2)

if suavizado:
    ventana = st.sidebar.slider("Ventana de suavizado [días]", 
                                1,15,7)
    
    df_rolling = df_covid[columna]. rolling(ventana, center = True). mean()
    df_covid[columna+"_rolling"] = df_rolling
    df_covid.plot(x="date", y=columna+"_rolling", ax=ax)
    st.sidebar.divider()

col1.pyplot(fig) 

if tabla:
        df_covid["date"] = df_covid["date"].dt.strftime("%d-%b-%Y")
        df_filtrado = df_covid[["date", columna]]
        col2.write(df_filtrado)


st.sidebar.markdown("""Aplicación desarrollada por: <br> Janira Nieves <br> 
                    Comp3005<br> Universidad de Puerto Rico en Humacao""",
                    unsafe_allow_html=True)

