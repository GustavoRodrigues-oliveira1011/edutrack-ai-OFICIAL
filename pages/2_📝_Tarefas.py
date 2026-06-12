import streamlit as st
import requests
import datetime

st.set_page_config(page_title="Tarefas", page_icon="📝", layout="wide")

# ==========================================
# TRAVA DE SEGURANÇA (FORÇAR LOGIN)
# ==========================================
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

@st.dialog("⚠️ Confirmar Exclusão")
def modal_excluir(tarefa_id, tarefa_titulo):
    st.write(f"Deseja excluir a tarefa **{tarefa_titulo}**?")
    if st.button("Sim, Excluir", type="primary"):
        requests.delete(f"https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/academic_task/{tarefa_id}", headers=cabecalho)
        st.rerun()

@st.dialog("✏️ Editar Tarefa")
def modal_editar(tarefa):
    with st.form(f"form_edit_task_{tarefa['id']}"):
        novo_titulo = st.text_input("Título", value=tarefa['title'])
        nova_desc = st.text_area("Descrição", value=tarefa.get('description', ''))
        data_atual_dt = datetime.datetime.fromtimestamp(tarefa['due_date'] / 1000.0).date()
        nova_data = st.date_input("Novo Prazo", value=data_atual_dt)
        if st.form_submit_button("Salvar"):
            dados = tarefa.copy()
            dados.update({
                "title": novo_titulo, 
                "description": nova_desc, 
                "due_date": int(datetime.datetime.combine(nova_data, datetime.time.min).timestamp() * 1000)
            })
            requests.patch(f"https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/academic_task/{tarefa['id']}", json=dados, headers=cabecalho)
            st.rerun()

st.markdown("<h1 style='border-bottom: 2px solid #E63946; padding-bottom: 10px;'>Gestão de Tarefas</h1>", unsafe_allow_html=True)
tab_lista, tab_novo = st.tabs(["📋 Minhas Tarefas", "➕ Nova Tarefa"])

with tab_novo:
    # Busca a lista de disciplinas para mapear no selectbox de forma dinâmica
    lista_disciplinas_existentes = []
    mapa_disciplinas = {}
    try:
        res_subjects = requests.get("https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/subjects", headers=cabecalho)
        if res_subjects.status_code == 200:
            lista_disciplinas_existentes = res_subjects.json()
            # Garante que o ID enviado seja um Integer estrito para o Xano
            mapa_disciplinas = {d["name"]: int(d["id"]) for d in lista_disciplinas_existentes}
    except:
        pass

    if not mapa_disciplinas:
        mapa_disciplinas = {"Nenhuma disciplina cadastrada": 0}

    with st.form("form_tarefa"):
        titulo = st.text_input("Título da Tarefa")
        descricao = st.text_area("Descrição da Atividade")
        col1, col2 = st.columns(2)
        with col1:
            disc_selecionada = st.selectbox("Disciplina Vinculada", options=list(mapa_disciplinas.keys()))
            semestre = st.selectbox("Semestre", ["1º Semestre", "2º Semestre", "3º Semestre", "4º Semestre", "5º Semestre", "6º Semestre"])
        with col2:
            data = st.date_input("Prazo de Entrega")
            prioridade = st.selectbox("Prioridade", ["Baixa", "Média", "Alta"])
        
        if st.form_submit_button("Salvar Tarefa", type="primary"):
            if mapa_disciplinas.get(disc_selecionada) == 0:
                st.error("⚠️ Cadastre uma disciplina válida primeiro na aba de Disciplinas!")
            elif titulo:
                # Converte para timestamp Unix em milissegundos estrito
                ts = int(datetime.datetime.combine(data, datetime.time.min).timestamp() * 1000)
                
                payload = {
                    "title": titulo, 
                    "description": descricao, 
                    "due_date": ts, 
                    "Status": "Pendente", # Força a letra maiúscula de acordo com o input do Xano Status
                    "subject_id": mapa_disciplinas[disc_selecionada],
                    "Priority": prioridade, 
                    "semester": semestre
                }
                
                resposta = requests.post("https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/academic_task", json=payload, headers=cabecalho)
                
                # TRAVA DE VALIDAÇÃO REAL DO BACKEND
                if resposta.status_code == 200:
                    st.success("✅ Tarefa cadastrada e vinculada com sucesso!")
                    st.rerun()
                else:
                    st.error(f"❌ Erro ao salvar no banco. (O Xano recusou com o erro: {resposta.text})")
            else:
                st.warning("O título da tarefa é obrigatório.")

