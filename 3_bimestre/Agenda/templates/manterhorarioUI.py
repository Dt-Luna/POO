import streamlit as st
import pandas as pd
import time
from views import View
import datetime

class ManterClienteUI:
    def main():
        st.header('Cadastro de Horários')
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()
    
    def listar():
        horarios = View.cliente_listar()
        if len(horarios) == 0: st.write('Nenhum cliente cadastrado')
        else:
            list_dic = []
            for obj in horarios: 
                cliente = View.cliente_listar_id(obj.get_id_cliente())
                servico = View.servico_listar_id(obj.get_id_servico())
                if cliente != None: cliente = cliente.get_nome()
                if servico != None: servico = servico.get_desc()
                list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    
    def inserir():
        clientes = View.cliente_listar()
        servico = View.servico_listar()
        data = st.text_input('Informe a data e o horário do serviço', datetime.now().strftime("%d/%m/%Y %H:%M"))
        confirmado = st.checkbox('Confirmado')
        cliente = st.selectbox('Informe o cliente'. clientes, Index=None)
        servico = st.selectbox('Informe o serviço'. servicos, Index=None)
        if st.button('Inserir'):
            if cliente != None: id_cliente= cliente.get_id()
            if servico != None: id_servico= servico.get_id()
            View.horario_inserir(datetime.strptime(data,"%d/%m/%Y %H:%M"),confirmado, id_cliente, id_servico)
            st.success('Horário inserido com sucesso')

    def atualizar():
        horarios = View.cliente_listar()
        if len(horarios) == 0: st.write('Nenhum cliente cadastrado')
        else:
            clientes = View.cliente_listar()
            servico = View
            op = st.selectbox('Atualização de clientes', clientes)
            nome = st.text_input('Novo nome', op.get_nome())
            email = st.text_input('Novo email', op.get_email())
            fone = st.text_input('Novo fone', op.get_fone())
            if st.button('Atualizar'):
                id = op.get_id()
                View.cliente_atualizar(id, nome, email, fone)
                st.success('Cliente atualizado com sucesso')
            
    def excluir():
        clientes = View.cliente_listar()
        if len(clientes) == 0: st.write('Nenhum cliente cadastrado')
        else:
            op = st.selectbox('Exclusão de clientes', clientes)
            if st.button('Excluir'):
                id = op.get_id()
                View.cliente_excluir(id)
                st.success('Cliente excluído com sucesso')
