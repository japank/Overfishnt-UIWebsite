import streamlit as st
import datetime

st.set_page_config(
    page_title="Fishku - Contributor",
    page_icon="🐟",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# Made By Overfishn't Team."
    }
)

st.markdown("# Jadilah Kontributor")
st.write("Mari bantu Fishku dengan menjadi kontributor. Cukup isi form dibawah ini.")

name = st.text_input('Nama', 'Jevin Arda')
st.text_input('Domisili', 'Trenggalek')
st.time_input('Berangkat Melaut', datetime.time(17, 00))
st.time_input('Pulang Melaut', datetime.time(20, 00))
st.number_input('Hasil Tangkapan Tertinggi (kg)')
st.number_input('Hasil Tangkapan Terendah (kg)')
st.text_area('Apa masalah yang sering anda hadapi',
             'Terlalu banyak membuang sumber daya saat proses pencarian lokasi ikan berkumpul')

agree = st.checkbox(
    'Saya Setuju untuk mengikuti syarat dan ketentuan dari Fishku')

if agree:
    st.button('Submit', type="primary")
else:
    st.button('Submit', type="secondary")
