import streamlit as st 
from datetime import datetime

st.set_page_config(
    page_title="Nossa História ❤️",
    page_icon="❤️",
    layout="wide"
)

st.title('❤️ Be & Lala ❤️')

inicio = datetime(2023, 11, 25)

agora = datetime.now()
tempo = agora - inicio 

st.header('Estamos juntos há:')
st.writer(f'{tempo.days} dias')

st.image('fotos/foto1.jpg')

st.header('Nossa História')

if st.button('Clique aqui ❤️ '):
    st.balloons()
    st.success('Eu te amoooo infinitamenteeeeee ❤️ ❤️ ❤️ ❤️ ')