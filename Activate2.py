#'''
#A01610903 José Rodrigo Hernández
#'''


#INSTRUCCIONES
#'''
#Desarrollar un código sobre la estructura de una aplicación web que
#contenga 3 controles (radio, selectbox y slider) sobre el proyecto de
#visualización de analítica de datos para WalMart USA.
#'''

#CODIGO ------------------------------------
#'''Librerias'''
import streamlit as st
import pandas as pd

#'''DataSet WalMart'''
dset_rute = 'https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'
data_WalM = pd.read_csv(dset_rute)
data_vis = data_WalM.copy()


#Basicos

def showDataset(data):
    return st.dataframe(data)

apptitle = 'Visualización de datos WalMart USA'
descrip = 'En esta WebApp se podrá visualizar datos sobre WalMart USA. Con el objetivo de visualizar y controlar los datos motrados de forma dinámica utilizando Streamlit.'
sidebar = st.sidebar

#'''Web'''
st.title(apptitle)
st.header(descrip)
st.markdown('___')

#'''Sidebar'''
sidebar.title('Controles')
sidebar.write('En esta sección se encuentran los controles para visualizar el dataset')

Categ= sidebar.selectbox('Categoría:', data_WalM['Category'].unique())

sidebar.markdown('___')


s_mode= sidebar.radio('Ship Mode:',data_WalM['Ship Mode'].unique())
sidebar.markdown('___')
optionals = sidebar.expander('Optional config',True)
disc_val = optionals.slider(
    'Select the Fare:',
    min_value= float(data_WalM['Discount'].min()),
    max_value= float(data_WalM['Discount'].max())

)


data_vis = data_WalM[(data_WalM['Ship Mode']==s_mode)&
    (data_WalM['Category']==Categ)&
    (data_WalM['Discount']==disc_val)
    ]
sidebar.markdown('___')

sidebar.header('Controles checkbox')
if sidebar.checkbox('Visualizar Dataset?'):
    showDataset(data_vis)

