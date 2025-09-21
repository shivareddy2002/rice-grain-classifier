# app.py
import streamlit as st
from PIL import Image
from model_utils import load_rice_model, load_class_map, predict_topk, get_model_input_size, preprocess_pil_image
import os
# --------------------
# Page Config
# --------------------
st.set_page_config(
    page_title="🌾 Rice Classifier",
    page_icon="🌾",
    layout="wide",
)

# --------------------
# Custom CSS Styling
# --------------------
st.markdown("""
    <style>
        /* Main background */
        .main {
            background-color: #0d1117;
            color: #f0f6fc;
        }
        h1, h2, h3 {
            color: #58a6ff !important;
        }
        .highlight {
            background-color: #161b22;
            padding: 5px 10px;
            border-radius: 5px;
            color: #58a6ff;
            display: inline-block;
        }
        .uploadedImage, .resizedImage {
            border-radius: 12px;
            margin-top: 15px;
        }
        .prediction-box {
            padding: 15px;
            border-radius: 12px;
            background-color: #161b22;
            margin-top: 10px;
        }
        .footer {
            text-align: center;
            color: #8b949e;
            padding: 15px;
        }
        .navbar {
            background-color: #161b22;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .navbar a {
            margin-right: 15px;
            color: #58a6ff;
            text-decoration: none;
            font-weight: bold;
        }
        .navbar a:hover {
            text-decoration: underline;
        }
        .navbar .author {
            color: #f0f6fc;
            font-weight: bold;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# --------------------
# Navigation Bar
# --------------------
st.markdown("""
<div class="navbar">
    <div class="author">Siva Gangi Reddy Lomada</div>
    <div>
        <a href="#demo">Demo</a>
        <a href="#about">About Project</a>
        <a href="#how-it-works">How it Works</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --------------------
# App Title & Description
# --------------------
st.markdown("<h1>🌾 Rice Type Classifier</h1>", unsafe_allow_html=True)
st.write("A **Convolutional Neural Network (CNN)-powered** app to classify different rice grain varieties accurately.")

# --------------------
# Load Model
# --------------------
@st.cache_resource
def load_resources():
    model, model_format = load_rice_model()
    class_names = load_class_map()
    input_size = get_model_input_size(model)
    return model, class_names, input_size

try:
    model, class_names, input_size = load_resources()
except Exception as e:
    st.error(f"⚠️ Model or class map not found. Place model files under `model/` folder. Error: {e}")
    st.stop()

# --------------------
# Sidebar Content (Removed "About & How it Works")
# --------------------
with st.sidebar:
    st.write(f"**Model Input Size:** `{input_size}`")
    st.write(f"**Number of Classes:** `{len(class_names)}`")
    top_k = st.slider("Choose the Top-K predictions (adjustable from 1 to 5)", min_value=1, max_value=min(5, len(class_names)), value=3)

# --------------------
# Main Demo Page
# --------------------
st.markdown("<h2 id='demo'>🖼️ Demo</h2>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("📂 Upload a rice image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<span class="highlight">📸 Uploaded Image</span>', unsafe_allow_html=True)
        st.image(img, use_container_width=True)

    with col2:
        resized_img = preprocess_pil_image(img, input_size)
        st.markdown(f'<span class="highlight">🔍 Resized Image ({input_size})</span>', unsafe_allow_html=True)
        st.image(resized_img[0], use_container_width=True)

    st.markdown("---")

    if st.button("🚀 Classify", use_container_width=True):
        with st.spinner("🔎 Analyzing image..."):
            results = predict_topk(model, img, class_names, k=top_k)

        st.success("✅ Prediction Completed!")

        for r in results:
            confidence_pct = int(r['confidence'] * 100)
            st.markdown(
                f"""
                <div class="prediction-box">
                    <h4>{r['label']}</h4>
                    <progress value="{confidence_pct}" max="100" style="width:100%"></progress>
                    <p>Confidence: {confidence_pct}%</p>
                </div>
                """,
                unsafe_allow_html=True
            )

# --------------------
# Footer
# --------------------
st.markdown('<div class="footer">By Siva</div>', unsafe_allow_html=True)
