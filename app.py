import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

NAMA = "Mohammad Alif Rachman Setiaji"
NIM = "241041009"

st.set_page_config(page_title="Kasus 1 - Penjualan", layout="wide")
st.title("Kasus 1: Dataset Operasional Penjualan")
st.caption(f"Nama: {NAMA}  |  NIM: {NIM}")

# ---- Data ----
rng = np.random.default_rng(42)
produk = {"Laptop": ("Elektronik", 8500000), "Buku": ("Pendidikan", 75000),
          "Mouse": ("Elektronik", 150000), "Pulpen": ("Pendidikan", 5000),
          "Meja Belajar": ("Furnitur", 900000), "Monitor": ("Elektronik", 2200000)}
rows = []
for tgl in pd.date_range("2024-01-01", periods=30):
    p = rng.choice(list(produk))
    rows.append([p, produk[p][0], produk[p][1], int(rng.integers(10, 150)), tgl])
df = pd.DataFrame(rows, columns=["Produk", "Kategori", "Harga (Rp)", "Jumlah Terjual", "Tanggal"])

st.subheader("Data")
st.dataframe(df, use_container_width=True)

# ---- Diagnostik tipe data ----
st.subheader("Diagnostik Tipe Data")
st.table(pd.DataFrame({
    "Kolom": df.columns,
    "Tipe": ["Kategorik", "Kategorik", "Numerik (Kontinu)", "Numerik (Diskrit)", "Waktu"],
    "Skala": ["Nominal", "Nominal", "Rasio", "Rasio", "Interval"],
    "Visualisasi": ["Bar/Pie Chart", "Bar/Pie Chart", "Histogram", "Bar Chart/Histogram", "Line Chart"],
}))

# ---- Visualisasi ----
c1, c2 = st.columns(2)
c1.plotly_chart(px.bar(df.groupby("Produk", as_index=False)["Jumlah Terjual"].sum(),
                x="Produk", y="Jumlah Terjual", title="Total Terjual per Produk (Bar - Nominal)"), use_container_width=True)
c2.plotly_chart(px.pie(df, names="Kategori", title="Proporsi Kategori (Pie - Nominal)"), use_container_width=True)
c3, c4 = st.columns(2)
c3.plotly_chart(px.histogram(df, x="Harga (Rp)", nbins=10, title="Distribusi Harga (Histogram - Rasio Kontinu)"), use_container_width=True)
c4.plotly_chart(px.line(df.sort_values("Tanggal"), x="Tanggal", y="Jumlah Terjual", title="Tren Penjualan (Line - Waktu/Interval)"), use_container_width=True)