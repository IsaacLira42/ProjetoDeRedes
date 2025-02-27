import streamlit as st
from Templates import adminUI, loginUI, vitimaUI

# Começo
def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
        st.session_state['current_user'] = None

    st.title("Monitoramento Remoto")

    if st.session_state['logged_in']:
        adminUI.app()
    else:
        pagina = st.sidebar.radio("Navegação", ("Login Admin", "Vitima"))
        if pagina == "Login Admin":
            loginUI.app()
        elif pagina == "Vitima":
            vitimaUI.app()

main()