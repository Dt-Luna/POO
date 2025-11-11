import streamlit as st
import pandas as pd
import time
from views import View

class ManterEspecialidadeUI:
    def main():
        st.header('Cadastro de Especialidades')
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterEspecialidadeUI.listar()
        with tab2: ManterEspecialidadeUI.inserir()
        with tab3: ManterEspecialidadeUI.atualizar()
        with tab4: ManterEspecialidadeUI.excluir()
    
    def listar():
        especialidades = View.especialidade_listar()
        if len(especialidades) == 0: st.write('Nenhuma especialidade cadastrada')
        else:
            list_dic = []
            for obj in especialidades: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    
    def inserir():
        nome = st.text_input('Informe o nome')
        if st.button('Inserir'):
            try:
                View.especialidade_inserir(nome)
                st.success('Esepecialidade inserida com sucesso')
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

    def atualizar():
        especialidades = View.especialidade_listar()
        if len(especialidades) == 0: st.write('Nenhuma especialidade cadastrada')
        else:
            op = st.selectbox('Atualização de especialidades', especialidades)
            nome = st.text_input('Novo nome', op.get_nome())
            if st.button('Atualizar'):
                try:
                    id = op.get_id()
                    View.especialidade_atualizar(id, nome)
                    st.success('Especialidade atualizada com sucesso')
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
                    time.sleep(2)
                    st.rerun()
            
    def excluir():
        especialidades = View.especialidade_listar()
        if len(especialidades) == 0: st.write('Nenhuma especialidade cadastrada')
        else:
            op = st.selectbox('Exclusão de especialidade', especialidades)
            if st.button('Excluir'):
                try:
                    id = op.get_id()
                    View.especialidade_excluir(id)
                    st.success('Especialidade excluída com sucesso')
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()
