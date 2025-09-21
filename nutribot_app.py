import streamlit as st
import google.generativeai as genai
import requests
import json
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Konfigurasi API key
GEMINI_API_KEY = "AIzaSyDLXsUpDcx0e25nTNGIqxuSZeQK6xwz_mk"  # Gemini API key
USDA_API_KEY = "BDxxjtMOcp6UqIOg7NFAiNMmufbhiDJoVPEWkkov"  # USDA API key
genai.configure(api_key=GEMINI_API_KEY)

# Fungsi untuk fetch data gizi dari USDA API
def get_nutrition_data(food_query):
    try:
        search_url = "https://api.nal.usda.gov/fdc/v1/foods/search"
        params = {
            "query": food_query,
            "pageSize": 1,
            "api_key": USDA_API_KEY
        }
        response = requests.get(search_url, params=params)
        response.raise_for_status()
        data = response.json()
        if data["foods"]:
            food = data["foods"][0]
            nutrients = food.get("foodNutrients", [])
            nutrition_info = {
                "Kalori (kcal)": next((n["value"] for n in nutrients if n["nutrientName"] == "Energy"), "Tidak tersedia"),
                "Protein (g)": next((n["value"] for n in nutrients if n["nutrientName"] == "Protein"), "Tidak tersedia"),
                "Lemak (g)": next((n["value"] for n in nutrients if n["nutrientName"] == "Total lipid (fat)"), "Tidak tersedia"),
                "Karbohidrat (g)": next((n["value"] for n in nutrients if n["nutrientName"] == "Carbohydrate, by difference"), "Tidak tersedia"),
            }
            return nutrition_info
        return None
    except Exception as e:
        st.error(f"Gagal mengambil data gizi: {str(e)}")
        return None

# Fungsi untuk rekomendasi minuman sehat
def suggest_healthy_drink(diet_goal=None, language="id"):
    drinks = [
        {"name": "Smoothie Bayam-Nanas", "ingredients": "Bayam, nanas, pisang, air kelapa", "calories": 150, "benefit": "Kaya vitamin C dan serat, cocok untuk detoks."},
        {"name": "Jus Beetroot-Wortel", "ingredients": "Beetroot, wortel, apel, jahe", "calories": 120, "benefit": "Meningkatkan stamina dan kesehatan jantung."},
        {"name": "Smoothie Protein Cokelat", "ingredients": "Susu almond, pisang, bubuk protein, kakao", "calories": 200, "benefit": "Mendukung pembentukan otot setelah olahraga."},
        {"name": "Infused Water Lemon-Mint", "ingredients": "Lemon, daun mint, air", "calories": 10, "benefit": "Hidrasi rendah kalori dan menyegarkan."}
    ]
    if language == "en":
        drinks = [
            {"name": "Spinach-Pineapple Smoothie", "ingredients": "Spinach, pineapple, banana, coconut water", "calories": 150, "benefit": "Rich in vitamin C and fiber, great for detox."},
            {"name": "Beetroot-Carrot Juice", "ingredients": "Beetroot, carrot, apple, ginger", "calories": 120, "benefit": "Boosts stamina and heart health."},
            {"name": "Chocolate Protein Smoothie", "ingredients": "Almond milk, banana, protein powder, cocoa", "calories": 200, "benefit": "Supports muscle building post-workout."},
            {"name": "Lemon-Mint Infused Water", "ingredients": "Lemon, mint leaves, water", "calories": 10, "benefit": "Low-calorie hydration and refreshing."}
        ]
    if diet_goal == "Turun Berat Badan" or diet_goal == "Weight Loss":
        drinks = [d for d in drinks if d["calories"] < 150]
    elif diet_goal == "Tambah Otot" or diet_goal == "Muscle Gain":
        drinks = [d for d in drinks if d["calories"] >= 150]
    return drinks[0] if drinks else {"name": "Air Putih", "ingredients": "Air", "calories": 0, "benefit": "Hidrasi terbaik!" if language == "id" else "Best hydration!"}

