# System Context
## Overview
Este projeto é um ecossistema de gestão acadêmica chamado **EduTrack AI**, construído utilizando XanoScript e Spec-Driven Development.

## Purpose
Permitir que alunos gerenciem suas disciplinas, tarefas e progresso acadêmico de forma centralizada.

## Core Entities
- **Users**: Entidade nativa do Xano para autenticação.
- **Subjects**: Disciplinas acadêmicas que pertencem aos usuários.
- **Tasks**: Tarefas vinculadas a cada disciplina.

## Relationships
- Cada **Subject** pertence a um **User**.
- Cada **Task** pertence a um **Subject**.

## Expected Evolution
O sistema incluirá APIs para conexão com o frontend em Streamlit, automações de lembretes e integração com IA para análise de desempenho.

