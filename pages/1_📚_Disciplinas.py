import streamlit as st
import requests

st.set_page_config(page_title="Disciplinas", page_icon="📚", layout="wide")

if "usuario_logado" not in st.session_state or not st.session_state["usuario_logado"]:
    st.error("🔒 Sua sessão expirou ou você não está logado.")
    if st.button("Fazer Login Novamente", type="primary"):
        st.switch_page("app.py")
    st.stop()

cabecalho = {"Authorization": f"Bearer {st.session_state['token_xano']}"}

css_e_logo = """
    <style>
        [data-testid="stSidebarNav"] { padding-top: 4rem !important; }
        .logo-fixa { position: fixed; top: 1.5rem; left: 1.5rem; display: flex; align-items: center; gap: 10px; z-index: 99999; }
        [data-testid="stSidebarNavItems"] li div:hover { background-color: rgba(230, 57, 70, 0.15) !important; }
        [data-testid="stSidebarNavItems"] li div[data-testid="stSidebarNavLinkActive"] { background-color: rgba(230, 57, 70, 0.3) !important; border-left: 4px solid #E63946; }
        [data-testid="stSidebarNavItems"] li:first-child a span { display: none; }
        [data-testid="stSidebarNavItems"] li:first-child a::after { content: "📊 Dashboard"; color: #E63946; font-weight: 800; font-size: 16px; letter-spacing: 0.5px; }
        @media (max-width: 768px) { .logo-fixa { display: none; } }
    </style>
    <div class="logo-fixa">
        <div style="background-color: #E63946; color: white; border-radius: 8px; padding: 5px 10px; font-weight: 900; font-size: 18px; box-shadow: 0 0 10px rgba(230,57,70,0.5);">ET</div>
        <div style="font-size: 22px; font-weight: 800; color: #F1F1F1; letter-spacing: -1px;">Edu<span style="color: #E63946;">Track</span></div>
    </div>
"""
with st.sidebar: st.markdown(css_e_logo, unsafe_allow_html=True)

# Busca prévia de disciplinas para listagem e validações
lista_disciplinas_existentes = []
try:
    r_check = requests.get("https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/subjects", headers=cabecalho)
    if r_check.status_code == 200: 
        lista_disciplinas_existentes = r_check.json()
except: pass

@st.dialog("⚠️ Confirmar Exclusão")
def modal_excluir(id_disciplina, nome_disciplina):
    st.write(f"Deseja excluir a disciplina **{nome_disciplina}**?")
    if st.button("Sim, Excluir", type="primary"):
        requests.delete(f"https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/subjects/{id_disciplina}", headers=cabecalho)
        st.rerun()

@st.dialog("✏️ Editar Disciplina")
def modal_editar(disciplina):
    with st.form(f"form_edit_disc_{disciplina['id']}"):
        novo_nome = st.text_input("Nome da Disciplina", value=disciplina['name'])
        novo_prof = st.text_input("Professor", value=disciplina.get('teacher', ''))
        novo_semestre = st.selectbox("Semestre/Período", ["1º Semestre", "2º Semestre", "3º Semestre", "4º Semestre", "5º Semestre", "6º Semestre"], index=["1º Semestre", "2º Semestre", "3º Semestre", "4º Semestre", "5º Semestre", "6º Semestre"].index(disciplina.get('semester', '1º Semestre')) if disciplina.get('semester') in ["1º Semestre", "2º Semestre", "3º Semestre", "4º Semestre", "5º Semestre", "6º Semestre"] else 0)
        nova_carga = st.text_input("Carga Horária (ex: 60h)", value=disciplina.get('carga_horaria', ''))
        nova_desc = st.text_area("Descrição", value=disciplina.get('description', ''))
        
        if st.form_submit_button("Salvar Alterações"):
            dados = disciplina.copy()
            dados.update({"name": novo_nome, "teacher": novo_prof, "description": nova_desc, "semester": novo_semestre, "carga_horaria": nova_carga})
            res_put = requests.put(f"https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/subjects/{disciplina['id']}", json=dados, headers=cabecalho)
            if res_put.status_code == 200:
                st.rerun()
            else:
                st.error(f"Erro ao editar: {res_put.text}")

st.markdown("<h1 style='border-bottom: 2px solid #E63946; padding-bottom: 10px;'>Gestão de Disciplinas</h1>", unsafe_allow_html=True)
tab_lista, tab_novo = st.tabs(["📚 Minhas Disciplinas", "➕ Nova Disciplina"])

