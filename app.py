import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io
import base64

st.set_page_config(page_title="Numistor – Münz-Auswahl", layout="wide")
st.title("🪙 Numistor – Interaktive Münz-Auswahl mit Maus")

def image_to_base64_url(image: Image.Image) -> str:
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    img_bytes = buffer.getvalue()
    base64_str = base64.b64encode(img_bytes).decode()
    return f"data:image/png;base64,{base64_str}"

uploaded_file = st.file_uploader("📤 Lade ein Bild mit mehreren Münzen hoch", type=["jpg", "jpeg", "png"])

if uploaded_file:
    try:
        image = Image.open(uploaded_file).convert("RGB")
        image_url = image_to_base64_url(image)
    except Exception as e:
        st.error(f"❌ Fehler beim Laden des Bildes: {e}")
        st.stop()

    st.image(image, caption="Originalbild", use_column_width=True)
    st.subheader("✏️ Zeichne Kreise auf die Münzen")

    canvas_result = st_canvas(
        fill_color="rgba(255, 0, 0, 0.3)",
        stroke_width=3,
        stroke_color="#ff0000",
        background_image=image_url,
        update_streamlit=True,
        height=image.height,
        width=image.width,
        drawing_mode="circle",
        key="canvas",
    )

    if canvas_result.json_data and "objects" in canvas_result.json_data:
        objects = canvas_result.json_data["objects"]
        if objects:
            st.success(f"✅ {len(objects)} Kreise erkannt")
            st.write("🧾 Koordinaten der Kreise:")
            for i, obj in enumerate(objects, 1):
                st.write(f"{i}: center=({int(obj['left'])}, {int(obj['top'])}), radius={int(obj['radius'])}")
        else:
            st.warning("⚠️ Noch keine Kreise gezeichnet.")



