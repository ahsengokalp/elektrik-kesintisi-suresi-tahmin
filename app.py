import streamlit as st
import pandas as pd
from datetime import datetime
import requests

# Streamlit sayfa ayarları
st.set_page_config(
    page_title="Elektrik Kesintisi Tahmini",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Arka plan ve metin stilleri
st.markdown(
    """
    <style>
    .main {
        background-color: #F5F5F5;
    }
    h1, h2, h3, h4, h5, h6 {
        text-align: center;
        color: #333333;
    }
    .stDataFrame {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #ddd;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Başlık
st.title("⚡ Elektrik Kesintisi Bilgileri ve Tahminler")

# Tahmin sınıfı belirleme fonksiyonu
def tahmin_sinifi_belirle(il, hava_durumu):
    """Hava durumu ve il bilgisine göre tahmin sınıfı belirler."""
    if hava_durumu in ['Fırtına', 'Yoğun Kar Yağışı']:
        return 'Çok Uzun'
    elif hava_durumu in ['Kar Yağışı', 'Sağanak Yağış']:
        return 'Uzun'
    elif hava_durumu in ['Bulutlu', 'Hafif Yağış']:
        return 'Orta'
    else:
        return 'Kısa'

# Kenar Çubuğu
st.sidebar.image("https://via.placeholder.com/300x100.png?text=Kesinti+Tahmini", use_container_width=True)
st.sidebar.title("🔍 Navigasyon")
menu = st.sidebar.radio("Menü", ["Veri Görüntüleme", "Tahmin Sonuçları", "Kesinti Süresi Tahmini"])

# Menüye göre içerik
if menu == "Veri Görüntüleme":
    st.subheader("📊 Elektrik Kesintisi Verileri")
    selected_date = st.date_input("Tarih Seçin", datetime.today())
    df = pd.read_csv('ADM_Merged_Final_Fuad.csv')  # Veri setini yükle
    df.columns = df.columns.str.strip()
    df['KESİNTİ BAŞLAMA TARİHİ VE ZAMANI (6)'] = pd.to_datetime(
        df['KESİNTİ BAŞLAMA TARİHİ VE ZAMANI (6)'], format='%d.%m.%Y %H:%M:%S', errors='coerce'
    )
    filtrelenmis_veriler = df[df['KESİNTİ BAŞLAMA TARİHİ VE ZAMANI (6)'].dt.date == selected_date]
    st.write(f"Seçilen Tarih: {selected_date}")
    st.dataframe(filtrelenmis_veriler)

elif menu == "Tahmin Sonuçları":
    st.subheader("🔍 Tahmin Sonuçları")
    results = {
        'Kısa': {'precision': 0.77, 'recall': 0.95, 'f1_score': 0.85, 'support': 982},
        'Orta': {'precision': 0.42, 'recall': 0.27, 'f1_score': 0.33, 'support': 272},
        'Uzun': {'precision': 0.44, 'recall': 0.07, 'f1_score': 0.12, 'support': 179},
        'Çok Uzun': {'precision': 0.60, 'recall': 0.66, 'f1_score': 0.63, 'support': 168},
    }
    for key, value in results.items():
        st.markdown(f"""
        ### {key} Kesinti için Sonuçlar
        - *Precision*: {value['precision']}
        - *Recall*: {value['recall']}
        - *F1-Score*: {value['f1_score']}
        - *Support*: {value['support']}
        """)

elif menu == "Kesinti Süresi Tahmini":
    st.subheader("⏳ Kesinti Süresi Tahmini")
    
    il = st.selectbox("İl Seçin", ["İzmir", "Aydın", "Muğla", "Manisa", "Denizli"])
    hava_durumu = st.selectbox("Hava Durumu Seçin", ["Açık", "Bulutlu", "Hafif Yağış", "Sağanak Yağış", "Kar Yağışı", "Yoğun Kar Yağışı", "Fırtına"])

    tarih = st.date_input("Kesinti Başlangıç Tarihini Seçin", datetime.today())
    saat = st.time_input("Kesinti Başlangıç Saatini Seçin", datetime.now().time())
    kesinti_tarihi_saat = pd.to_datetime(f"{tarih} {saat}")

    tahmin_sinifi = tahmin_sinifi_belirle(il, hava_durumu)
    tahmin_sureleri = {
        'Kısa': 30,
        'Orta': 60,
        'Uzun': 120,
        'Çok Uzun': 180,
    }

    tahmin_suresi = tahmin_sureleri[tahmin_sinifi]
    tahmin_bitis = kesinti_tarihi_saat + pd.Timedelta(minutes=tahmin_suresi)

    st.write(f"Seçilen İl: {il}")
    st.write(f"Seçilen Hava Durumu: {hava_durumu}")
    st.write(f"Tahmin Sınıfı: {tahmin_sinifi}")
    st.success(f"Tahmin Edilen Kesinti Bitiş Zamanı: {tahmin_bitis}")

# Alt bilgi
st.sidebar.info("Bu uygulama, elektrik kesintisi bilgilerini ve tahminlerini sunmak için geliştirilmiştir.")
