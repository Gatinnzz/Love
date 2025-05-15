import streamlit as st

# Página inicial
st.set_page_config(page_title="Você me ama?", page_icon="❤️", layout="centered")

st.title("💘 Você me ama?")
st.markdown("### Só tem uma resposta certa e vc sabe qual é... 😏")

# Botão "Sim"
if st.button("Sim ❤️"):
    st.success("Eu também te amo pra caralho garota 🥰")

# Nenhum botão de "Não" 😄
