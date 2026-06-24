import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.graph_objects as go

st.set_page_config(
    page_title='Rick & Morty API Dataset',
    page_icon='👽',
    layout='wide'
)

st.title('Rick & Morty API Dataset')
st.write('Welcome to my website: explore Rick & Morty API data and visualizations here.')

@st.cache_data
def data_load():
    return pd.read_csv(Path(__file__).parent / '../data/dataset.csv')

df = data_load()

filters_col, data_col = st.columns([1, 4])

with filters_col:
    searching_name = st.text_input(
        'Searching name...', 
        width=200, 
        placeholder='Example: Morty Smith', 
        icon='🔎')
    
    status = st.radio(
        'Status:',
        ['All', 'Alive', 'Dead', 'unknown']
    )

    select_specie = st.multiselect(
        'Specie:',
        sorted(df['species'].dropna().unique())
    )

    select_type = st.multiselect(
        'Type:',
        sorted(df['type'].dropna().unique())
        )
    
    gender = st.radio(
        'Gender:',
        ['All', 'Male', 'Female']
    )

with data_col:

    df = df.copy()

    if searching_name:
        df = df[df["name"].str.contains(searching_name, case=False, na=False)]
    if status != 'All':
        df = df[df["status"] == status]
    if select_specie:
        df = df[df["species"].isin(select_specie)]
    if select_type:
        df = df[df["type"].isin(select_type)]
    if gender != 'All':
        df = df[df["gender"] == gender]
    
    st.dataframe(df, use_container_width=True)


