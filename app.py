import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np

st.set_page_config(page_title="Numistor – Münz-Auswahl", layout="wide")
st.title("🪙 Numistor – Interaktive Münz-Auswahl mit Maus")

uploaded_file = st.file_uploader("📤 Lade ein Bild mit mehreren Münzen hoch", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Sicheres Laden und Konvertieren des Bildes
    try:
        image = Image.open(uploaded_file).convert("RGB")
        img_array = np.asarray(image).astype("uint8")
    except Exception as e:
        st.error(f"❌ Fehler beim Laden des Bildes: {e}")
        st.stop()

    st.image(image, caption="Originalbild", use_column_width=True)
    st.subheader("✏️ Zeichne Kreise auf die Münzen")

    try:
        canvas_result = st_canvas(
            fill_color="rgba(255, 0, 0, 0.3)",
            stroke_width=3,
            stroke_color="#ff0000",

