# -*- coding: utf-8 -*-
"""[Submission] Destination Jogja Recommendation use Content Based Filtering

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zWKTJPJDi6NDlpbXhen08DatWP5lnD4w

# Proyek Akhir Machine Learning: Sistem Rekomendasi Buku

- **Nama:** Kevin Arnandes
- **Email:** kevinarnandes21@gmail.com
- **ID Dicoding:** kevinarnandes

# Data Collection

## Import libary
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""## Gathering Data"""

# Load Dataset
url_tour = "https://raw.githubusercontent.com/Vinzzztty/playground-data-analyst/main/Dataset/pariwisata_jogja/tour.csv"
url_rating = "https://raw.githubusercontent.com/Vinzzztty/playground-data-analyst/main/Dataset/pariwisata_jogja/tour_rating.csv"
url_user = "https://raw.githubusercontent.com/Vinzzztty/playground-data-analyst/main/Dataset/pariwisata_jogja/user.csv"

tour = pd.read_csv(url_tour)
rating = pd.read_csv(url_rating)
user = pd.read_csv(url_user)

print('Jumlah data tempat wisata: ', len(tour.Place_Id.unique()))
print('Jumlah data rating tempat wisata: ', len(rating.Place_Id.unique()))
print('Jumlah data user: ', len(user.User_Id.unique()))

"""# Data Understanding

## Univariate Exploratory Data Analysis

### Tour Variabel
"""

tour.info()

tour.shape

print("Banyak data: ", len(tour.Place_Id.unique()))
print("Kategori tempat wisata: ", tour.Category.unique())

"""### Rating Variabel"""

rating.head()

rating.describe()

rating.Place_Ratings.value_counts()

"""### User Variabel"""

user.head()

user.describe()

"""Rata rata umur adalah 28 tahun

# Data Pre Processing

## Menggabungkan seluruh rating wisata
"""

# Menggabungkan seluruh Place_Id pada kategori Tour
tour_all = np.concatenate((
    tour.Place_Id.unique(),
    rating.Place_Id.unique(),
))

# Mengurutkan data dan menghapus data yang sama
tour_all = np.sort(np.unique(tour_all))

print('Jumlah seluruh data wisata berdasarkan Place_Id: ', len(tour_all))

"""## Menggabungkan Seluruh User"""

# Menggabungkan seluruh userID
user_all = np.concatenate((
    user.User_Id.unique(),
    rating.User_Id.unique(),
))

# Menghapus data yang sama kemudian mengurutkannya
user_all = np.sort(np.unique(user_all))

print('Jumlah seluruh user: ', len(user_all))

"""## Mengetahui Jumlah Rating"""

tour.groupby('Place_Id').sum()

"""## Menggabungkan Data dengan Fitur Nama Tempat"""

# Definisikan dataframe rating ke dalam variabel all_tour_rate
all_tour_rate = rating

all_tour_rate

# Menggabungkan all_tour_rate dengan dataframe tour berdasarkan Place_Id
all_tour = pd.merge(all_tour_rate, tour[['Place_Id', 'Place_Name', 'Category', 'Rating']], on='Place_Id', how='left')

all_tour

"""# Data Preparation

## Mencari tahu apakah ada Missing Value
"""

all_tour.isnull().sum()

"""## Melihat kategori wisata"""

all_tour.Category.unique()

"""## Preparation Data"""

# Membuat variabel preparation yang berisi dataframe all_tour kemudian diurutkan berdasarkan Place_Id
preparation = all_tour

preparation.sort_values('Place_Id')

"""### Menghapus data Duplikat"""

# Melihat data duplikat
preparation.duplicated().sum()

# Menghapus data duplikat
preparation = preparation.drop_duplicates('Place_Id')

preparation

"""### Mengkonversi data series menjadi bentuk list"""

# Mengonversi data series Place_Id menjadi dalam bentuk list
destination_id = preparation['Place_Id'].tolist()

# Mengonversi data series Place_Name menjadi dalam bentuk list
destination_name = preparation['Place_Name'].tolist()

# Mengonversi data series Category menjadi dalam bentuk list
destination_category = preparation['Category'].tolist()

print(len(destination_id))
print(len(destination_name))
print(len(destination_category))

# Membuat dictionary untuk data destination_id, destination_name, destination_category
destination = pd.DataFrame({
    'id': destination_id,
    'destination_name': destination_name,
    'category': destination_category
})
destination

"""# Model Development dengan Content Based Filtering"""

data = destination
data.sample(5)

"""## TF-IDF Vectorizer"""

# Inisialisasi TFIDFVectorizer
tf = TfidfVectorizer()

# Melakukan perhitungan idf pada data category
tf.fit(data['category'])

# Mapping array dari fitur inedx integer ke fitur utama
tf.get_feature_names_out()

# Melakukan Fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tf.fit_transform(data['category'])

# Melihat ukuran matrix tfidf
tfidf_matrix.shape

# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()

"""### Membuat dataframe tf-idf matrix"""

# Membuat dataframe untuk melihat tf-idf matrix
# Kolom diisi dengan jenis masakan
# Baris diisi dengan nama resto

pd.DataFrame(
    tfidf_matrix.todense(),
    columns=tf.get_feature_names_out(),
    index=data.destination_name
).sample(8, axis=1).sample(10, axis=0)

"""## Cosine Similarity

### Menghitung cosine similarity pada matrix tf-idf
"""

# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

"""### Melihat matrix kesamaan setiap destinasi"""

# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa nama resto
cosine_sim_df = pd.DataFrame(cosine_sim, index=data['destination_name'], columns=data['destination_name'])
print('Shape:', cosine_sim_df.shape)

# Melihat similarity matrix pada setiap resto
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""# Model Evaluation

## Mendapatkan Rekomendasi
"""

def destination_recommendations(nama_destinasi, similarity_data=cosine_sim_df, items=data[['destination_name', 'category']], k=10):
  """
  Rekomendasi Destinasi Wisata berdasarkan kemiripan dataframe

  Parameter:
  ---
  nama_destinasi : tipe data string (str)
                Nama Destinasi (index kemiripan dataframe)
  similarity_data : tipe data pd.DataFrame (object)
                      Kesamaan dataframe, simetrik, dengan destinasi sebagai
                      indeks dan kolom
  items : tipe data pd.DataFrame (object)
            Mengandung kedua nama dan fitur lainnya yang digunakan untuk mendefinisikan kemiripan
  k : tipe data integer (int)
        Banyaknya jumlah rekomendasi yang diberikan
  ---


  Pada index ini, kita mengambil k dengan nilai similarity terbesar
  pada index matrix yang diberikan (i).
  """

  index = similarity_data.loc[:,nama_destinasi].to_numpy().argpartition(
      range(-1, -k, -1))

  closest = similarity_data.columns[index[-1:-(k+2):-1]]

  closest = closest.drop(nama_destinasi, errors='ignore')

  return pd.DataFrame(closest).merge(items).head(k)

data[data.destination_name.eq('Candi Sewu')]

# Mendapatkan rekomendasi destinasi yang mirip dengan Candi Sewu
destination_recommendations('Candi Sewu')