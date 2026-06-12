import streamlit as st
import requests

st.set_page_config(page_title="EduTrack | Dashboard", page_icon="🚀", layout="wide")

# ==========================================
# INICIALIZAÇÃO DE ESTADOS DE SESSÃO
# ==========================================
if "usuario_logado" not in st.session_state:
    st.session_state["usuario_logado"] = False
if "token_xano" not in st.session_state:
    st.session_state["token_xano"] = ""
if "aba_ativa" not in st.session_state:
    st.session_state["aba_ativa"] = 0

# ==========================================
# CSS AVANÇADO (CARDS, MENU E ESTILIZAÇÃO)
# ==========================================
css_dashboard = """
    <style>
        [data-testid="stSidebarNav"] { padding-top: 4rem !important; }
        .logo-fixa {
            position: fixed; top: 1.5rem; left: 1.5rem; display: flex; align-items: center; gap: 10px; z-index: 99999;
        }
        [data-testid="stSidebarNavItems"] li div:hover { background-color: rgba(230, 57, 70, 0.15) !important; }
        [data-testid="stSidebarNavItems"] li div[data-testid="stSidebarNavLinkActive"] {
            background-color: rgba(230, 57, 70, 0.3) !important; border-left: 4px solid #E63946;
        }
        [data-testid="stSidebarNavItems"] li:first-child a span { display: none; }
        [data-testid="stSidebarNavItems"] li:first-child a::after {
            content: "📊 Dashboard"; color: #E63946; font-weight: 800; font-size: 16px; letter-spacing: 0.5px;
        }
        
        .header-container {
            border-bottom: 2px solid #E63946; 
            padding-bottom: 15px;
            margin-bottom: 35px;
        }
        
        @media (max-width: 768px) { .logo-fixa { display: none; } }
    </style>
    <div class="logo-fixa">
        <div style="background-color: #E63946; color: white; border-radius: 8px; padding: 5px 10px; font-weight: 900; font-size: 18px; box-shadow: 0 0 10px rgba(230,57,70,0.5);">ET</div>
        <div style="font-size: 22px; font-weight: 800; color: #F1F1F1; letter-spacing: -1px;">Edu<span style="color: #E63946;">Track</span></div>
    </div>
"""

