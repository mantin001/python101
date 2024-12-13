import streamlit as st



st.title("🎈 Nere App berria")
st.write(
    "Goazen sortzera! Dokumentazioa edo laguntza behar baduzu, sakatu hemen  [docs.streamlit.io](https://docs.streamlit.io/)."
)
with st.sidebar:
    st.write("MENUA")
    #log in 
    #log out
    #lo detecta automaticamente  y se ordena automaticamente. Si esto no es el orden, hay que usar trucos

# Botón "sakatu hemen"
if st.button("sakatu hemen"):
    st.write("Oso ongi. Sakatu duzu")


