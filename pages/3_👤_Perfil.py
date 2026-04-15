import streamlit as st

st.set_page_config(page_title="Perfil", page_icon="👤")
st.title("Meu Perfil")

st.info("As informações do perfil serão carregadas do Xano na Tarefa 13.")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://via.placeholder.com/150", caption="Foto do Usuário")

with col2:
    st.write("**Nome:** Usuário EduTrack")
    st.write("**E-mail:** usuario@edutrack.com")
    st.write("**Curso:** Innovation Lab")
