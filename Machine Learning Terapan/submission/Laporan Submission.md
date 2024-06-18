# Laporan Proyek Machine Learning - Kevin Arnandes

### Proyek Machine Learning: Sistem Rekomendasi Wisata Di Jogja dengan Content Based Filtered

-   **Nama:** Kevin Arnandes
-   **Email:** kevinarnandes21@gmail.com
-   **ID Dicoding:** kevinarnandes

## 1. Project Overview

### Latar Belakang

Pariwisata memiliki peranan penting dalam ekonomi Indonesia, dengan kekayaan alam dan keragaman budaya menjadi daya tarik utama bagi pengunjung. Yogyakarta, salah satu destinasi terkenal di Indonesia, menarik jutaan pengunjung setiap tahunnya. Data statistik dari tahun 2023 menunjukkan peningkatan jumlah pengunjung yang mengunjungi Jogja, dengan berbagai objek wisata dari alam hingga budaya.

Saat merencanakan perjalanan, pemilihan destinasi menjadi hal utama yang dipertimbangkan. Beberapa pengunjung memilih menggunakan jasa agen wisata atau pemandu, sementara yang lain lebih memilih merencanakan sendiri. Namun, merencanakan sendiri sering memakan waktu karena proses pengumpulan informasi yang intensif. Meskipun demikian, kelebihan informasi sering membuat pengunjung bingung dalam memilih destinasi yang sesuai dengan preferensi mereka.

Dalam konteks ini, peran Content Based Filtering sangat penting. Teknologi ini dapat membantu pengunjung dengan memberikan rekomendasi tempat wisata di Jogja berdasarkan preferensi individu mereka, seperti minat dalam wisata alam atau budaya. Dengan menggunakan algoritma yang memeriksa kesesuaian antara profil pengunjung dan karakteristik tempat wisata, Content Based Filtering dapat menjadi solusi yang efektif untuk membantu pengunjung menjelajahi berbagai pilihan yang ada.

## 2. Business Understanding

### Problem Statements

-   Bagaimana mengatasi kesulitan wisatawan dalam memilih destinasi wisata yang sesuai dengan preferensi mereka di Yogyakarta, dengan menggunakan metode _content-based filtering_ sebagai solusi untuk memberikan rekomendasi yang akurat dan memuaskan.

Ketika merencanakan perjalanan, wisatawan dihadapkan pada banyak pertimbangan, termasuk memilih destinasi atau tempat wisata yang sesuai. Beberapa orang mengandalkan agen wisata atau pemandu wisata, sementara yang lain lebih suka merencanakan sendiri perjalanan mereka. Namun, merencanakan sendiri seringkali memerlukan waktu lebih lama karena wisatawan perlu mengumpulkan banyak informasi. Informasi yang berlimpah kadang membuat wisatawan bingung dalam memilih destinasi wisata yang tepat sesuai keinginan mereka.

-   Sejauh mana metode _content-based filtering_ dapat memberikan rekomendasi destinasi wisata yang akurat dan sesuai dengan preferensi wisatawan di Yogyakarta, dengan mempertimbangkan kompleksitas fitur yang digunakan dalam sistem rekomendasi serta keterbatasan dalam pengumpulan data yang tersedia.

Faktor utama yang memengaruhi akurasi rekomendasi mungkin karena kompleksitas fitur yang digunakan dalam sistem rekomendasi. Selain itu, keterbatasan dalam pengumpulan data juga dapat berdampak pada tingkat akurasi rekomendasi.

### Goals

Pembuatan sistem rekomendasi destinasi wisata di Yogyakarta menggunakan metode _Content-Based Filtering_ bertujuan untuk:

-   Menguji Keefektifan Metode Content-Based Filtering: Evaluasi apakah metode content-based filtering dapat diterapkan secara efektif untuk merekomendasikan destinasi wisata di Yogyakarta. Ini melibatkan analisis kemampuan metode tersebut dalam memahami preferensi pengguna berdasarkan fitur-fitur dan karakteristik destinasi wisata.
-   Menilai Ketepatan Rekomendasi: Memastikan bahwa sistem rekomendasi dapat memberikan rekomendasi destinasi wisata di Yogyakarta yang sesuai dengan preferensi dan kebutuhan pengguna. Hal ini mencakup pengoptimalan pemilihan fitur-fitur yang relevan dan peningkatan kemampuan sistem dalam menyesuaikan rekomendasi dengan preferensi individual pengguna.

