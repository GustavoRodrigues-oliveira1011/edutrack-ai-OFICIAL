import streamlit as st
import requests

# Configuração OBRIGATÓRIA no topo
st.set_page_config(page_title="EduTrack - Dashboard", page_icon="🎓", layout="wide")

# Inicialização segura da sessão
if "usuario_logado" not in st.session_state:
    st.session_state["usuario_logado"] = False
if "token_xano" not in st.session_state:
    st.session_state["token_xano"] = ""

# ==========================================
# AMBIENTE 1: USUÁRIO LOGADO (DASHBOARD REAL)
# ==========================================
if st.session_state["usuario_logado"]:
    # O Streamlit renderiza apenas o que está dentro deste bloco
    
    # Ajustei as proporções das colunas para o botão de Logout ficar menor
    col_titulo, col_espaco, col_botao = st.columns([6, 3, 2])
    with col_titulo:
        st.title("📊 Painel Geral - EduTrack")
    with col_botao:
        st.write("") 
        # Removi o use_container_width para o botão não esticar
        if st.button("Sair (Logout)", type="primary"):
            st.session_state["usuario_logado"] = False
            st.session_state["token_xano"] = ""
            st.rerun()

    st.markdown("---")
    
    # BUSCA DE DADOS REAIS NO XANO
    total_disciplinas = 0
    total_tarefas = 0
    tarefas_pendentes = 0
    tarefas_concluidas = 0
    
    try:
        res_sub = requests.get("https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/subjects")
        if res_sub.status_code == 200:
            total_disciplinas = len(res_sub.json())
            
        res_task = requests.get("https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/academic_task")
        if res_task.status_code == 200:
            lista_tarefas = res_task.json()
            total_tarefas = len(lista_tarefas)
            tarefas_pendentes = len([t for t in lista_tarefas if t.get("status") == "Pendente"])
            tarefas_concluidas = len([t for t in lista_tarefas if t.get("status") == "Concluída"])
            
    except Exception as e:
        st.warning(f"Erro ao conectar com o banco de dados: {e}")

    # Exibindo os KPIs sincronizados
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="📚 Total de Disciplinas", value=total_disciplinas)
    with col2:
        st.metric(label="📝 Total de Tarefas", value=total_tarefas)
    with col3:
        st.metric(label="⏳ Tarefas Pendentes", value=tarefas_pendentes, delta="- Foco!" if tarefas_pendentes > 0 else "")
    with col4:
        st.metric(label="✅ Tarefas Concluídas", value=tarefas_concluidas, delta="Muito bem!" if tarefas_concluidas > 0 else "")

    st.markdown("---")
    
    col_dica, col_refresh = st.columns([4, 1])
    with col_dica:
        st.info("💡 Dica: Utilize o menu lateral para cadastrar novas Disciplinas ou atualizar o status das suas Tarefas.")
    with col_refresh:
        if st.button("🔄 Atualizar Números"):
            st.rerun()

# ==========================================
# AMBIENTE 2: USUÁRIO DESLOGADO (TELA DE LOGIN COMPACTA)
# ==========================================
else:
    # Esconde menu lateral, botão de colapso e as instruções de formulário ("Press Enter")
    st.markdown("""
        <style>
            [data-testid="stSidebar"] {display: none;}
            [data-testid="collapsedControl"] {display: none;}
            div[data-testid="InputInstructions"] {display: none !important;}
        </style>
    """, unsafe_allow_html=True)

    # 🪄 Truque das colunas fantasmas para espremer o conteúdo no centro
    col_esq, col_centro, col_dir = st.columns([1, 2, 1])

    with col_centro:
        # Título com o novo vermelho visualmente agradável (#E63946)
        st.markdown("<h1 style='text-align: center; color: #E63946;'>EduTrack</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>Seu Gerenciador Acadêmico</h3>", unsafe_allow_html=True)
        st.write("---")

        tab_login, tab_cadastro = st.tabs(["🔐 Entrar", "📝 Criar Conta"])

        with tab_login:
            with st.form("form_login"):
                email_login = st.text_input("E-mail")
                senha_login = st.text_input("Senha", type="password")
                
                btn_entrar = st.form_submit_button("Entrar no Sistema", use_container_width=True)
                
                if btn_entrar:
                    if email_login and senha_login:
                        url_login = "https://x8ki-letl-twmt.n7.xano.io/api:wwEG4bZX/auth/login"
                        dados = {"email": email_login, "password": senha_login}
                        
                        try:
                            resposta = requests.post(url_login, json=dados)
                            if resposta.status_code == 200:
                                token = resposta.json().get("authToken")
                                st.session_state["usuario_logado"] = True
                                st.session_state["token_xano"] = token
                                st.toast("✅ Login efetuado com sucesso!") 
                                st.rerun()
                            else:
                                st.error("E-mail ou senha incorretos.")
                        except Exception as e:
                            st.error(f"Erro de conexão: {e}")
                    else:
                        st.warning("Preencha e-mail e senha.")

        with tab_cadastro:
            with st.form("form_cadastro"):
                nome_cad = st.text_input("Nome Completo")
                email_cad = st.text_input("E-mail")
                senha_cad = st.text_input("Senha", type="password")
                
                btn_criar = st.form_submit_button("Cadastrar Nova Conta", use_container_width=True)
                
                if btn_criar:
                    if nome_cad and email_cad and senha_cad:
                        url_signup = "https://x8ki-letl-twmt.n7.xano.io/api:wwEG4bZX/auth/signup"
                        dados_cad = {"name": nome_cad, "email": email_cad, "password": senha_cad}
                        
                        try:
                            resposta = requests.post(url_signup, json=dados_cad)
                            if resposta.status_code == 200:
                                st.success("Conta criada com sucesso! Vá para a aba 'Entrar' para fazer o login.")
                            else:
                                st.error(f"Erro ao criar conta. Código: {resposta.status_code}")
                        except Exception as e:
                            st.error(f"Erro de conexão: {e}")
                    else:
                        st.warning("Preencha todos os campos para se cadastrar.")