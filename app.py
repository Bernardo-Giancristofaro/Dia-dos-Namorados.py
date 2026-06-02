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
st.write(f'{tempo.days} dias')

st.image('foto_juntos.jpg', width=600)

st.header('Nossa História')

if st.button('Clique aqui ❤️ '):
    st.balloons()
    st.success('Eu te amoooo infinitamenteeeeee ❤️ ❤️ ❤️ ❤️ ')

#teste para streamlit