with tab_lista:
    col_busca, col_filtro = st.columns([3, 1])
    with col_busca: busca = st.text_input("Buscar tarefa por título...")
    with col_filtro: filtro_status = st.selectbox("Filtrar por Status", ["Todas", "Pendente", "Concluída"])
    st.markdown("---")

    try:
        r = requests.get("https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/academic_task", headers=cabecalho)
        if r.status_code == 200:
            tarefas = r.json()
            if busca: tarefas = [t for t in tarefas if busca.lower() in t.get("title", "").lower()]
            if filtro_status != "Todas": tarefas = [t for t in tarefas if t.get("status", "") == filtro_status or t.get("Status", "") == filtro_status]
            
            if len(tarefas) > 0:
                hoje = int(datetime.datetime.combine(datetime.date.today(), datetime.time.min).timestamp() * 1000)
                for t in tarefas:
                    dt_str = datetime.datetime.fromtimestamp(t['due_date'] / 1000.0).strftime('%d/%m/%Y')
                    
                    status_atual = t.get('status', t.get('Status', 'Pendente'))
                    atrasada = status_atual == "Pendente" and t['due_date'] < hoje
                    
                    prio_val = t.get('Priority', 'Baixa')
                    if "Alta" in prio_val:
                        cor_prio, emoji_dot = "#FF4B4B", "🔴"
                    elif "Média" in prio_val or "Media" in prio_val:
                        cor_prio, emoji_dot = "#FFD166", "🟡"
                    else:
                        cor_prio, emoji_dot = "#06D6A0", "🟢"
                        
                    badge_prio = f"<span style='border: 1px solid {cor_prio}; color: {cor_prio}; padding: 2px 8px; border-radius: 12px; font-size: 13px; font-weight: bold;'>{prio_val} {emoji_dot}</span>"
                    badge_atraso = f"<span style='border: 1px solid #FF4B4B; color: #FF4B4B; padding: 2px 8px; border-radius: 12px; font-size: 13px; font-weight: bold; margin-left: 10px;'>⚠️ ATRASADA</span>" if atrasada else ""
                    badge_concluido = f"<span style='border: 1px solid #06D6A0; color: #06D6A0; padding: 2px 8px; border-radius: 12px; font-size: 13px; font-weight: bold; margin-left: 10px;'>✅ CONCLUÍDA</span>" if status_atual == "Concluída" else ""
                    
                    icone = '✅' if status_atual == 'Concluída' else '📌'
                    
                    with st.expander(f"{icone} {t['title']} — Prazo: {dt_str}"):
                        st.markdown(f"**Status:** {badge_prio} {badge_atraso} {badge_concluido}", unsafe_allow_html=True)
                        st.write(f"**Descrição:** {t.get('description', 'Sem descrição')}")
                        st.write(f"**Semestre:** {t.get('semester', 'Não informado')}")
                        
                        c1, c2, c3 = st.columns([1, 1, 6])
                        if status_atual == "Pendente" and c1.button("✅ Concluir", key=f"c_{t['id']}"):
                            requests.patch(f"https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/academic_task/{t['id']}", json={**t, "status": "Concluída", "Status": "Concluída"}, headers=cabecalho)
                            st.rerun()
                        if c2.button("✏️ Editar", key=f"e_{t['id']}"): modal_editar(t)
                        if c3.button("🗑️ Excluir", key=f"d_{t['id']}", type="secondary"): modal_excluir(t['id'], t['title'])
            else: 
                st.info("Nenhuma tarefa cadastrada para este filtro.")
    except: 
        st.error("Erro ao carregar a listagem de tarefas.")