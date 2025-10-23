from views import View
import streamlit as st

class AlterarSenhaUI:
    def main():
        st.header('Alterar Senha')
        senha = st.text_input('Informe a nova senha', )