with tab_novo:
    with st.form("form_disciplina"):
        col1, col2 = st.columns(2)
        with col1:
            nome = st.text_input("Nome da Disciplina")
            semestre_disc = st.selectbox("Semestre/Período", ["1º Semestre", "2º Semestre", "3º Semestre", "4º Semestre", "5º Semestre", "6º Semestre"])
        with col2:
            professor = st.text_input("Nome do Professor")
            carga_horaria = st.text_input("Carga Horária (ex: 80h)")
            
        descricao = st.text_area("Descrição do Conteúdo")
        
        if st.form_submit_button("Salvar Disciplina", type="primary"):
            if nome:
                duplicado = any(d.get('name', '').lower() == nome.lower() and d.get('teacher', '').lower() == professor.lower() for d in lista_disciplinas_existentes)
                if duplicado:
                    st.error("⚠️ Já existe uma disciplina cadastrada com esse mesmo nome e professor!")
                else:
                    payload = {
                        "name": nome, 
                        "teacher": professor, 
                        "description": descricao, 
                        "semester": semestre_disc,
                        "carga_horaria": carga_horaria,
                        "arquivada": False
                    }
                    resposta = requests.post("https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/subjects", json=payload, headers=cabecalho)
                    
                    if resposta.status_code == 200:
                        st.success("✅ Disciplina salva com sucesso!")
                        st.rerun()
                    else:
                        st.error(f"❌ Erro ao salvar no banco de dados. (Xano retornou: {resposta.text})")
            else: 
                st.warning("O nome da disciplina é obrigatório.")

with tab_lista:
    col_b, col_f, col_arq = st.columns([2, 1, 1])
    with col_b: busca = st.text_input("Buscar Disciplina...", placeholder="Ex: Engenharia de Software")
    with col_f: 
        st.write("")
        filtrar_atrasadas = st.checkbox("⚠️ Com tarefas em atraso")
    with col_arq:
        st.write("")
        mostrar_arquivadas = st.checkbox("📦 Ver Arquivadas")
    st.markdown("---")
    
    if len(lista_disciplinas_existentes) > 0:
        disciplinas = lista_disciplinas_existentes
        
        # Filtro de Busca
        if busca: 
            disciplinas = [d for d in disciplinas if busca.lower() in d.get("name", "").lower()]
            
        # Filtro de Arquivamento
        disciplinas = [d for d in disciplinas if d.get("arquivada", False) == mostrar_arquivadas]
            
        # Filtro de Atraso
        if filtrar_atrasadas:
            r_tasks = requests.get("https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/academic_task", headers=cabecalho)
            if r_tasks.status_code == 200:
                import datetime
                hoje = int(datetime.datetime.combine(datetime.date.today(), datetime.time.min).timestamp() * 1000)
                ids_atrasados = {t['subject_id'] for t in r_tasks.json() if t.get('status') == 'Pendente' and t.get('due_date', 0) < hoje}
                disciplinas = [d for d in disciplinas if d['id'] in ids_atrasados]

        if len(disciplinas) > 0:
            for d in disciplinas:
                icone_arq = "📦" if not d.get("arquivada") else "✅"
                status_nome = d['name'] + (" (Arquivada)" if d.get("arquivada") else "")
                
                with st.expander(f"📘 {status_nome} ({d.get('semester', 'Sem Período')})"):
                    col_info1, col_info2 = st.columns(2)
                    with col_info1: st.write(f"**👨‍🏫 Professor:** {d.get('teacher', 'Não informado')}")
                    with col_info2: st.write(f"**⏱️ Carga Horária:** {d.get('carga_horaria', 'Não informada')}")
                    st.write(f"**📝 Descrição:** {d.get('description', 'Sem anotações')}")
                    
                    c1, c2, c3, c4 = st.columns([5, 1, 1, 1])
                    if c2.button("✏️", key=f"ed_{d['id']}", help="Editar"): modal_editar(d)
                    if c3.button("🗑️", key=f"dl_{d['id']}", help="Excluir"): modal_excluir(d['id'], d['name'])
                    
                    # BOTÃO DE ARQUIVAR COM TRAVA DE VALIDAÇÃO
                    if c4.button(icone_arq, key=f"arq_{d['id']}", help="Arquivar/Desarquivar"):
                        dados_arq = d.copy()
                        dados_arq["arquivada"] = not d.get("arquivada", False)
                        
                        res_arq = requests.put(f"https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/subjects/{d['id']}", json=dados_arq, headers=cabecalho)
                        
                        if res_arq.status_code == 200:
                            st.rerun()
                        else:
                            st.error(f"Erro ao arquivar. Verifique o Xano: {res_arq.text}")
        else:
            st.info("Nenhuma disciplina encontrada com os filtros atuais.")
    else:
        st.info("Você ainda não possui disciplinas cadastradas.")