import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np

st.set_page_config(page_title="Numistor – Münz-Auswahl", layout="wide")
st.title("🪙 Numistor – Interaktive Münz-Auswahl mit Maus")

uploaded_file = st.file_uploader("📤 Lade ein Bild mit mehreren Münzen hoch", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Konvertiere sicher zu RGB und NumPy-Array
    image = Image.open(uploaded_file).convert("RGB")
    img_array = np.asarray(image).astype("uint8")  # <-- wichtig

    st.image(image, caption="Originalbild", use_column_width=True)
    st.subheader("✏️ Zeichne Kreise auf die Münzen")

    canvas_result = st_canvas(
        fill_color="rgba(255, 0, 0, 0.3)",
        stroke_width=3,
        stroke_color="#ff0000",
        background_image=img_array,
        update_streamlit=True,
        height=image.height,
        width=image.width,
        drawing_mode="circle",
        key="canvas",
    )

    if canvas_result.json_data is not None:
        objects = canvas_result.json_data["objects"]
        if objects:
            st.success(f"✅ {len(objects)} Kreise erkannt")
            st.write("🧾 Koordinaten der Kreise:")
            for i, obj in enumerate(objects, 1):
                st.write(f"{i}: center=({int(obj['left'])}, {int(obj['top'])}), radius={int(obj['radius'])}")
        else:
            st.warning("⚠️ Noch keine Kreise gezeichnet.")



