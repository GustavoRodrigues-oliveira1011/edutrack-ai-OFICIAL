import streamlit as st

# Configuração principal da página (Aba do navegador)
st.set_page_config(
    page_title="EduTrack - Home",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Bem-vindo ao EduTrack!")
st.markdown("---")

st.write("Este é o seu Dashboard principal. Use o menu lateral para navegar entre as páginas do aplicativo.")

# Um pequeno exemplo de como um Dashboard ficaria
st.subheader("Resumo Rápido")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Disciplinas Cadastradas", value="2") # Valores fixos (Mockup) por enquanto
    
with col2:
    st.metric(label="Tarefas Pendentes", value="1")
    
with col3:
    st.metric(label="Tarefas Concluídas", value="5")

st.markdown("---")
st.info("👈 Selecione **Disciplinas** ou **Tarefas** no menu à esquerda para começar a gerenciar seus estudos!")