import streamlit as st
import requests

# Configuração da página
st.set_page_config(page_title="Disciplinas", page_icon="📚")
st.title("Gestão de Disciplinas")

# Abas para separar Listagem e Cadastro
tab_lista, tab_novo = st.tabs(["📋 Listar", "➕ Nova Disciplina"])

# ==========================================
# ABA 1: CADASTRAR NOVA DISCIPLINA (TESTE POST)
# ==========================================
with tab_novo:
    st.subheader("Cadastrar Nova Matéria")
    with st.form("form_disciplina"):
        nome = st.text_input("Nome da Disciplina")
        descricao = st.text_input("Descrição")
        professor = st.text_input("Nome do Professor")
        
        # Botão para enviar o formulário
        submitted = st.form_submit_button("Salvar")
        
        if submitted:
            # URL correta para o POST (Criar) - ROTA SEGURA
            url_post = "https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/subjects"
            
            dados = {
                "name": nome,
                "description": descricao, 
                "teacher": professor,     
                "user_id": 1  
            }
            
            try:
                resposta = requests.post(url_post, json=dados)
                
                if resposta.status_code == 200:
                    st.success(f"Show! A disciplina '{nome}' foi salva no Xano de verdade!")
                else:
                    st.error(f"Opa, o Xano recusou. Código do erro: {resposta.status_code} | Detalhe: {resposta.text}")
                    
            except Exception as e:
                st.error(f"Erro ao conectar com o Xano: {e}")

# ==========================================
# ABA 2: BUSCAR DISCIPLINAS (BYPASS VIA PYTHON)
# ==========================================
with tab_lista:
    st.subheader("Buscar Disciplinas")
    
    # Barra de pesquisa na tela
    termo_busca = st.text_input("Pesquisar disciplina pelo nome:")
    
    if st.button("Buscar"):
        # Usamos a MESMA ROTA SEGURA, mas agora com GET para puxar tudo
        url_get_todas = "https://x8ki-letl-twmt.n7.xano.io/api:Ne4eK2p9/subjects"
        
        try:
            resposta = requests.get(url_get_todas)
            
            if resposta.status_code == 200:
                todas_disciplinas = resposta.json()
                
                # O Python faz o filtro inteligente aqui!
                if termo_busca:
                    # Filtra ignorando maiúsculas e minúsculas
                    disciplinas_filtradas = [d for d in todas_disciplinas if termo_busca.lower() in d.get("name", "").lower()]
                else:
                    # Se clicar em buscar sem digitar nada, mostra todas
                    disciplinas_filtradas = todas_disciplinas
                
                if len(disciplinas_filtradas) > 0:
                    st.success(f"Encontramos {len(disciplinas_filtradas)} disciplina(s)!")
                    st.dataframe(disciplinas_filtradas, use_container_width=True)
                else:
                    st.warning("Nenhuma disciplina encontrada com esse nome.")
            else:
                st.error(f"Erro ao conectar com o Xano. Código: {resposta.status_code}")
                
        except Exception as e:
            st.error(f"Erro de conexão: {e}")