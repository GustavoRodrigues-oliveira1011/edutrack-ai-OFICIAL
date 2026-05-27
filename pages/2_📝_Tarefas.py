import streamlit as st
import requests
import datetime

st.set_page_config(page_title="Tarefas", page_icon="📝")
st.title("Gestão de Tarefas")

tab_lista, tab_novo = st.tabs(["📋 Minhas Tarefas", "➕ Nova Tarefa"])

# ==========================================
# ABA 1: CADASTRAR NOVA TAREFA (POST)
# ==========================================
with tab_novo:
    st.subheader("Cadastrar Nova Tarefa")
    
    url_subjects = "https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/subjects"
    try:
        res_subjects = requests.get(url_subjects)
        if res_subjects.status_code == 200:
            lista_disciplinas = res_subjects.json()
            mapa_disciplinas = {d["name"]: d["id"] for d in lista_disciplinas}
        else:
            mapa_disciplinas = {"Nenhuma disciplina encontrada": 0}
    except Exception:
        mapa_disciplinas = {"Erro ao carregar disciplinas": 0}

    with st.form("form_tarefa"):
        titulo = st.text_input("Título da Tarefa")
        descricao = st.text_area("Descrição")
        
        col1, col2 = st.columns(2)
        with col1:
            data_vencimento = st.date_input("Data de Vencimento")
        with col2:
            nome_disciplina_selecionada = st.selectbox("Disciplina", options=list(mapa_disciplinas.keys()))
        
        submitted = st.form_submit_button("Salvar Tarefa")
        
        if submitted:
            if mapa_disciplinas.get(nome_disciplina_selecionada) == 0:
                st.error("Cadastre uma disciplina válida primeiro antes de criar tarefas!")
            else:
                id_disciplina = mapa_disciplinas[nome_disciplina_selecionada]
                timestamp_ms = int(datetime.datetime.combine(data_vencimento, datetime.time.min).timestamp() * 1000)
                url_post = "https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/academic_task"
                
                dados = {
                    "title": titulo,
                    "description": descricao,
                    "due_date": timestamp_ms,
                    "status": "Pendente",
                    "subject_id": id_disciplina,
                    "user_id": 1
                }
                
                try:
                    resposta = requests.post(url_post, json=dados)
                    if resposta.status_code == 200:
                        st.success(f"Show! A tarefa '{titulo}' foi salva!")
                    else:
                        st.error(f"Opa, o Xano recusou. Código: {resposta.status_code}")
                except Exception as e:
                    st.error(f"Erro ao conectar: {e}")

# ==========================================
# ABA 2: LISTAR, EDITAR E EXCLUIR TAREFAS
# ==========================================
with tab_lista:
    col_busca, col_filtro = st.columns([3, 1])
    
    with col_busca:
        search = st.text_input("Buscar tarefa pelo título...", placeholder="Ex: Projeto EduTrack")
    with col_filtro:
        filtro_status = st.selectbox("Status", ["Todas", "Pendente", "Concluída"])

    st.markdown("---")

    url_get = "https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/academic_task"
    
    try:
        resposta = requests.get(url_get)
        
        if resposta.status_code == 200:
            todas_tarefas = resposta.json()
            
            if search:
                todas_tarefas = [t for t in todas_tarefas if search.lower() in t.get("title", "").lower()]
            
            if filtro_status != "Todas":
                todas_tarefas = [t for t in todas_tarefas if t.get("status", "") == filtro_status]
            
            if len(todas_tarefas) > 0:
                todas_tarefas.sort(key=lambda x: x.get('status', 'Pendente'), reverse=True)
                
                for tarefa in todas_tarefas:
                    data_legivel = datetime.datetime.fromtimestamp(tarefa['due_date'] / 1000.0).strftime('%d/%m/%Y')
                    icone = "✅" if tarefa['status'] == "Concluída" else "📌"
                    
                    with st.expander(f"{icone} {tarefa['title']} - Prazo: {data_legivel}", expanded=False):
                        st.write(f"**Descrição:** {tarefa.get('description', '')}")
                        st.write(f"**Status atual:** {tarefa['status']}")
                        
                        # 1. BOTÃO RÁPIDO DE CONCLUIR (Só aparece se estiver pendente)
                        if tarefa['status'] == "Pendente":
                            if st.button("✅ Marcar como Concluída", key=f"btn_concluir_{tarefa['id']}"):
                                url_patch = f"https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/academic_task/{tarefa['id']}"
                                dados_update = tarefa.copy()
                                dados_update["status"] = "Concluída"
                                if requests.patch(url_patch, json=dados_update).status_code == 200:
                                    st.rerun()
                        
                        st.markdown("---")
                        
                        # 2. ÁREA DE EDIÇÃO AVANÇADA E EXCLUSÃO
                        with st.expander("✏️ Editar ou Excluir Tarefa"):
                            with st.form(key=f"form_edit_{tarefa['id']}"):
                                edit_titulo = st.text_input("Novo Título", value=tarefa['title'])
                                edit_desc = st.text_area("Nova Descrição", value=tarefa.get('description', ''))
                                
                                index_status = 0 if tarefa['status'] == "Pendente" else 1
                                edit_status = st.selectbox("Mudar Status", ["Pendente", "Concluída"], index=index_status)
                                
                                col_btn1, col_btn2 = st.columns(2)
                                with col_btn1:
                                    btn_salvar = st.form_submit_button("Salvar Alterações")
                                with col_btn2:
                                    # O botão de deletar fica no formulário mas executa uma ação diferente
                                    btn_excluir = st.form_submit_button("🗑️ Excluir Tarefa", type="primary")
                                
                                if btn_salvar:
                                    url_patch = f"https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/academic_task/{tarefa['id']}"
                                    dados_update = tarefa.copy()
                                    dados_update["title"] = edit_titulo
                                    dados_update["description"] = edit_desc
                                    dados_update["status"] = edit_status
                                    
                                    if requests.patch(url_patch, json=dados_update).status_code == 200:
                                        st.success("Atualizado!")
                                        st.rerun()
                                    else:
                                        st.error("Erro ao atualizar.")
                                
                                if btn_excluir:
                                    url_delete = f"https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/academic_task/{tarefa['id']}"
                                    if requests.delete(url_delete).status_code == 200:
                                        st.success("Tarefa excluída!")
                                        st.rerun()
                                    else:
                                        st.error("Erro ao excluir.")
            else:
                st.info("Nenhuma tarefa encontrada. Que tal cadastrar uma nova?")
        else:
            st.error("Erro ao puxar as tarefas do banco.")
            
    except Exception as e:
        st.error(f"Erro de conexão: {e}")