# Fungsi untuk generate respons dengan Gemini
def generate_response(user_input, chat_history, nutrition_data, drink_suggestion, language="id"):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"""
    Kamu adalah NutriBot, chatbot gizi santai dan ramah. Gunakan bahasa {'Indonesia' if language == 'id' else 'Inggris'}.
    Riwayat percakapan: {chat_history}
    Input pengguna: {user_input}
    Data gizi (jika ada): {json.dumps(nutrition_data, ensure_ascii=False)}
    Rekomendasi minuman: {json.dumps(drink_suggestion, ensure_ascii=False)}
    Berikan respons relevan, tambahkan saran minuman sehat atau tips gizi jika cocok. Jika tidak ada data gizi, tetap berikan jawaban ramah. Maksimal 500 kata.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Maaf, ada masalah dengan AI: {str(e)}. Coba lagi nanti!" if language == "id" else f"Sorry, there was an issue with the AI: {str(e)}. Try again later!"

# UI Streamlit
st.set_page_config(page_title="NutriBot", page_icon="🍎", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #f0f4f8; padding: 20px; }
    .stButton>button { background-color: #4CAF50; color: white; border-radius: 5px; }
    .stSelectbox { background-color: #ffffff; border-radius: 5px; }
    .stChatMessage { border-radius: 10px; padding: 10px; }
    .title { color: #2E7D32; font-size: 2.5em; text-align: center; }
    .subtitle { color: #616161; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="title">NutriBot: Asisten Gizi dan Minuman Sehat</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Tanya tentang gizi makanan (misalnya, "Berapa kalori di apel?") atau minta saran minuman sehat!</p>', unsafe_allow_html=True)

# Pilih bahasa dan tujuan diet
col1, col2 = st.columns(2)
with col1:
    language = st.selectbox("Pilih Bahasa / Language", ["Bahasa Indonesia", "English"], key="language")
lang_code = "id" if language == "Bahasa Indonesia" else "en"
with col2:
    diet_goal = st.selectbox(
        "Tujuan Diet / Diet Goal" if lang_code == "id" else "Diet Goal",
        ["Tidak Ada", "Turun Berat Badan", "Tambah Otot"] if lang_code == "id" else ["None", "Weight Loss", "Muscle Gain"],
        key="diet_goal"
    )

# Inisialisasi session state untuk memory chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan riwayat chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input pengguna
if prompt := st.chat_input("Tulis pertanyaanmu / Type your question..."):
    # Tampilkan input user
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Proses: Cari data gizi dan saran minuman
    nutrition_data = get_nutrition_data(prompt) if any(kw in prompt.lower() for kw in ["kalori", "gizi", "nutrisi", "calorie", "nutrition"]) else None
    drink_suggestion = suggest_healthy_drink(None if diet_goal == ("Tidak Ada" if lang_code == "id" else "None") else diet_goal, lang_code)

    # Generate grafik jika ada data gizi
    if nutrition_data and all(isinstance(v, (int, float)) for v in nutrition_data.values()):
        chart_data = {
            "labels": list(nutrition_data.keys()),
            "values": [float(v) for v in nutrition_data.values()]
        }
        st.markdown(f"### {'Grafik Gizi' if lang_code == 'id' else 'Nutrition Chart'}")
        fig = go.Figure(data=[
            go.Bar(
                x=chart_data["labels"],
                y=chart_data["values"],
                marker_color=["#4CAF50", "#2196F3", "#FF9800", "#F44336"],
                marker_line_color=["#388E3C", "#1976D2", "#F57C00", "#D32F2F"],
                marker_line_width=1
            )
        ])
        fig.update_layout(
            yaxis_title="Jumlah" if lang_code == "id" else "Amount",
            xaxis_title="Nutrisi" if lang_code == "id" else "Nutrients",
            yaxis=dict(range=[0, max(chart_data["values"]) * 1.2]),
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    # Generate respons dengan Gemini
    chat_history = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages])
    with st.chat_message("assistant"):
        response = generate_response(prompt, chat_history, nutrition_data, drink_suggestion, lang_code)
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Tombol untuk ekspor riwayat chat
if st.button("Unduh Riwayat Chat / Download Chat History"):
    chat_text = "\n".join([f"{m['role'].capitalize()}: {m['content']}" for m in st.session_state.messages])
    st.download_button(
        label="Unduh sebagai Teks / Download as Text",
        data=chat_text,
        file_name=f"nutribot_chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
        mime="text/plain"
    )