Dengan mencapai tujuan ini, diharapkan sistem rekomendasi dapat menjadi sumber informasi yang berguna dan dapat diandalkan bagi pengguna yang tertarik untuk menjelajahi destinasi wisata di Yogyakarta, serta meningkatkan pengalaman perjalanan mereka dengan rekomendasi yang akurat dan bermakna.

Adapun manfaat dari sistem rekomendasi destinasi wisata di Yogyakarata

-   Eksplorasi Destinasi yang Lebih _Divers_: Sistem rekomendasi akan mendorong pengguna untuk menjelajahi berbagai destinasi wisata di Yogyakarta yang mungkin belum mereka ketahui sebelumnya, memperkaya pengalaman wisata mereka dengan variasi dan keunikan yang beragam.
-   Efisiensi Perencanaan Perjalanan: Pengguna dapat menghemat waktu dan usaha dalam merencanakan perjalanan mereka, karena sistem akan memberikan rekomendasi langsung berdasarkan preferensi mereka tanpa perlu melakukan pencarian manual yang memakan waktu.

### Solutions Statements

Solusi yang diajukan untuk mencapai tujuan pembuatan sistem rekomendasi destinasi wisata di Yogyakarta menggunakan metode _Content-Based Filtering_ melibatkan beberapa tahapan yang teliti dan terperinci:

-   Pemrosesan Data Awal: Analisis dan pemrosesan awal terhadap data yang akan digunakan, termasuk pemahaman struktur data dan identifikasi insight untuk informasi selanjutnya.
-   Implementasi Metode _Content-Based Filtering_: Pembangunan model sistem rekomendasi dengan memilih fitur relevan dan pengembangan algoritma rekomendasi.
-   Evaluasi Kualitas Rekomendasi: Pengukuran kualitas rekomendasi menggunakan metrik evaluasi Precision untuk mengukur akurasi dan relevansi rekomendasi.

## 3. Data Understanding

Dataset yang digunakan dalam proyek ini merupakan data tentang pariwisata jogja.

