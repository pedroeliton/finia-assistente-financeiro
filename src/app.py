import streamlit as st

st.set_page_config(
    page_title="FinIA",
    page_icon="💰",
    layout="centered"
)

st.title("💰 FinIA")
st.subheader("Assistente de Educação Financeira")

st.write(
    "Olá! Eu sou o FinIA. "
    "Posso ajudar você a compreender conceitos de educação financeira "
    "e realizar simulações simples."
)

# Histórico da conversa
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada do usuário
if prompt := st.chat_input("Digite sua dúvida financeira..."):

    # Exibe mensagem do usuário
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Resposta inicial
    response = (
        "Recebi sua pergunta! Em breve poderei "
        "consultar minha base de conhecimento e responder "
        "utilizando inteligência artificial."
    )

    # Exibe resposta do FinIA
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
