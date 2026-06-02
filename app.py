import streamlit as st 
from datetime import datetime


def mostrar_tempo_juntos(data_inicio):
    agora = datetime.now()
    tempo = agora - data_inicio

    dias = tempo.days
    horas = tempo.seconds // 3600
    minutos = (tempo.seconds % 3600) // 60
    segundos = tempo.seconds % 60

    st.header("Estamos juntos há  ❤️")


    st.markdown(f"""
    ### ⏳ {dias} dias
    ### {horas} horas
    ### {minutos} minutos
    ### {segundos} segundos
    """)


st.set_page_config(
    page_title="Nossa História ❤️",
    page_icon="❤️",
    layout="wide"
)

co11, co12, co13 = st.columns([1, 3, 1])

with co12:
    st.title('❤️ Be & Lala ❤️')

    inicio = datetime(2023, 11, 25)

    mostrar_tempo_juntos(inicio)

    st.image('foto_juntos.jpg', width=700)

    st.header('Nossa História')

    if st.button('Clique aqui ❤️ '):
        st.balloons()
        st.success('Eu te amoooo infinitamenteeeeee ❤️ ❤️ ❤️ ❤️ ')

#teste para streamlit