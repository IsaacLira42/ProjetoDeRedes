from Models.admin import Admin
from Models.admins import Admins
import streamlit as st


def app():
    st.header("Login")
    with st.form("login_form"):
        usuario = st.text_input("Usuario")
        senha = st.text_input("Senha", type="password")
        submit = st.form_submit_button("Entrar")
    
    if submit:
        admins = Admins.listar()
        usuario_encontrado = None
        if len(admins) == 0:
            Admins.inserir(Admin(0, "admin", "admin"))

        for admin in admins:
            if admin.usuario == usuario and admin.senha == senha:
                usuario_encontrado = admin
                break
        
        if usuario_encontrado:
            st.session_state['logged_in'] = True
            st.session_state['current_user'] = usuario_encontrado
            st.success("Login realizado com sucesso!")
            st.rerun()
        else:
            st.error("Usuario ou senha incorretos.")