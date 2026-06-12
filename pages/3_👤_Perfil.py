import streamlit as st
import requests

st.set_page_config(page_title="Meu Perfil", page_icon="👤", layout="wide")

if "usuario_logado" not in st.session_state or not st.session_state["usuario_logado"]:
    st.error("🔒 Sua sessão expirou ou você não está logado.")
    if st.button("Fazer Login Novamente", type="primary"): st.switch_page("app.py")
    st.stop()

cabecalho = {"Authorization": f"Bearer {st.session_state['token_xano']}"}

# PRINT 4: Lógica de persistência em memória segura para Curso e Instituição
if "curso" not in st.session_state:
    st.session_state["curso"] = "Análise e Desenvolvimento de Sistemas"
if "instituicao" not in st.session_state:
    st.session_state["instituicao"] = "Faculdade Impacta de Tecnologia"

css_e_logo = """
    <style>
        [data-testid="stSidebarNav"] { padding-top: 4rem !important; }
        .logo-fixa { position: fixed; top: 1.5rem; left: 1.5rem; display: flex; align-items: center; gap: 10px; z-index: 99999; }
        [data-testid="stSidebarNavItems"] li div:hover { background-color: rgba(230, 57, 70, 0.15) !important; }
        [data-testid="stSidebarNavItems"] li div[data-testid="stSidebarNavLinkActive"] { background-color: rgba(230, 57, 70, 0.3) !important; border-left: 4px solid #E63946; }
        [data-testid="stSidebarNavItems"] li:first-child a span { display: none; }
        [data-testid="stSidebarNavItems"] li:first-child a::after { content: "📊 Dashboard"; color: #E63946; font-weight: 800; font-size: 16px; letter-spacing: 0.5px; }
    </style>
    <div class="logo-fixa">
        <div style="background-color: #E63946; color: white; border-radius: 8px; padding: 5px 10px; font-weight: 900; font-size: 18px; box-shadow: 0 0 10px rgba(230,57,70,0.5);">ET</div>
        <div style="font-size: 22px; font-weight: 800; color: #F1F1F1; letter-spacing: -1px;">Edu<span style="color: #E63946;">Track</span></div>
    </div>
"""
with st.sidebar: st.markdown(css_e_logo, unsafe_allow_html=True)

# PRINT 4: Modal estendido para permitir editar Curso e Instituição de forma limpa
@st.dialog("✏️ Editar Perfil")
def modal_editar_perfil(nome_atual, email_atual):
    with st.form("form_edit_profile"):
        novo_nome = st.text_input("Nome Completo", value=nome_atual)
        novo_email = st.text_input("E-mail", value=email_atual)
        novo_curso = st.text_input("Curso", value=st.session_state["curso"])
        nova_inst = st.text_input("Instituição", value=st.session_state["instituicao"])
        
        if st.form_submit_button("Salvar Alterações", type="primary"):
            st.session_state["curso"] = novo_curso
            st.session_state["instituicao"] = nova_inst
            res = requests.post("https://x8ki-letl-twmt.n7.xano.io/api:wwEG4bZX/auth/me", json={"name": novo_nome, "email": novo_email}, headers=cabecalho)
            if res.status_code == 200: 
                st.rerun()

st.markdown("<h1 style='border-bottom: 2px solid #E63946; padding-bottom: 10px;'>Meu Workspace Acadêmico</h1>", unsafe_allow_html=True)

try:
    resposta = requests.get("https://x8ki-letl-twmt.n7.xano.io/api:wwEG4bZX/auth/me", headers=cabecalho)
    if resposta.status_code == 200:
        dados_usuario = resposta.json()
        nome = dados_usuario.get("name", "Usuário")
        email = dados_usuario.get("email", "Não informado")
        
        col_avatar, col_info, col_vazia = st.columns([3, 5, 2])
        
        with col_avatar:
            # PRINT 2 e 3 FILTRADOS: Removido use_container_width e fixado largura para travar o erro de 2026
            if 'foto_perfil' in st.session_state:
                st.image(st.session_state['foto_perfil'], width=240)
            else:
                st.markdown(f"<div style='background-color: #E63946; color: white; border-radius: 8px; width: 240px; height: 240px; display: flex; align-items: center; justify-content: center; font-size: 70px; font-weight: bold; box-shadow: 0 10px 20px rgba(230,57,70,0.3);'>{nome[0].upper()}</div><br>", unsafe_allow_html=True)
            
            foto = st.file_uploader("Alterar Foto", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
            if foto:
                st.session_state['foto_perfil'] = foto.getvalue()
                st.rerun()

        with col_info:
            st.subheader("Informações Pessoais")
            st.write(f"**👤 Nome:** {nome}")
            st.write(f"**📧 E-mail:** {email}")
            st.write("")
            if st.button("✏️ Editar Dados Cadastrais"): modal_editar_perfil(nome, email)
            
    else: st.error("Erro ao carregar dados.")
except Exception as e: st.error(f"Erro de conexão: {e}")