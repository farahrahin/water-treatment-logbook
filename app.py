import streamlit as st
import pandas as pd
from datetime import date
import io

st.set_page_config(layout="wide")
st.title("💧 Water Treatment Plant Logbook (E-Form)")

# ===== HEADER =====
st.header("📋 Maklumat Umum")

col1, col2, col3 = st.columns(3)

with col1:
    plant = st.selectbox("Loji Air", ["Bukit Ubi", "Panching"])

with col2:
    tarikh = st.date_input("Tarikh", date.today())

with col3:
    no_siri = st.text_input("No Siri")

# ===== SHIFT =====
st.header("🔄 Data Entry")

col_shift = st.columns(2)

with col_shift[0]:
    shift = st.selectbox("Shift", ["Shift 1", "Shift 2", "Shift 3"])

with col_shift[1]:
    masa = st.selectbox("Masa", ["8.00", "12.00", "4.00", "8.00"])

st.divider()

# ===== AIR MENTAH =====
st.subheader("🌊 Air Mentah")
c1,c2,c3,c4,c5,c6,c7,c8 = st.columns(8)

flow = c1.number_input("Flow")
raw_ph = c2.number_input("pH")
raw_ntu = c3.number_input("NTU")
raw_warna = c4.number_input("Warna")
raw_al = c5.number_input("Al")
raw_fe = c6.number_input("Fe")
raw_mn = c7.number_input("Mn")
raw_cl = c8.number_input("Cl")

# ===== TANGKI MENDAP =====
st.subheader("🧪 Tangki Mendap")
c1,c2,c3 = st.columns(3)

medap_ph = c1.number_input("pH (Medap)")
medap_ntu = c2.number_input("NTU (Medap)")
medap_warna = c3.number_input("Warna (Medap)")

# ===== SELEPAS TAPIS =====
st.subheader("🧪 Selepas Tapis")
c1,c2,c3 = st.columns(3)

filter_ph = c1.number_input("pH (Filter)")
filter_ntu = c2.number_input("NTU (Filter)")
filter_warna = c3.number_input("Warna (Filter)")

# ===== AIR BERSIH =====
st.subheader("💧 Air Bersih")
c1,c2,c3,c4,c5,c6,c7 = st.columns(7)

clean_ph = c1.number_input("pH (Clean)")
clean_ntu = c2.number_input("NTU (Clean)")
clean_warna = c3.number_input("Warna (Clean)")
clean_fe = c4.number_input("Fe (Clean)")
clean_al = c5.number_input("Al (Clean)")
clean_mn = c6.number_input("Mn (Clean)")
clean_cl2 = c7.number_input("Cl₂")

# ===== DOSING =====
st.subheader("⚗️ Dosing")
c1,c2,c3,c4 = st.columns(4)

kapur_pre = c1.number_input("Kapur (Pre)")
kapur_post = c2.number_input("Kapur (Post)")
koagulan = c3.number_input("Koagulan")
polimer = c4.number_input("Polimer")

# ===== KLORIN =====
st.subheader("🧴 Klorin")
c1,c2 = st.columns(2)

klorin_pre = c1.number_input("Klorin (Pre)")
klorin_post = c2.number_input("Klorin (Post)")

# ===== FLUORIDE =====
fluoride = st.number_input("🧪 Fluoride")

# ===== PARAS AIR =====
paras_air = st.number_input("📏 Paras Air")

st.divider()

# ===== SAVE BUTTON =====
if st.button("💾 Save Data"):

    data = {
        "Plant": plant,
        "Date": tarikh,
        "No_Siri": no_siri,
        "Shift": shift,
        "Masa": masa,

        "Flow": flow,
        "Raw_pH": raw_ph,
        "Raw_NTU": raw_ntu,
        "Raw_Warna": raw_warna,
        "Raw_Al": raw_al,
        "Raw_Fe": raw_fe,
        "Raw_Mn": raw_mn,
        "Raw_Cl": raw_cl,

        "Medap_pH": medap_ph,
        "Medap_NTU": medap_ntu,
        "Medap_Warna": medap_warna,

        "Filter_pH": filter_ph,
        "Filter_NTU": filter_ntu,
        "Filter_Warna": filter_warna,

        "Clean_pH": clean_ph,
        "Clean_NTU": clean_ntu,
        "Clean_Warna": clean_warna,
        "Clean_Fe": clean_fe,
        "Clean_Al": clean_al,
        "Clean_Mn": clean_mn,
        "Clean_Cl2": clean_cl2,

        "Kapur_Pre": kapur_pre,
        "Kapur_Post": kapur_post,
        "Koagulan": koagulan,
        "Polimer": polimer,

        "Klorin_Pre": klorin_pre,
        "Klorin_Post": klorin_post,

        "Fluoride": fluoride,
        "Paras_Air": paras_air
    }

    df = pd.DataFrame([data])

    # Convert to Excel (NO FILE SAVING)
    buffer = io.BytesIO()
    df.to_excel(buffer, index=False, engine='openpyxl')

    st.success("✅ Data ready!")

    st.download_button(
        label="⬇️ Download Excel",
        data=buffer,
        file_name="WTP_data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    
