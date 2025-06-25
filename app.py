
import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Numistor Münzerkennung", layout="wide")
st.title("🪙 Numistor – Interaktive Münzerkennung")

uploaded_file = st.file_uploader("📤 Lade ein Bild mit mehreren Münzen hoch", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Hochgeladenes Bild", use_column_width=True)
    st.info("🔧 Die manuelle Auswahl von Münzen mit der Maus folgt im nächsten Schritt (interaktive Komponente folgt).")
