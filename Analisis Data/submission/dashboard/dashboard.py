# Import library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style="dark")

# Load dataset
df = pd.read_csv("main_data.csv")

# Set header
st.header("Proyek Analisis Data: Air Quality")
st.subheader(
    "Nama: Kevin Arnandes\n Email: kevinarnandes21@gmail.com\n ID Dicoding: kevinarnandes"
)

# Visualisasi Tingkat Polusi Udara tahun ke tahun
st.subheader("Rata rata polusi udara setiap tahun pada seluruh Stasiun")

# Hitung rata-rata polusi udara untuk setiap tahun
df["year"] = pd.to_datetime(df["date"]).dt.year  # Menambahkan kolom tahun
avg_pollution_by_year = df.groupby("year")[
    ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
].mean()

# Plot
fig, ax = plt.subplots(figsize=(16, 8))
for column in avg_pollution_by_year.columns:
    ax.plot(avg_pollution_by_year.index, avg_pollution_by_year[column], label=column)

ax.set_title("Tren Perubahan Polusi Udara dari Tahun ke Tahun")
ax.set_xlabel("Tahun")
ax.set_ylabel("Rata-rata Tingkat Polusi Udara")
ax.legend()
ax.grid(True)

st.pyplot(fig)


# Visualisasi untuk melihat Tingkat Polusi Udara Setiap Station
st.subheader("Tingkat Polusi Udara Masing Masing Station")

# List stasiun
stations = [
    "Aotizhongxin",
    "Changping",
    "Dingling",
    "Dongsi",
    "Guanyuan",
    "Gucheng",
    "Huairou",
    "Nongzhanguan",
    "Shunyi",
    "Tiantan",
    "Wanliu",
    "Wanshouxigong",
]

# Widget select stasiun
selected_station = st.selectbox("Pilih Stasiun", stations)

# Hitung rata-rata polusi udara untuk setiap tanggal dan stasiun
avg_pollution_by_date_station = df.groupby(["date", "station"])[
    ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
].mean()

# Plot
fig, ax = plt.subplots(figsize=(16, 8))  # Menggunakan format awal untuk membuat plot

data_station = avg_pollution_by_date_station.xs(selected_station, level="station")
for column in data_station.columns:
    ax.plot(
        data_station.index, data_station[column], label=f"{selected_station} - {column}"
    )

ax.set_title(f"Pola Musiman Tingkat Polusi Udara di Stasiun {selected_station}")
ax.set_xlabel("Tanggal")
ax.set_ylabel("Rata-rata Tingkat Polusi Udara")
ax.legend()
ax.grid(True)

# Set interval ticks pada sumbu x
num_ticks = 6  # Ganti dengan jumlah yang sesuai untuk interval yang diinginkan
xticks = ax.get_xticks()
date_index = pd.to_datetime(data_station.index)
tick_indices = range(0, len(date_index), len(date_index) // num_ticks)
ax.set_xticks(xticks[:: len(xticks) // num_ticks])
ax.set_xticklabels([date_index[i].strftime("%Y-%m-%d") for i in tick_indices])

ax.tick_params(axis="x", rotation=45)
st.pyplot(fig)


st.caption("Dicoding Submission ")
