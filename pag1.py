import streamlit as st

###########IZENBURUA
st.title("HASIERAKO LEHEN ORRIALDEA")
###########
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
st.page_link("streamlit_app.py", label="Etxea", icon="🏠") ##st.markdown("[🏠 Etxea](./streamlit_app.py)")
st.page_link("pages/pag2.py", label="2.en Orrialdea", icon="2️⃣") ##st.markdown("[2️⃣ 2. Orrialdea](./pages/pag2.py)")


# Función para sumar
def sumar(numero1, numero2):
    return numero1 + numero2

# Entradas para los números
numero1 = st.number_input("Sartu lehenengo zenbakia:", value=0)
numero2 = st.number_input("Sartu bigarren zenbakia:", value=0)

if numero1:
    st.write(f"Zure lehenengo zenbakia: {numero1}")
if numero2:
    st.write(f"Zure bigarren zenbakia: {numero2}")

# Botón "kalkulatu"
if st.button("kalkulatu"):
    emaitza = sumar(numero1, numero2)
    st.write(f"Emaitza: {emaitza}")