# ==========================================
# AMBIENTE LOGADO (DASHBOARD)
# ==========================================
if st.session_state["usuario_logado"]:
    with st.sidebar:
        st.markdown(css_dashboard, unsafe_allow_html=True)
        
    cabecalho = {"Authorization": f"Bearer {st.session_state['token_xano']}"}
    
    col_titulo, col_sync, col_logout = st.columns([7.5, 0.7, 1.8])
    with col_titulo:
        st.markdown("<div class='header-container'><h1>Visão Geral do Semestre</h1></div>", unsafe_allow_html=True)
    with col_sync:
        st.write("") 
        if st.button("🔄", key="btn_sync", type="primary", help="Sincronizar Dados"):
            st.rerun()
    with col_logout:
        st.write("") 
        if st.button("Sair (Logout)", type="secondary", use_container_width=True):
            st.session_state["usuario_logado"] = False
            st.session_state["token_xano"] = ""
            st.session_state["aba_ativa"] = 0
            st.rerun()
    
    total_disciplinas, total_tarefas, tarefas_pendentes, tarefas_concluidas, progresso = 0, 0, 0, 0, 0.0
    lista_tarefas = []
    
    try:
        res_sub = requests.get("https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/subjects", headers=cabecalho)
        if res_sub.status_code == 200: total_disciplinas = len(res_sub.json())
            
        res_task = requests.get("https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/academic_task", headers=cabecalho)
        if res_task.status_code == 200:
            lista_tarefas = res_task.json()
            total_tarefas = len(lista_tarefas)
            tarefas_pendentes = len([t for t in lista_tarefas if t.get("status") == "Pendente" or t.get("Status") == "Pendente"])
            tarefas_concluidas = len([t for t in lista_tarefas if t.get("status") == "Concluída" or t.get("Status") == "Concluída"])
            if total_tarefas > 0: progresso = (tarefas_concluidas / total_tarefas)
    except:
        st.warning("Aguardando conexão com o banco...")

    # Seção de Progresso com Barra Verde Customizada
    st.markdown("### 📈 Progresso de Conclusão")
    st.write(f"Você concluiu {int(progresso * 100)}% das suas tarefas cadastradas.")
    
    barra_html = f"""
    <div style="width: 100%; background-color: #2D333B; border-radius: 10px; margin-bottom: 25px;">
        <div style="width: {int(progresso * 100)}%; background-color: #06D6A0; padding: 6px 0; border-radius: 10px; text-align: center; color: #161B22; font-weight: bold; font-size: 14px; transition: width 0.5s ease-in-out;">
            {int(progresso * 100)}%
        </div>
    </div>
    """
    st.markdown(barra_html, unsafe_allow_html=True)

    cards_html = f"""
    <div style="display: flex; gap: 20px; flex-wrap: wrap; justify-content: space-between;">
        <div style="flex: 1; min-width: 200px; background: linear-gradient(145deg, #161B22, #0E1117); padding: 20px; border-radius: 12px; border-left: 5px solid #4361EE; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
            <p style="margin: 0; color: #8B949E; font-size: 14px; font-weight: bold;">📚 TOTAL DE DISCIPLINAS</p>
            <h1 style="margin: 10px 0 0 0; color: #FFFFFF; font-size: 36px;">{total_disciplinas}</h1>
        </div>
        <div style="flex: 1; min-width: 200px; background: linear-gradient(145deg, #161B22, #0E1117); padding: 20px; border-radius: 12px; border-left: 5px solid #F72585; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
            <p style="margin: 0; color: #8B949E; font-size: 14px; font-weight: bold;">📝 TOTAL DE TAREFAS</p>
            <h1 style="margin: 10px 0 0 0; color: #FFFFFF; font-size: 36px;">{total_tarefas}</h1>
        </div>
        <div style="flex: 1; min-width: 200px; background: linear-gradient(145deg, #161B22, #0E1117); padding: 20px; border-radius: 12px; border-left: 5px solid #FFD166; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
            <p style="margin: 0; color: #8B949E; font-size: 14px; font-weight: bold;">⏳ PENDENTES</p>
            <h1 style="margin: 10px 0 0 0; color: #FFD166; font-size: 36px;">{tarefas_pendentes}</h1>
        </div>
        <div style="flex: 1; min-width: 200px; background: linear-gradient(145deg, #161B22, #0E1117); padding: 20px; border-radius: 12px; border-left: 5px solid #06D6A0; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
            <p style="margin: 0; color: #8B949E; font-size: 14px; font-weight: bold;">✅ CONCLUÍDAS</p>
            <h1 style="margin: 10px 0 0 0; color: #06D6A0; font-size: 36px;">{tarefas_concluidas}</h1>
        </div>
    </div>
    """
    st.markdown(cards_html, unsafe_allow_html=True)

    # ==========================================
    # EXPORTAÇÃO DE RELATÓRIO (CSV)
    # ==========================================
    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("📊 Relatórios e Exportação de Dados"):
        st.write("Baixe o histórico completo de tarefas para análise em planilhas (Excel/Google Sheets).")
        
        if total_tarefas > 0:
            import pandas as pd
            df_tarefas = pd.DataFrame(lista_tarefas)
            if 'created_at' in df_tarefas.columns: df_tarefas.drop(columns=['created_at'], inplace=True)
            if 'user_id' in df_tarefas.columns: df_tarefas.drop(columns=['user_id'], inplace=True)
            
            csv = df_tarefas.to_csv(index=False).encode('utf-8')
            st.download_button(label="📥 Exportar Tarefas (CSV)", data=csv, file_name="relatorio_edutrack_tarefas.csv", mime="text/csv", type="primary")
        else:
            st.info("Cadastre algumas tarefas primeiro para gerar o relatório.")

