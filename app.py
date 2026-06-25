import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title='Rick & Morty API Dataset',
    page_icon='👽',
    layout='wide'
)

characters = st.Page('./pages/characters.py', title='Characters', icon='🦹')
location = st.Page('./pages/location.py', title='Location', icon='📍')
cards = st.Page('./pages/cards.py', title='Cards', icon='📇')

pagination = st.navigation(
    [characters, location, cards],
    position='sidebar'
)

pagination.run()

