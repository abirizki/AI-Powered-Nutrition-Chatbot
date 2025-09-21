NutriBot: AI-Powered Nutrition Chatbot
English | Bahasa Indonesia
Overview
NutriBot is an AI-powered chatbot designed to provide nutrition analysis and healthy drink recommendations. Built with Python and Streamlit, it leverages the USDA FoodData Central API for accurate food nutrient data and the Google Gemini API for natural language processing. The app features interactive Plotly charts, bilingual support (English/Indonesian), and chat history export, making it a robust tool for health enthusiasts. Deployed on Streamlit Cloud, NutriBot showcases modern AI engineering with a clean, user-friendly interface.
🔗 Live Demo:[(https://ai-powered-nutrition-chatbot-jhqvfstroroehcqvfjyz6a.streamlit.app/)🔗 GitHub Repository: (https://github.com/abirizki/AI-Powered-Nutrition-Chatbot)🔗 
Features

Nutrition Analysis: Retrieves calorie, protein, fat, and carbohydrate data for foods using the USDA API.
Healthy Drink Suggestions: Recommends smoothies and juices tailored to diet goals (e.g., weight loss, muscle gain).
Interactive Visualizations: Displays nutrition data with modern Plotly bar charts.
Bilingual Support: Supports English and Indonesian for a broader user base.
Chat History Export: Allows users to download conversation history as a text file.
Responsive Design: Optimized for desktop and mobile, with a clean and intuitive UI inspired by modern health apps.

Tech Stack

Programming Language: Python
Framework: Streamlit
APIs:
Google Gemini API (NLP for chat responses)
USDA FoodData Central API (nutrition data)


Visualization: Plotly for interactive bar charts
Deployment: Streamlit Cloud
Design: Figma for UI prototyping

Setup Instructions
To run NutriBot locally, follow these steps:

Clone the repository:git clone (https://github.com/abirizki/AI-Powered-Nutrition-Chatbot)


Navigate to the project directory:cd nutribot


Create and activate a virtual environment:python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux


Install dependencies:pip install -r requirements.txt


Configure API keys in Streamlit Secrets or .env:[secrets]
GEMINI_API_KEY = "gemini-api-key"
USDA_API_KEY = "usda-api-key"


Run the app:streamlit run nutribot_app.py


Open http://localhost:8501 in your browser.

Requirements (requirements.txt):
streamlit
google-generativeai
requests
pandas
plotly

UI Design
NutriBot features a modern, minimalist UI inspired by health and wellness apps:

Header: Bold "NutriBot" title with an apple icon, reflecting a healthy lifestyle.
Dropdowns: Language (English/Indonesian) and diet goal selectors for personalized user experience.
Chat Interface: Clean chat bubbles with user input and bot responses, optimized for readability.
Nutrition Chart: Interactive Plotly bar charts displaying calorie, protein, fat, and carbohydrate data.
Export Button: Green-themed button for downloading chat history.

The UI was prototyped in Figma, ensuring a professional and responsive design. See the Figma prototype for details.
Screenshots

Main Page: Clean layout with header and dropdowns.
Chat Example: Nutrition analysis with Plotly chart.
Drink Suggestion: Healthy drink recommendation card.

Credits

USDA FoodData Central API: For nutrition data.
Google Gemini API: For natural language processing.
Streamlit: For rapid web app development.
Plotly: For interactive visualizations.
Figma: For UI design prototyping.


NutriBot: Chatbot Gizi Berbasis AI
Bahasa Indonesia | English
Ikhtisar
NutriBot adalah chatbot berbasis AI yang dirancang untuk menganalisis gizi makanan dan memberikan rekomendasi minuman sehat. Dibangun dengan Python dan Streamlit, aplikasi ini memanfaatkan USDA FoodData Central API untuk data gizi akurat dan Google Gemini API untuk pemrosesan bahasa alami. NutriBot menawarkan grafik interaktif dengan Plotly, dukungan multibahasa (Indonesia/Inggris), dan fitur ekspor riwayat chat, menjadikannya alat ideal untuk penggemar kesehatan. Aplikasi ini dideploy di Streamlit Cloud dengan antarmuka yang modern dan ramah pengguna.
🔗 Demo Langsung: [(https://ai-powered-nutrition-chatbot-jhqvfstroroehcqvfjyz6a.streamlit.app/)]🔗 Repositori GitHub: https://github.com/abirizki/AI-Powered-Nutrition-Chatbot🔗 
Fitur

Analisis Gizi: Menampilkan data kalori, protein, lemak, dan karbohidrat dari makanan menggunakan USDA API.
Rekomendasi Minuman Sehat: Menyarankan smoothie dan jus sesuai tujuan diet (misalnya, turun berat badan, tambah otot).
Visualisasi Interaktif: Grafik batang Plotly untuk data gizi.
Dukungan Multibahasa: Mendukung bahasa Indonesia dan Inggris untuk menjangkau pengguna yang lebih luas.
Ekspor Riwayat Chat: Pengguna dapat mengunduh riwayat percakapan sebagai file teks.
Desain Responsif: Dioptimalkan untuk desktop dan mobile dengan antarmuka yang bersih dan intuitif.

Teknologi yang Digunakan

Bahasa Pemrograman: Python
Framework: Streamlit
API:
Google Gemini API (NLP untuk respons chat)
USDA FoodData Central API (data gizi)


Visualisasi: Plotly untuk grafik batang interaktif
Deployment: Streamlit Cloud
Desain: Figma untuk prototipe UI

Petunjuk Setup
Untuk menjalankan NutriBot secara lokal:

Clone repositori:git clone https://github.com/abirizki/AI-Powered-Nutrition-Chatbot


Masuk ke direktori proyek:cd nutribot


Buat dan aktifkan virtual environment:python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux


Install dependensi:pip install -r requirements.txt


Konfigurasi API key di Streamlit Secrets atau .env:[secrets]
GEMINI_API_KEY = "gemini-api-key"
USDA_API_KEY = "usda-api-key"


Jalankan aplikasi:streamlit run nutribot_app.py


Buka http://localhost:8501 di browser Anda.

Dependensi (requirements.txt):
streamlit
google-generativeai
requests
pandas
plotly

Desain UI
NutriBot memiliki antarmuka modern dan minimalis yang terinspirasi dari aplikasi kesehatan:

Header: Judul "NutriBot" dengan ikon apel, mencerminkan gaya hidup sehat.
Dropdown: Pilihan bahasa (Indonesia/Inggris) dan tujuan diet untuk pengalaman personal.
Antarmuka Chat: Gelembung chat yang bersih untuk input pengguna dan respons bot.
Grafik Gizi: Grafik batang interaktif Plotly untuk menampilkan data kalori, protein, lemak, dan karbohidrat.
Tombol Ekspor: Tombol bertema hijau untuk mengunduh riwayat chat.

UI dirancang menggunakan Figma untuk memastikan desain profesional dan responsif. Lihat prototipe Figma untuk detailnya.
Screenshot

Halaman Utama: Tata letak bersih dengan header dan dropdown.
Contoh Chat: Analisis gizi dengan grafik Plotly.
Rekomendasi Minuman: Kartu rekomendasi minuman sehat.

Kredit

USDA FoodData Central API: Untuk data gizi.
Google Gemini API: Untuk pemrosesan bahasa alami.
Streamlit: Untuk pengembangan aplikasi web cepat.
Plotly: Untuk visualisasi interaktif.
Figma: Untuk prototipe desain UI.