Dataset dapat di di unduh di: [Dataset Pariwisata Jogja](https://www.kaggle.com/datasets/saufan/dataset-pariwisata-yogyakarta)

Terdapat 3 dataset utama yaitu dataset tour, tour_rating, dan user.

-   tour: berisi tentang pariwisata di jogja dan memiliki 126 baris dataset
-   tour_rating: berisi tentang rating pariwisata di jogja dan memiliki 126 baris dataset
-   user: berisi tentang pengguna yang ikut berkontribusi dalam pembuatan dataset pariwista jogja dan memiliki 300 baris dataset

### Variabel variabel pada dataset tour adalah sebagai berikut:

-   Place_Id: id destinasi wisata
-   Place_Name: nama destinasi wisata
-   Description: deskripsi singkat destinasi wisata
-   Category: kategori wisata
-   City: nama kota destinasi wisata
-   Price: harga masuk tempat wisata
-   Rating: rating wisata dari angka 1 - 5
-   Time_Minutes: estimasi waktu yang dibutuhkan ke tempat wisata
-   Coordinate: koordinat lokasi wisata
-   Latitude: nilai latitude lokasi wisata
-   Longitude: nilai longitude lokasi wisata

#### Insight variabel dataset tour

-   Dataset tour memiliki total data sebanyak 126
-   Category:
    -   Memiliki data sebanyak 36 kategori Taman Hiburan
    -   Memiliki data sebanyak 30 kategori Budaya
    -   Memiliki data sebanyak 34 kategori Bahari
    -   Memiliki data sebanyak 23 kategori Cagar Alam
    -   Memiliki data sebanyak 3 kategori Pusat Perbelanjaan

### Variabel variabel pada dataset tour_rating adalah sebagai berikut:

-   User_Id: id user atau pengguna
-   Place_Id: id destinasi wisata
-   Place_Ratings: rating destinasi wisata

#### Insight variabel dataset tour_rating

-   Place_Ratings:
    -   Memiliki data sebanyak 622 rating 5 tempat wisata
    -   Memiliki data sebanyak 601 rating 4 tempat wisata
    -   Memiliki data sebanyak 589 rating 3 tempat wisata
    -   Memiliki data sebanyak 208 rating 2 tempat wisata
    -   Memiliki data sebanyak 89 rating 1 tempat wisata
-   Rata rata rating tempat wisata yang diberikan adalah 3

### Variabel variabel pada dataset user adalah sebagai berikut:

-   User_Id: id user atau pengguna
-   Location: lokasi user yang membantu dalam pembuatan dataset
-   Age: Umur user atau pengguna

#### Insight variabel dataset user

-   Rata rata umur pengguna yang berkontribusi dalam dataset inin adalah 28 tahun

### Pendalaman Data

-   Melakukan Univariate EDA seperti mendeskripsikan variabel
-   Mencari keterkaitan fitur id masing masing dataset

#### Mencari keterkaitan fitur id masing masing dataset

Dalam tahapan ini, dilakukan pencarian dan pemahaman terhadap keterkaitan fitur id antara setiap dataset yang akan digunakan, yaitu dataset tour, dataset rating, dan dataset user. Berikut adalah penjelasan lebih lanjut mengenai keterkaitan fitur id pada setiap dataset:

1. Dataset Tour: Dataset ini memiliki keterkaitan dengan dataset rating melalui kolom Place_Id. Setiap entitas dalam dataset tour, yang mewakili informasi tentang destinasi wisata, memiliki Place_Id yang unik. Place_Id ini akan digunakan sebagai kunci untuk mengaitkan informasi tentang destinasi wisata dengan penilaian yang diberikan oleh pengguna.
2. Dataset Rating: Dataset rating memiliki keterkaitan dengan dataset tour melalui kolom Place_Id. Setiap penilaian yang diberikan oleh pengguna terhadap destinasi wisata akan terkait dengan Place_Id dari destinasi tersebut. Ini memungkinkan untuk menghubungkan informasi tentang penilaian dengan informasi tentang destinasi wisata yang bersangkutan.
3. Dataset User: Dataset user memiliki keterkaitan dengan dataset rating melalui kolom User_Id. Setiap entitas dalam dataset user, yang mewakili informasi tentang pengguna, memiliki User_Id yang unik. User_Id ini akan digunakan sebagai kunci untuk mengaitkan informasi tentang pengguna dengan penilaian yang mereka berikan terhadap destinasi wisata.

Keterkaitan ini penting karena akan digunakan sebagai kunci dalam menggabungkan informasi dari ketiga dataset tersebut menjadi satu dataset yang lengkap. Dengan menggunakan kunci-kunci ini, informasi tentang destinasi wisata, penilaian pengguna, dan informasi tentang pengguna dapat diintegrasikan dengan tepat, sehingga memungkinkan analisis dan pemodelan yang lebih komprehensif tentang preferensi pengguna terhadap destinasi wisata di Yogyakarta.

## 4. Data Preparation

### Melihat Apakah ada _Missing Value_

Pada dataset ini tidak memiliki missing value yang berarti dataset ini dari awal sudah bersih.

### Menghapus data duplikat

Terdapat 23 data duplikat dalam dataset yang harus dihapus. Hal ini dapat dilakukan menggunakan fungsi drop_duplicates pada library pandas, dengan parameter 'Place Id'.

### Menggabungkan seluruh rating wisata

1. Menggabungkan Nilai Place_Id: Pada bagian ini, digunakan fungsi np.concatenate() untuk menggabungkan dua array yang berisi nilai-nilai Place_Id unik dari dataset tour dan dataset rating. Ini dilakukan dengan memanggil metode .unique() untuk mendapatkan nilai unik dari kolom Place_Id dalam setiap dataset.
2. Pengurutan Data: Setelah menggabungkan nilai-nilai Place_Id, dilakukan pengurutan data secara ascending menggunakan fungsi np.sort() untuk memastikan bahwa nilai-nilai tersebut terurut dengan baik.
3. Penghapusan Nilai yang Sama: Langkah terakhir adalah menghapus nilai-nilai yang sama dari array menggunakan fungsi np.unique() agar hanya nilai-nilai Place_Id yang unik yang tersisa.

### Menggabungkan seluruh User

1. Menggabungkan Nilai User_Id: Pada bagian ini, digunakan fungsi np.concatenate() untuk menggabungkan dua array yang berisi nilai-nilai User_Id unik dari dataset user dan dataset rating. Ini dilakukan dengan memanggil metode .unique() untuk mendapatkan nilai unik dari kolom User_Id dalam setiap dataset.
2. Pengurutan Data dan Penghapusan Nilai yang Sama: Setelah menggabungkan nilai-nilai User_Id, dilakukan pengurutan data secara ascending menggunakan fungsi np.sort() dan penghapusan nilai-nilai yang sama menggunakan fungsi np.unique() agar hanya nilai-nilai User_Id yang unik yang tersisa.

### Menggabungkan Dataframe Tour dengan Dataframe Rating

1. Definisi DataFrame: Pada bagian ini, dataframe rating disalin ke dalam variabel all_tour_rate untuk kemudian digunakan dalam proses penggabungan.
2. Penggabungan DataFrame: Selanjutnya, dataframe all_tour_rate digabungkan dengan dataframe tour berdasarkan kolom Place_Id menggunakan fungsi pd.merge(). Proses penggabungan ini akan menghasilkan dataframe baru yang berisi semua kolom dari dataframe all_tour_rate serta kolom Place_Name, Category, dan Rating dari dataframe tour. Penggabungan dilakukan dengan menggunakan metode left join (how='left') sehingga semua baris dari dataframe all_tour_rate akan tetap dipertahankan dalam hasil penggabungan.
3. Menampilkan DataFrame Hasil Penggabungan: DataFrame hasil penggabungan disimpan dalam variabel all_tour dan ditampilkan untuk dilihat strukturnya dan memastikan proses penggabungan berjalan dengan baik.

Penggabungan dataframe dilakukan dengan tujuan untuk menggabungkan informasi yang relevan dari dua atau lebih dataframe yang berbeda menjadi satu dataframe yang lengkap. Beberapa alasan atau tujuan dari penggabungan dataframe antara lain:

-   Mengintegrasikan Informasi: Penggabungan dataframe memungkinkan untuk mengintegrasikan informasi yang terdapat dalam dua atau lebih dataframe yang memiliki hubungan atau keterkaitan antar data. Dengan menggabungkan dataframe, kita dapat memperoleh dataset yang lebih lengkap yang menggabungkan berbagai aspek informasi.
-   Analisis Data yang Lebih Komprehensif: Dengan menggabungkan dataframe, kita dapat melakukan analisis data yang lebih komprehensif dengan mempertimbangkan berbagai aspek atau dimensi data yang berbeda. Ini memungkinkan untuk mendapatkan wawasan yang lebih dalam tentang data dan hubungan antara variabel-variabel yang berbeda.

### Membuat Dataframe destination

1. Pembuatan Variabel \*preparation:

    - Variabel _preparation_ dibuat dan diinisialisasi dengan nilai dataframe _all_tour_. Ini dilakukan untuk mempermudah pengelolaan dan manipulasi data yang akan dilakukan selanjutnya.

2. Pengurutan DataFrame Berdasarkan Place_Id:

    - Meskipun pengurutan dilakukan menggunakan fungsi `sort_values()`, hasilnya tidak disimpan kembali ke variabel _preparation_. Ini karena fungsi tersebut hanya mengembalikan dataframe yang diurutkan, tetapi tidak mempengaruhi dataframe asli kecuali jika parameter `inplace=True` disetel.

3. Konversi Data Series Menjadi List:

    - Data dari kolom-kolom tertentu dalam dataframe _preparation_ diambil dan dikonversi menjadi list. Kolom-kolom yang diambil meliputi 'Place_Id', 'Place_Name', dan 'Category'. Operasi ini dilakukan dengan menggunakan metode `.tolist()` pada data series yang relevan.

4. Pembuatan Dictionary untuk Data Destination:

    - Menggunakan data yang telah dikonversi menjadi list, dibuatlah sebuah dictionary yang mewakili informasi tentang destinasi wisata. Dictionary ini terdiri dari tiga kunci, yaitu 'id', 'destination*name', dan 'category', yang masing-masing berisi list dari \_destination_id*, _destination_name_, dan _destination_category_.

5. Penyimpanan Data dalam DataFrame _destination_:
    - Data dari dictionary _destination_ disimpan dalam sebuah dataframe baru yang disebut _destination_. DataFrame ini akan digunakan untuk menyimpan informasi yang akan digunakan dalam proses selanjutnya, seperti pembuatan model atau analisis data.

### Melakukan TF-IDF Vectorizer

1. Membuat copy dataframe destionation yang disimpan ke dalam variabel data
2. Inisialisasi TFIDFVectorizer:

    - Objek _tf_ dari kelas _TfidfVectorizer_ diinisialisasi. Objek ini akan digunakan untuk menghitung TF-IDF dari data kategori.

3. Perhitungan IDF pada Data Category:

    - Metode `.fit()` dari objek _tf_ dipanggil untuk menghitung nilai IDF (Inverse Document Frequency) dari data kategori. Ini akan menghasilkan representasi vektor dari setiap kata dalam kategori.

4. Mapping Array dari Fitur Index ke Fitur Utama:

    - Metode `.get_feature_names_out()` digunakan untuk mendapatkan daftar fitur utama yang terkait dengan setiap indeks fitur.

5. Fit dan Transformasi ke Bentuk Matrix:

    - Metode `.fit_transform()` dari objek _tf_ digunakan untuk melakukan perhitungan TF-IDF pada data kategori. Hasilnya adalah matriks TF-IDF yang akan digunakan dalam analisis selanjutnya.

6. Melihat Ukuran Matrix TFIDF:

    - Metode `.shape` digunakan untuk melihat ukuran matriks TF-IDF, yaitu jumlah baris dan kolom.

7. Konversi Vektor TF-IDF menjadi Matriks Dense:

    - Metode `.todense()` digunakan untuk mengonversi vektor TF-IDF dalam bentuk matriks sparse menjadi matriks dense.

8. Pembuatan DataFrame dari Matrix TF-IDF:

    - DataFrame baru dibuat dari matriks TF-IDF yang telah diubah menjadi matriks dense. Nama-nama kolomnya diambil dari daftar fitur utama yang diperoleh sebelumnya, sedangkan nama-nama barisnya diambil dari nama destinasi dalam dataframe _data_. Ini memberikan representasi yang lebih mudah dimengerti tentang hasil perhitungan TF-IDF.

    - Metode `.sample(8, axis=1).sample(10, axis=0)` digunakan untuk mengambil sampel acak delapan kolom dan sepuluh baris dari dataframe hasil, sehingga memberikan representasi yang lebih ringkas dan mudah dibaca.

## 5. Modeling

Cosine Similarity adalah metrik yang digunakan untuk mengukur seberapa mirip dua vektor dalam ruang berdimensi banyak. Metrik ini mengukur cosinus sudut antara dua vektor, di mana nilai cosinus sudut yang lebih besar menunjukkan kemiripan yang lebih tinggi antara dua vektor. Cosine Similarity sering digunakan dalam pemrosesan teks dan sistem rekomendasi untuk membandingkan kesamaan antara dokumen atau item berdasarkan representasi vektor mereka.

### Perhitungan _Cosine Similarity_ pada matrix tf-idf

1. Menggunakan fungsi cosine_similarity() dari library scikit-learn untuk menghitung cosine similarity dari matriks TF-IDF yang telah dihasilkan sebelumnya. Hasilnya adalah matriks cosine similarity yang menyajikan kemiripan antara setiap pasangan item atau destinasi wisata dalam dataset.

2. Pembuatan DataFrame Cosine Similarity: DataFrame baru cosine_sim_df dibuat dari matriks cosine similarity yang telah dihitung sebelumnya. Nama destinasi wisata digunakan sebagai indeks (baris dan kolom) dari dataframe ini.

3. Sebuah sampel dari similarity matrix yang dihasilkan ditampilkan untuk memberikan gambaran tentang kemiripan antara beberapa pasangan destinasi wisata. Ini memberikan representasi visual tentang seberapa mirip setiap pasangan destinasi dalam dataset berdasarkan cosine similarity.

Tabel 1 Hasil Cosine Similarity
| destination_name | Bukit Paralayang, Watugupit | Pantai Sepanjang | Pantai Nguluran | Tugu Pal Putih Jogja | Pantai Congot |
|-------------------------------|-----------------------------|------------------|-----------------|----------------------|---------------|
| Tebing Breksi | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Pantai Krakal | 0.0 | 1.0 | 1.0 | 0.0 | 1.0 |
| Monumen Batik Yogyakarta | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Goa Rancang Kencono | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Candi Ijo | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Candi Prambanan | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Kebun Teh Nglinggo | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Kampung Wisata Dipowinatan | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Pantai Ngandong | 0.0 | 1.0 | 1.0 | 0.0 | 1.0 |
| Kampung Wisata Taman Sari | 0.0 | 0.0 | 0.0 | 1.0 | 0.0 |

Dari tabel di atas, kita dapat melihat bahwa beberapa pasangan destinasi memiliki tingkat kemiripan yang cukup tinggi, seperti Pantai Sepanjang dan Pantai Ngandong yang memiliki nilai cosine similarity 1.0, yang menunjukkan bahwa kedua destinasi tersebut sangat mirip berdasarkan fitur yang digunakan dalam perhitungan.

### Mendapatkan Rekomendasi Wisata

#### Membuat Fungsi Rekomendasi Wisata

Fungsi ini bertujuan untuk merekomendasikan destinasi wisata berdasarkan kemiripan dengan destinasi yang telah ditentukan.

##### Parameter Fungsi:

-   nama_destinasi: Parameter ini adalah nama destinasi wisata yang menjadi fokus untuk mendapatkan rekomendasi.
-   similarity_data: Parameter ini adalah dataframe yang berisi data kemiripan antara destinasi wisata. Secara default, nilainya diambil dari dataframe cosine similarity yang telah dihitung sebelumnya.
-   items: Parameter ini adalah dataframe yang berisi informasi tentang destinasi wisata, termasuk nama dan fitur lainnya yang digunakan dalam perhitungan kemiripan. Secara default, nilainya diambil dari dataframe data.
-   k: Parameter ini menentukan jumlah rekomendasi yang akan diberikan. Secara default, nilai adalah 5.

##### Algoritma Rekomendasi:

-   Pertama, dilakukan pengindeksan untuk mendapatkan nilai similarity terbesar menggunakan metode argpartition() pada matriks kemiripan dataframe.
-   Kemudian, kolom-kolom dengan similarity terbesar diambil untuk mendapatkan destinasi wisata yang paling mirip.
-   Destinasi yang sama dengan destinasi input dihapus dari hasil rekomendasi.
-   Hasilnya adalah dataframe berisi daftar destinasi rekomendasi yang kemudian digabungkan dengan informasi destinasi dari dataframe items.
-   Hanya lima destinasi teratas yang kemudian dikembalikan sebagai hasil rekomendasi.

### Hasil Rekomendasi Wisata

#### Hasil Rekoemendasi Top 5 Wisata

1. Pencarian Rekomendasi Destinasi:
   Pada bagian ini, kita ingin mendapatkan rekomendasi destinasi wisata yang mirip dengan destinasi 'Pasar Beringharjo'. Variabel user_input diinisialisasi dengan nilai 'Pasar Beringharjo'.
2. Pencetakan Informasi:
   Dicetak pesan yang menyatakan bahwa kita sedang mencari rekomendasi destinasi untuk destinasi wisata dengan nama 'Pasar Beringharjo'.
3. Pemanggilan Fungsi Rekomendasi:

-   Fungsi destination_recommendations() dipanggil dengan argumen 'Pasar Beringharjo' sebagai input. Fungsi ini akan memberikan rekomendasi destinasi yang mirip dengan destinasi tersebut.
-   Hasil dari pemanggilan fungsi tersebut kemudian dicetak.

4. Output:
   Hasil output menampilkan daftar rekomendasi destinasi yang mirip dengan 'Pasar Beringharjo', beserta informasi kategori masing-masing destinasi. Misalnya, destinasi wisata 'Pasar Kebon Empring Bintaran' yang termasuk dalam kategori 'Pusat Perbelanjaan' adalah salah satu rekomendasi yang diberikan.

Top Recommendation Destinasi: Pasar Beringharjo

| destination_name             | category           |
| ---------------------------- | ------------------ |
| Pasar Kebon Empring Bintaran | Pusat Perbelanjaan |
| Kawasan Wisata Sosrowijayan  | Pusat Perbelanjaan |
| Air Terjun Sri Gethuk        | Cagar Alam         |
| Goa Rancang Kencono          | Cagar Alam         |
| Kampung Wisata Kadipaten     | Budaya             |

Tabel 2 Hasil Rekomendasi Wisata dengan input Pasar Beringharjo

Dari tabel diatas, didapatkan 5 _top_ teratas metode _Content Based Filtering_. Hasil tersebut mendapatkan 3 destinasi wisata dengan kategori selain Pusat Perbelanjaan, sehingga didapatkan dari 5 destinasi wisata yang direkomendasikan, 2 destinasi memiliki kategori Pusat Perbelanjaan.

#### Hasil Rekomendasi Top N Wisata

| No. | Destination Name           | Category |
| --- | -------------------------- | -------- |
| 1   | Hutan Mangrove Kulon Progo | Bahari   |
| 2   | Pantai Samas               | Bahari   |
| 3   | Pantai Kukup               | Bahari   |
| 4   | Pantai Kesirat             | Bahari   |
| 5   | Pantai Siung               | Bahari   |
| 6   | Pantai Greweng             | Bahari   |
| 7   | Pantai Congot              | Bahari   |
| 8   | Pantai Sundak              | Bahari   |
| 9   | Pantai Sedahan             | Bahari   |
| 10  | Pantai Jogan               | Bahari   |
| 11  | Pantai Sepanjang           | Bahari   |

Tabel 3 Hasil Top N Rekomendasi Wisata dengan input Pantai Parangtris

Dari tabel diatas, didapatkan 10 _top_ rekomendasi wisata di Jogja dengan metode _Content Based Filtering_. Semua hasil rekomendasi adalah kategori bahari yang mana itu sangat sesuai jika kita mencari destinasi wisata yang mirip selain Pantai Parangtritis

## 6. Evaluation

### Metrik Evaluasi _Precision_

Metrik evaluasi yang digunakan untuk metode Content-Based Filtering adalah _Precision_.

Dari tabel 3 rekomendasi di atas, diperoleh 10 hasil teratas dari metode Content-Based Filtering. Semua hasil tersebut termasuk dalam kategori tempat wisata Bahari.

Artinya, _precision_ sistem sebesar 5/5 atau 100%. Dengan perhitungan sebagai berikut:
Presisi = Hasil Sesuai / Total hasil presisi = 5 / 5.
Presisi = 1.0 ==> 100%.

Presisi yang sempurna menunjukkan bahwa sistem memberikan rekomendasi yang sesuai dengan preferensi pengguna.

## Kesimpulan:

1. Tabel Rekomendasi Destinasi Wisata Teratas:
   Dari tabel rekomendasi, kita melihat bahwa destinasi wisata teratas untuk Pantai Parangtritis adalah berbagai pantai dan tempat wisata bahari lainnya di sekitar Jogja.
   Rekomendasi ini sesuai dengan ekspektasi karena Pantai Parangtritis adalah destinasi pantai terkenal di Yogyakarta, sehingga wisatawan yang berkunjung ke sana cenderung juga tertarik dengan destinasi serupa.
2. Evaluasi Metrik Precision:
   Metrik evaluasi precision digunakan untuk mengukur seberapa akurat sistem dalam memberikan rekomendasi yang sesuai dengan preferensi pengguna.
   Dalam kasus ini, nilai precision sistem adalah 100%, yang berarti semua rekomendasi yang diberikan oleh sistem sesuai dengan preferensi pengguna.
   Hasil ini menunjukkan bahwa metode content-based filtering yang digunakan dalam sistem rekomendasi mampu memberikan rekomendasi dengan tingkat akurasi yang tinggi, sehingga dapat diandalkan oleh pengguna dalam memilih destinasi wisata yang sesuai dengan preferensi mereka.

Dengan demikian, berdasarkan hasil tabel dan evaluasi metrik precision, dapat disimpulkan bahwa sistem rekomendasi menggunakan metode content-based filtering telah memberikan rekomendasi destinasi wisata yang relevan dan akurat untuk pengguna.

## Referensi

[1] Aprilia Saptu Ningrum, Heru Cahya Rustamaji, Yuli Fauziah (2019). CONTENT BASED DAN COLLABORATIVE FILTERING PADA REKOMENDASI TUJUAN PARIWISATA DI DAERAH YOGYAKARTA