# ==========================================
# AMBIENTE DESLOGADO (LOGIN E CADASTRO)
# ==========================================
else:
    # Oculta estritamente o menu lateral e as caixinhas/bolinhas redondas do st.radio
    st.markdown("""
        <style>
            [data-testid="stSidebar"] {display: none !important;}
            div[data-testid="stRadio"], .stRadio {display: none !important;}
        </style>
    """, unsafe_allow_html=True)
    
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        st.write("\n\n")
        st.markdown("""
        <div style="text-align: center; margin-bottom: 30px;">
            <span style="background-color: #E63946; color: white; border-radius: 10px; padding: 8px 15px; font-weight: 900; font-size: 30px; box-shadow: 0 0 15px rgba(230,57,70,0.6);">ET</span>
            <span style="font-size: 36px; font-weight: 800; color: #F1F1F1; margin-left: 10px;">Edu<span style="color: #E63946;">Track</span></span>
            <p style="color: #8B949E; font-size: 18px; margin-top: 10px;">Seu Workspace Acadêmico Inteligente</p>
        </div>
        """, unsafe_allow_html=True)

        lista_abas = ["🔐 Entrar", "📝 Criar Conta"]
        
        # O rádio invisível mantém a funcionalidade ativa por trás das cortinas
        tab_selecionada = st.radio("Navegação Interna", options=lista_abas, index=st.session_state["aba_ativa"], label_visibility="collapsed")
        
        tab_login, tab_cadastro = st.tabs(lista_abas)

        if tab_selecionada == "🔐 Entrar": st.session_state["aba_ativa"] = 0
        else: st.session_state["aba_ativa"] = 1

        with tab_login:
            with st.form("form_login", clear_on_submit=False):
                email_login = st.text_input("E-mail corporativo ou acadêmico", key="input_email")
                senha_login = st.text_input("Senha de acesso", type="password", key="input_password")
                botao_entrar = st.form_submit_button("Entrar no Workspace", use_container_width=True)
                
            with st.expander("Esqueci minha senha"):
                email_recuperacao = st.text_input("Digite o e-mail cadastrado para receber o link", key="recupera_email")
                if st.button("Enviar e-mail de redefinição", type="primary"):
                    if email_recuperacao: st.success(f"✅ Um link seguro de redefinição de senha foi enviado para {email_recuperacao}! (Simulado no MVP)")
                    else: st.warning("Por favor, digite um e-mail.")
                
            if botao_entrar:
                if email_login and senha_login:
                    try:
                        resposta = requests.post("https://x8ki-letl-twmt.n7.xano.io/api:wwEG4bZX/auth/login", json={"email": email_login, "password": senha_login}, timeout=10)
                        if resposta.status_code == 200:
                            token = resposta.json().get("authToken")
                            if token:
                                st.session_state["token_xano"] = token
                                st.session_state["usuario_logado"] = True
                                st.rerun()
                            else: st.error("Token inválido retornado pelo servidor.")
                        else: st.error("Credenciais inválidas. Verifique seu e-mail e senha.")
                    except: st.error("Erro de comunicação com o servidor.")
                else: st.warning("Por favor, preencha todos os campos.")

        with tab_cadastro:
            with st.form("form_cadastro"):
                nome_cad = st.text_input("Nome Completo")
                email_cad = st.text_input("E-mail")
                senha_cad = st.text_input("Crie uma Senha Forte (mínimo 8 caracteres)", type="password")
                botao_registrar = st.form_submit_button("Registrar Conta", use_container_width=True)
                
            if botao_registrar:
                if nome_cad and email_cad and senha_cad:
                    if len(senha_cad) < 8: st.error("⚠️ A senha precisa ter pelo menos 8 caracteres!")
                    else:
                        try:
                            resposta = requests.post("https://x8ki-letl-twmt.n7.xano.io/api:wwEG4bZX/auth/signup", json={"name": nome_cad, "email": email_cad, "password": senha_cad})
                            if resposta.status_code == 200: 
                                st.session_state["aba_ativa"] = 0
                                st.toast("✅ Conta criada com sucesso! Faça seu login.")
                                st.rerun()
                            else: st.error("Erro ao registrar conta. Verifique se o e-mail já existe.")
                        except: st.error("Erro interno no servidor.")
                else: st.warning("Preencha todos os campos.")