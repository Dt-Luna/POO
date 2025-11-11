import streamlit as st
import pandas as pd
import time
from views import View

class ManterProfissionalUI:
    def main():
        st.header('Cadastro de Profissionais')
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()
    
    def listar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write('Nenhum profissional cadastrado')
        else:
            list_dic = []
            for obj in profissionais: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    
    def inserir():
        especialidades = View.especialidade_listar()
        nome = st.text_input('Informe o nome')
        email = st.text_input('Informe o email')
        especialidade = st.selectbox('Informe a especialidade', especialidades, index=None)
        conselho = st.text_input('Informe o conselho')
        senha = st.text_input("Informe a senha", type="password")
        if st.button('Inserir'):
            try:
                if especialidade != None: especialidade = especialidade.get_id()
                View.profissional_inserir(nome, email, especialidade, conselho, senha)
                st.success('Profissional inserido com sucesso')
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

    def atualizar():
        profissionais = View.profissional_listar()
        especialidades = View.especialidade_listar()
        if len(profissionais) == 0: st.write('Nenhum profissional cadastrado')
        else:
            op = st.selectbox('Atualização de profissionais', profissionais)
            nome = st.text_input('Novo nome', op.get_nome())
            email = st.text_input('Novo email', op.get_email())
            id_especialidade = None if op.get_id_especialidade() in [None, 0] else op.get_id_especialidade()
            especialidade = st.selectbox('Informe a nova especialidade', especialidades)
            conselho = st.text_input('Novo conselho', op.get_conselho())
            senha = st.text_input('Nova senha', op.get_senha())
            if st.button('Atualizar'):
                try:
                    if especialidade != None: especialidade = especialidade.get_id()
                    id = op.get_id()
                    View.profissional_atualizar(id, nome, email, especialidade, conselho, senha)
                    st.success('Profissional atualizado com sucesso')
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()
            
    def excluir():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write('Nenhum profissional cadastrado')
        else:
            op = st.selectbox('Exclusão de profissionais', profissionais)
            if st.button('Excluir'):
                try:
                    id = op.get_id()
                    View.profissional_excluir(id)
                    st.success('Profissional excluído com sucesso')
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()
