import streamlit as st
import requests

st.set_page_config(page_title="Perfil", page_icon="👤")

# Proteção de Rota com Botão de Redirecionamento 🚀
if "usuario_logado" not in st.session_state or not st.session_state["usuario_logado"]:
    st.warning("🔒 Você precisa fazer login para acessar esta página.")
    if st.button("Ir para o Login", type="primary"):
        st.switch_page("app.py") # Comando mágico que joga o usuário para a Home
    st.stop()

st.title("Meu Perfil Acadêmico")
st.markdown("---")

url_me = "https://x8ki-letl-twmt.n7.xano.io/api:wwEG4bZX/auth/me"

headers = {
    "Authorization": f"Bearer {st.session_state['token_xano']}"
}

nome_usuario = "Carregando..."
email_usuario = "Carregando..."

try:
    resposta = requests.get(url_me, headers=headers)
    
    if resposta.status_code == 200:
        dados_usuario = resposta.json()
        nome_usuario = dados_usuario.get("name", "Usuário Não Encontrado")
        email_usuario = dados_usuario.get("email", "Sem e-mail")
    else:
        # AGORA O ERRO VAI NOS DIZER EXATAMENTE O MOTIVO
        st.error(f"Erro {resposta.status_code} no Xano: {resposta.text}")
except Exception as e:
    st.error(f"Erro de conexão: {e}")

# ==========================================
# 2. MONTANDO O VISUAL DO PERFIL
# ==========================================
col_foto, col_info = st.columns([1, 2])

with col_foto:
    inicial = nome_usuario[0].upper() if nome_usuario != "Carregando..." else "U"
    
    st.markdown(f"""
        <div style="background-color: #E63946; width: 150px; height: 150px; border-radius: 50%; 
                    display: flex; align-items: center; justify-content: center; 
                    color: white; font-size: 65px; font-weight: bold; margin: auto; 
                    box-shadow: 0px 4px 6px rgba(0,0,0,0.3);">
            {inicial}
        </div>
    """, unsafe_allow_html=True)

with col_info:
    st.subheader("Informações Pessoais")
    st.write(f"**Nome:** {nome_usuario}")
    st.write(f"**E-mail:** {email_usuario}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.subheader("Dados Acadêmicos")
    st.write("**Curso:** Análise e Desenvolvimento de Sistemas")
    st.write("**Instituição:** Faculdade Impacta de Tecnologia")

st.markdown("---")
st.info("💡 Suas informações pessoais são gerenciadas de forma segura e protegidas por autenticação criptografada (Token JWT).")