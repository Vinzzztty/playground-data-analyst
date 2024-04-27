# Laporan Proyek Machine Learning - Kevin Arnandes

### Proyek Machine Learning: Prediksi Pertumbuhan Selada Dengan Algoritma Machine Learning

-   **Nama:** Kevin Arnandes
-   **Email:** kevinarnandes21@gmail.com
-   **ID Dicoding:** kevinarnandes

## Project Domain

#### **Latar Belakang**

Dalam menghadapi kebutuhan akan pertanian yang efisien dan berkualitas, pengembangan algoritma prediksi pertumbuhan dan kualitas selada menjadi semakin krusial. Dengan pemahaman yang lebih mendalam tentang faktor-faktor yang memengaruhi pertumbuhan tanaman dan kualitasnya, potensi untuk meningkatkan produktivitas pertanian, mengoptimalkan pemanfaatan sumber daya, dan menjamin pasokan yang konsisten dan bermutu bagi konsumen dapat ditingkatkan. Algoritma prediksi yang akurat dapat menjadi alat yang berharga bagi petani dan produsen dalam pengambilan keputusan, dengan demikian meningkatkan efisiensi operasional dan keberlanjutan sistem pertanian secara keseluruhan.

Relevansi proyek Pertumbuhan Selada sebagai berikut:

-   Penelitian ini bertujuan untuk membandingkan empat algoritma machine learning (_SVM, Random Forest, Gradient Boosting_, dan _K-Nearest Neighbor_) dalam klasifikasi pola pertumbuhan selada, dengan tujuan untuk memilih algoritma yang paling sesuai untuk meningkatkan produktivitas pertanian dan kualitas hasil pertumbuhan tanaman.

-   Langkah-langkah untuk meningkatkan akurasi model machine learning, seperti pemilihan fitur-fitur yang relevan, penyetelan parameter secara cermat untuk mengoptimalkan kinerja model, serta penerapan teknik ensemble learning, merupakan aspek yang sangat penting dalam upaya mencapai tujuan penelitian tersebut, yakni meningkatkan kualitas hasil pertumbuhan tanaman selada. Dengan melakukan langkah-langkah tersebut, diharapkan model yang dikembangkan dapat memberikan prediksi yang lebih akurat dan dapat diandalkan, sehingga memungkinkan pengambilan keputusan yang lebih tepat dalam mengelola pertumbuhan tanaman selada di dalam plant factory.

Dalam domain ini, penerapan teknologi pertanian presisi di pabrik tanaman melibatkan pengamatan yang cermat terhadap pertumbuhan selada untuk memahami perilakunya dan meramalkan kualitas tanaman [1].

Kesimpulannya, memahami prediksi pertumbuhan selada memiliki relevansi yang signifikan. Dengan pemahaman yang lebih mendalam tentang faktor-faktor yang mempengaruhi pertumbuhan dan kualitas tanaman, efisiensi produksi dapat ditingkatkan, penggunaan sumber daya dapat dioptimalkan, dan pasokan produk yang konsisten dan berkualitas tinggi dapat dijamin untuk konsumen. Dengan menggunakan algoritma prediksi yang akurat, petani dan produsen memiliki kemampuan untuk membuat keputusan yang lebih cerdas dalam pengelolaan pertanian mereka, yang pada gilirannya meningkatkan efisiensi operasional dan keberlanjutan sistem pertanian secara keseluruhan.

## 2. Business Understanding

### Problem Statements

-   Algoritma _machine learning_ mana yang memiliki tingkat akurasi tinggi dalam klasifikasi pola pertumbuhan selada?

Petani dihadapkan pada tantangan yang kompleks dalam memastikan pertumbuhan yang optimal untuk tanaman selada mereka, karena banyaknya faktor yang memengaruhi kesehatan dan perkembangan tanaman.

Proyek ini bertujuan untuk mengatasi tantangan tersebut dengan membandingkan kinerja empat algoritma machine learning yang berbeda. Tujuannya adalah untuk menemukan algoritma yang paling mampu klasifikasi pola pertumbuhan selada dengan akurasi tertinggi.

-   Apa langkah yang dapat di ambil untuk meningkatkan akurasi dalam prediksi pola pertumbuhan selada?

Penyebab utama dari rendahnya akurasi dalam prediksi pola pertumbuhan selada mungkin disebabkan oleh kurangnya relevansi atau kompleksitas fitur-fitur yang digunakan dalam model prediksi. Selain itu, keterbatasan dalam pengumpulan data yang representatif dan berkualitas juga dapat mempengaruhi akurasi prediksi.

Langkah-langkah yang dapat diambil untuk meningkatkan akurasi dalam prediksi pola pertumbuhan selada meliputi pemilihan fitur-fitur yang lebih relevan dan informatif, penyetelan parameter model yang optimal, penggunaan teknik ensemble learning untuk menggabungkan hasil dari beberapa model, serta peningkatan dalam pengumpulan data yang lebih representatif dan lengkap. Dengan melakukan langkah-langkah ini, diharapkan akurasi prediksi pola pertumbuhan selada dapat ditingkatkan secara signifikan.

### Goals

Tujuan penelitian Prediksi Pertumbuhan Selada dengan Algoritma Machine Learning adalah sebagai berikut:

-   Dalam mengkomparasi empat algoritma machine learning, yaitu SVM, Random Forest, Gradient Boosting, dan K-Nearest Neighbor, penelitian ini bertujuan untuk mengidentifikasi algoritma yang memiliki tingkat akurasi tertinggi dalam klasifikasi pertumbuhan selada. Penentuan ini memiliki signifikansi dalam peningkatan produktivitas pertanian dan kualitas hasil pertumbuhan tanaman.

-   Dalam konteks prediksi pertumbuhan selada, strategi untuk meningkatkan akurasi model machine learning melibatkan beberapa langkah. Ini termasuk pemilihan fitur yang paling relevan, penyetelan optimal parameter algoritma, penerapan teknik ensemble learning, seperti penggabungan hasil dari beberapa algoritma, dan pengumpulan data yang berkualitas dan representatif. Diharapkan upaya-upaya ini akan meningkatkan kemampuan model dalam memberikan prediksi yang akurat dan dapat diandalkan terkait pertumbuhan tanaman selada.

Dengan memahami tujuan penelitian, proyek ini dapat dirancang dan disesuaikan untuk memenuhi kebutuhan dan tujuan penelitian yang spesifik.

Oleh karena itu, proyek Prediksi Pertumbuhan Selada dengan Algoritma Machine Learning dapat memberikan manfaat signifikan bagi petani dengan karakteristik penelitian di atas, dengan tujuan meningkatkan efisiensi dan mencapai keunggulan yang lebih stabil, sebagai berikut:

-   Penemuan Algoritma Machine Learning yang Akurat: Dengan melakukan perbandingan antara beberapa model machine learning, proyek ini bertujuan untuk mengidentifikasi algoritma machine learning yang memiliki tingkat akurasi yang tinggi.

-   Peningkatan Efisiensi dan Produktivitas: Dengan menggunakan algoritma machine learning, petani dapat meningkatkan efisiensi dan produktivitas dalam proses penanaman tanaman selada. Model machine learning dapat memproses data dengan cepat dan memberikan prediksi pola pertumbuhan tanaman selada yang akurat. Hal ini memungkinkan petani untuk mendapatkan hasil tanaman yang lebih optimal dan tepat.

Dengan memanfaatkan algoritma machine learning yang dikembangkan dalam proyek ini, petani tanaman selada dapat membuat keputusan yang lebih baik, meningkatkan efisiensi operasional, dan mencapai hasil tanaman yang lebih baik secara konsisten.

### Solution Statements

Solusi yang diberikan untuk proyek ini melibatkan beberapa tahapan dan algorita yang digunakan. Berikut adalah penjelasan lebih rinci mengenai solusi yang diberikan:

1. Eksplorasi Data (_Exploratory Data Analysis_ - EDA)

    - Sebelum melatih model, proses EDA akan dilakukan guna memahami karakteristik data. EDA akan membantu dalam mengidentifikasi pola, melihat hubungan antar variabel, dan menemukan wawasan yang berguna dalam klasifikasi pola pertumbuhan tanaman selada

2. Algoritma _SVM (Support Vector Machine), Random Forest, Gradient Boosting_, dan _K-Nearest Neighbor_

    - Algoritma _SVM (Support Vector Machine), Random Forest, Gradient Boosting_, dan _K-Nearest Neighbor_ dipilih sebagai algoritma _machine learning_ yang akan digunakan dalam proyek ini
    - _SVM (Support Vector Machine)_ adalah metode machine learning yang digunakan untuk pemisahan kelas dengan menemukan hyperplane optimal yang memaksimalkan jarak antara kelas yang berbeda dalam ruang fitur.
    - _Random Forest_ adalah algoritma ensemble learning yang menggabungkan beberapa pohon keputusan yang independen untuk membuat prediksi yang lebih akurat.
    - _Gradient Boosting_ adalah teknik ensemble learning di mana model prediksi dibangun secara bertahap dengan memperbaiki kesalahan prediksi model sebelumnya.
    - _K-Nearest Neighbor_ adalah algoritma machine learning yang menghitung prediksi berdasarkan mayoritas label dari k tetangga terdekat dalam ruang fitur.

3. Evaluasi dengan Metrik Akurasi, Presisi, Recall, dan F1-score:
    - Metrik Akurasi akan digunakan untuk menilai seberapa tepat model dalam memprediksi kelas atau label data.
    - Metrik Presisi akan memberikan informasi tentang seberapa banyak prediksi positif yang sebenarnya benar.
    - Metrik Recall akan menunjukkan seberapa banyak kelas positif yang diprediksi dengan benar oleh model.
    - F1-score adalah ukuran rata-rata harmonis dari presisi dan recall, yang memberikan keseimbangan antara kedua metrik tersebut.
    - Dengan menggunakan metrik Akurasi, Presisi, Recall, dan F1-score, proyek ini dapat memperoleh pemahaman yang komprehensif tentang kinerja model dalam mengklasifikasikan pola pertumbuhan selada.

Melalui pendekatan ini, diharapkan solusi yang diberikan dapat memenuhi tujuan proyek dalam mengembangkan model _machine learning_ prediktif yang akurat dan efektif guna klasifikasi pola pertumbuhan tanaman selada.

## 3. Data Understanding

Dataset yang digunakan dalam proyek ini merupakan data parameter terkait tanaman selada yang dimonitoring secara _realtime_.

Dataset dapat diunduh di: [Dataset Selada](https://raw.githubusercontent.com/Vinzzztty/playground-data-analyst/main/Machine%20Learning%20Terapan/2.%20Sentiment%20Analysis/dataset/dataset_selada.csv).

Tabel 3.1 Tabel hasil table dataframe
| Jam | temperature | humidity | light | pH | EC | TDS | WaterTemp | Label | Pattern |
| ----- | ----------- | -------- | ----- | --- | --- | --- | --------- | ------ | ------- |
| 15.15 | 25.5 | 67 | 17660 | 6.4 | 855 | 427 | 29.7 | Selada | 1 |
| 17.22 | 26.9 | 80 | 86930 | 6.7 | 929 | 464 | 27.0 | Selada | 1 |
| 7.33 | 25.7 | 77 | 23320 | 6.1 | 900 | 449 | 25.4 | Selada | 1 |
| 9.18 | 26.6 | 69 | 32280 | 6.7 | 887 | 443 | 26.1 | Selada | 1 |
| 10.39 | 25.8 | 65 | 41750 | 6.6 | 967 | 482 | 25.7 | Selada | 1 |

Berikut informasi pada dataset:

-   Dataset memiliki format CSV (_Comma-Sperated Values_)
-   Dataset memiliki 5004 sampel dengan 10 fitur
-   Terdapat 1 kolom tipe object yaitu Label dan memiliki satu nilai unik
-   Terdapat 4 kolom numerik dengan tipe data float64 yaitu: Jam, temperature, pH, WaterTemp
-   Terdapat 5 kolom numerik edngan tipe data int64 yaitu: humidity, light, EC, TDS, Pattern
-   Tidak ada missing value dalam dataset

### Variabel-variabel pada Dataset selada adalah sebagai berikut:

-   Jam : waktu yang dicatat ketika nilai baru terekam.
-   temperature : nilai suhu dengan meteran Celcius
-   humidity: nilai kelembaban
-   light: nilai intensitas cahaya
-   pH: nilai pH
-   EC: nilai konduktivitas listrik
-   TDS: nilai total zat terlarut
-   WaterTemp: Suhu air
-   Label: Jenis tanaman yaitu hanya selada
-   Pattern: nilai pola atau tren peningkatan pertumbuhan tanaman
    -   1 Tahap Awal (Awal): Pada tahap ini, tanaman mulai tumbuh dengan cepat dan mengalami peningkatan pertumbuhan yang signifikan setiap hari.
    -   2 Tahap Pertumbuhan (Tengah): Tahap pertumbuhan selada ini mencakup periode di mana tanaman telah berakar dengan baik dan mulai mengalami pertumbuhan daun yang lebih luas serta perkembangan batang yang lebih kokoh
    -   3 Tahap Pematangan (Akhir): Tahap ini terjadi menjelang masa panen, di mana pertumbuhan tanaman melambat secara signifikan dan tanaman mencapai ukuran dan kejadian pertumbuhan yang optimal.

### Pendalam Data

-   Melakukan tahapan EDA seperti mendeskripsikan variabel
-   Mencari keterkaitan antar fitur numerik dengan _correlation matrix_ menggunakan fungsi pandas dan visualisasi _heatmap_ dengan _seaborn_

#### Menganalisa hubungan fitur dengan Korelasi Matrix

Menganalisa keterkaitan antara fitur numerik dan fitur kategori dengan _correlation matrix_ yang didapat dari fungsi pandas dan visualisasi heatmap menggunakan library seaborn.

Heatmap menunjukkan tingkat korelasi antara setiap pasangan fitur numerik dan fitur kategori. Warna dalam heatmap mencerminkan tingkat korelasi, di mana warna lebih terang menunjukkan korelasi yang lebih kuat, sedangkan warna lebih gelap menunjukkan korelasi yang lebih lemah atau tidak ada korelasi.

Hubungan antara fitur numerik dan fitur kategori dapat diamati melalui nilai korelasi, yang dapat bersifat positif atau negatif. Proses analisis ini membantu untuk memahami interaksi antar fitur dalam dataset dan memberikan wawasan yang berharga untuk keperluan seleksi fitur, pembuatan model, atau analisis lebih lanjut.

Dengan memanfaatkan matriks korelasi, dapat dilakukan analisis yang komprehensif terhadap keterkaitan antara fitur numerik dan fitur kategori dalam dataset secara visual dan numerik.

Gambar 3.1 hasil running korelasi matriks
![korelasi matriks](https://github.com/Vinzzztty/playground-data-analyst/blob/main/Assets/output.png?raw=true)

Terdapat beberapa hubungan antara variabel yang diamati berdasarkan koefisien korelasi dari hasil visualisasi diatas:

-   Variabel 'temperature' memiliki korelasi positif yang lemah dengan variabel 'WaterTemp' (0.162) dan korelasi negatif yang lemah dengan variabel 'humidity' (-0.106).
-   Variabel 'humidity' memiliki korelasi negatif yang lemah dengan variabel 'temperature' (-0.106) dan 'WaterTemp' (-0.102).
-   Variabel 'EC' dan 'TDS' memiliki korelasi sangat kuat (0.996), menunjukkan bahwa keduanya sangat berkorelasi dan mungkin dapat direduksi menjadi satu variabel.
-   Variabel 'pH' memiliki korelasi negatif yang lemah dengan variabel 'EC' (-0.063) dan 'TDS' (-0.065), menunjukkan adanya hubungan yang kurang kuat antara tingkat keasaman dan tingkat konduktivitas serta total padatan terlarut dalam air.

## 4. Data Preparation

### Menangani _Outliers_

Untuk mengatasi _outlier_, salah satu metode yang umum digunakakan adalah metode IQR (_Interquartile Range_) dengan visualisasi boxplot

Metode IQR:

1. Konsep: IQR merupakan ukuran statistik yang menggambarkan rentang atau sebaran data pada bagian tengah distribusi data. IQR dihitung dengan mengurangi nilai kuartil ketiga (Q3) dengan nilai kuartil pertama (Q1). Outlier dianggap sebagai nilai yang terletak di luar rentang IQR yang ditentukan.
2. Cara Kerja:
    - Hitung Q1 (kuartil pertama) dan Q3 (kuartil ketiga) dari data.
    - Hitung IQR dengan mengurangi Q1 dari Q3.
    - Tentukan batas atas dan batas bawah untuk outlier dengan menggunakan rumus: batas atas = Q3 + (1.5 _ IQR), batas bawah = Q1 - (1.5 _ IQR).
    - Data yang berada di luar batas atas dan batas bawah tersebut dianggap sebagai outlier.

Visualisasi Boxplot:

1. Konsep: Boxplot adalah visualisasi grafis yang digunakan untuk menganalisis distribusi data dan mengidentifikasi adanya outlier. Boxplot menampilkan beberapa ukuran statistik, termasuk Q1, Q3, median, serta batas atas dan batas bawah untuk outlier.
2. Cara Kerja:
    - Boxplot terdiri dari sebuah kotak (box) yang menunjukkan rentang IQR (dari Q1 hingga Q3).
    - Garis di dalam kotak menunjukkan posisi median.
    - Whisker atau garis lurus yang terhubung dengan kotak menunjukkan rentang data yang dianggap tidak sebagai outlier.
    - Titik-titik di luar whisker menunjukkan adanya outlier.

Dengan menggunakan metode IQR dan visualisasi boxplot, selanjutnya dapat mengidentifikasi dan mengatasi outlier dalam data. Outlier dapat menjadi nilai yang ekstrem dan tidak biasa yang dapat mempengaruhi hasil analisis statistik dan model prediksi.

### Kesalahan Penulisan Nilai pada kolom temperature

Untuk mengatasi kesalah penulisan nilai pada kolom temperature, dengan metode perhitungan matematika sederhana

1. Filter Baris dengan Nilai 'temperature' Lebih Besar dari 100:

    - Variabel `high_temperature_rows` digunakan untuk menyimpan baris-baris dalam DataFrame `df` yang memiliki nilai 'temperature' lebih besar dari 100.
    - Penggunaan `df['temperature'] > 100` merupakan teknik pemfilteran data untuk mendapatkan baris-baris yang memenuhi kondisi tersebut.

2. Tampilkan Nilai pada Kolom 'temperature' dari Baris yang Telah Difilter:
    - Variabel `high_temperature_values` digunakan untuk menyimpan nilai 'temperature' dari baris-baris yang telah difilter.
    - Dengan menggunakan `high_temperature_rows['temperature']`, untuk menampilkan nilai 'temperature' dari baris yang telah difilter.
3. Perbaikan Nilai 'temperature' Jika Ada Nilai yang Lebih Besar dari 100.00:
    - Jika `high_temperature_rows` tidak kosong (artinya ada baris dengan nilai 'temperature' lebih dari 100.00), maka dilakukan perbaikan nilai 'temperature'.
    - Perbaikan dilakukan dengan membagi nilai 'temperature' yang lebih besar dari 100.00 dengan 100, sehingga mengubah nilai tersebut menjadi nilai yang sesuai.
    - Penggunaan `df.loc[df['temperature'] > 100.00, 'temperature'] /= 100.0` digunakan untuk mengubah nilai 'temperature' yang memenuhi kondisi tersebut.

### Melakukan Pre-Processing Data

Sebelum melakukan analisis lebih lanjut, langkah awal yang dilakukan adalah pre-processing data untuk mempersiapkan dataset yang akan digunakan. Berikut adalah beberapa langkah yang dilakukan dalam pre-processing data:

-   Membuat kolom fitur ('X') yang terdiri dari variabel-variabel independen yang akan digunakan dalam analisis, yaitu: temperature, humidity, light, pH, EC, TDS, dan WaterTemp.
-   Membuat kolom target ('y') yang merupakan variabel dependen yang akan diprediksi, yaitu 'Pattern'.

### Split Data

Setelah membuat kolom fitur dan target, langkah selanjutnya adalah menggunakan teknik train*test_split dari \_library scikit-learn (sklear)* untuk membagi data menjadi data latih (train) dan data uji (test) dengan rasio 80:20. Hal ini bertujuan untuk memastikan bahwa model yang dikembangkan dapat diuji dengan baik pada data yang belum pernah dilihat sebelumnya, sehingga dapat mengukur kinerja model dengan lebih obyektif.

-   Total Sampel dalam Dataset Keseluruhan: 5005
-   Total Sampel dalam Dataset Latih: 4004
-   Total Sampel dalam Dataset Uji: 1001

### Standarisasi Data

Selanjutnya, dilakukan standarisasi data menggunakan metode _StandardScaler_. Langkah-langkah yang dilakukan adalah sebagai berikut:

-   Pengecekan Kolom Non-Numerik pada Variabel X: Memastikan tidak ada kolom non-numerik yang akan mengganggu proses standarisasi.
-   Standarisasi Data dengan StandardScaler(): Proses standarisasi dilakukan untuk menjaga skala data agar tidak mendominasi satu sama lain, sehingga memungkinkan model untuk lebih efektif dalam mempelajari pola-pola yang ada dalam dataset.

## 5. Modeling

### _Default Parameter_ Model

Dalam proses _modeling_, proyek ini akan menggunakan empat algoritma machine learning yaitu Algoritma _SVM (Support Vector Machine), Random Forest, Gradient Boosting_, dan _K-Nearest Neighbor_

Algoritma _SVM (Support Vector Machine), Random Forest, Gradient Boosting_, dan _K-Nearest Neighbor_ merupakan algoritma machine learning yang umum digunakan dalam klasifikasi.

1. Algoritma SVM (Support Vector Machine):
    - SVM adalah algoritma klasifikasi yang memisahkan data ke dalam kelas menggunakan hyperplane dalam ruang fitur yang diberikan.
    - Default parameter untuk SVM meliputi:
        - C (penalitas kesalahan): Defaultnya adalah 1.0. Ini mengontrol seberapa banyak model memperbolehkan pelanggaran margin. Nilai yang lebih tinggi menekankan pada klasifikasi yang benar, sementara nilai yang lebih rendah memberikan toleransi yang lebih besar terhadap kesalahan klasifikasi.
        - kernel (jenis fungsi kernel): Defaultnya adalah 'rbf' (radial basis function). Ini adalah fungsi yang digunakan untuk mentransformasi data ke dalam dimensi yang lebih tinggi sehingga data dapat dipisahkan oleh hyperplane.
        - gamma (koefisien kernel): Defaultnya adalah 'scale'. Gamma menentukan jarak pengaruh sampel. Nilai yang lebih rendah berarti sampel yang lebih jauh memiliki pengaruh yang lebih besar.
2. Algoritma Random Forest:
    - Random Forest adalah metode klasifikasi yang menggunakan ensemble learning dari berbagai pohon keputusan.
    - Default parameter untuk Random Forest meliputi:
        - n_estimators (jumlah pohon dalam ensemble): Defaultnya adalah 100. Ini adalah jumlah pohon keputusan yang akan dibuat dalam ensemble.
        - max_depth (kedalaman maksimum pohon): Defaultnya adalah None, yang berarti tidak ada batasan kedalaman. Ini adalah kedalaman maksimum setiap pohon dalam ensemble.
3. Algoritma Gradient Boosting:
    - Gradient Boosting adalah metode klasifikasi yang menghasilkan model prediktif dalam bentuk himpunan model prediktif lemah, umumnya pohon keputusan.
    - Default parameter untuk Gradient Boosting meliputi:
        - learning_rate (tingkat pembelajaran): Defaultnya adalah 0.1. Ini adalah faktor dengan nilai 0 hingga 1 yang mengontrol seberapa banyak setiap model berikutnya berusaha memperbaiki kesalahan model sebelumnya.
        - max_depth (kedalaman maksimum pohon): Defaultnya adalah 3. Ini adalah kedalaman maksimum setiap pohon keputusan dalam ensemble.
4. Algoritma K-Nearest Neighbor (KNN):
    - KNN adalah algoritma klasifikasi yang berdasarkan prinsip bahwa objek-objek yang serupa berada di dekat satu sama lain dalam ruang fitur.
    - Default parameter untuk KNN meliputi:
        - n_neighbors (jumlah tetangga terdekat): Defaultnya adalah 5. Ini adalah jumlah tetangga terdekat yang akan dipertimbangkan ketika memprediksi kelas suatu objek.
        - weights (metode bobot): Defaultnya adalah 'uniform'. Ini adalah metode untuk menghitung bobot dari setiap tetangga. 'Uniform' memberi bobot yang sama untuk semua tetangga, sedangkan 'distance' memberi bobot yang lebih tinggi untuk tetangga yang lebih dekat.
        - p (parameter jarak): Defaultnya adalah 2. Ini adalah parameter yang menentukan metrik jarak yang akan digunakan. Jika p=1, digunakan metrik jarak Manhattan. Jika p=2, digunakan metrik jarak Euclidean.

#### Tahapan yang dilakukan ketika proses modeling:

1. Membuat dictionary models yang berisi model klasifikasi yang akan dilatih, termasuk "Gradient Boosting Classifier", "Random Forest", "Support Vector Machine", dan "K-Nearest Neighbors".
2. Membuat list kosong results_list yang akan digunakan untuk menyimpan hasil evaluasi model.
3. Melakukan iterasi melalui setiap pasangan nama dan model dalam dictionary models.
4. Melatih model dengan menggunakan data pelatihan (X_train, y_train).
5. Melakukan prediksi menggunakan data uji (X_test).
6. Menghitung akurasi model dengan membandingkan prediksi dengan label sebenarnya menggunakan metode accuracy_score.
7. Menghasilkan laporan klasifikasi menggunakan classification_report dari scikit-learn, dengan output dalam bentuk dictionary.
8. Mengekstrak precision, recall, dan f1-score dari laporan klasifikasi untuk kelas 'weighted avg'.
9. Menambahkan hasil evaluasi model (Model, Accuracy, Precision, Recall, F1 Score) ke dalam list results_list dalam bentuk dictionary.
10. Iterasi berakhir setelah semua model dilatih dan dievaluasi.

Keempat algoritma tersebut digunakan untuk memodelkan klasifikasi pola pertumbuhan selada.

### Hyperparameter Tunning Model

Dalam model terbaru, parameter-parameter yang digunakan telah disesuaikan dengan nilai-nilai yang spesifik sesuai dengan kebutuhan. Berikut adalah penjelasan mengenai parameter-parameter yang digunakan dalam model terbaru:

1. Gradient Boosting Classifier:
    - learning_rate: Digunakan dengan nilai 0.1. Ini adalah tingkat pembelajaran yang mengontrol seberapa besar model berikutnya berusaha memperbaiki kesalahan model sebelumnya.
    - max_depth: Digunakan dengan nilai 10. Ini adalah kedalaman maksimum setiap pohon keputusan dalam ensemble.
2. Random Forest:
    - n_estimators: Digunakan dengan nilai 100. Ini adalah jumlah pohon keputusan yang akan dibuat dalam ensemble.
    - max_depth: Digunakan dengan nilai 30. Ini adalah kedalaman maksimum setiap pohon dalam ensemble.
3. Support Vector Machine (SVM):
    - C: Digunakan dengan nilai 10.0. Ini adalah penalitas kesalahan yang mengontrol seberapa besar model memperbolehkan pelanggaran margin.
    - kernel: Digunakan dengan nilai 'rbf' (radial basis function). Ini adalah fungsi yang digunakan untuk mentransformasi data ke dalam dimensi yang lebih tinggi.
    - gamma: Digunakan dengan nilai 'scale'. Ini adalah koefisien kernel yang menentukan jarak pengaruh sampel.
4. K-Nearest Neighbors (KNN):
    - n_neighbors: Digunakan dengan nilai 5. Ini adalah jumlah tetangga terdekat yang akan dipertimbangkan ketika memprediksi kelas suatu objek.
    - weights: Digunakan dengan nilai 'distance'. Ini adalah metode untuk menghitung bobot dari setiap tetangga, memberikan bobot yang lebih tinggi untuk tetangga yang lebih dekat.
    - p: Digunakan dengan nilai 1. Ini adalah parameter yang menentukan metrik jarak yang akan digunakan, dengan p=1 menggunakan metrik jarak Manhattan.

#### Tahapan yang dilakukan ketika proses modeling:

1. Definisi Model Baru:

    - Membuat sebuah dictionary baru bernama new_models yang berisi model-model klasifikasi baru yang akan dilatih, termasuk Gradient Boosting Classifier, Random Forest, Support Vector Machine, dan K-Nearest Neighbors.
    - Setiap model memiliki parameter-parameter yang telah ditentukan, seperti learning_rate, max_depth, n_estimators, C, kernel, gamma, n_neighbors, weights, dan p.

2. Inisialisasi List Kosong:
    - Membuat sebuah list kosong bernama new_results_list yang akan digunakan untuk menyimpan hasil evaluasi model baru.
3. Evaluasi Model Baru:
    - Melakukan iterasi melalui setiap pasangan nama dan model dalam dictionary new_models.
    - Melatih setiap model baru menggunakan data pelatihan (X_train, y_train).
    - Melakukan prediksi menggunakan data uji (X_test).
    - Menghitung akurasi model baru dengan membandingkan prediksi dengan label sebenarnya menggunakan metode accuracy_score.
    - Menghasilkan laporan klasifikasi menggunakan classification_report dari scikit-learn, dengan output dalam bentuk dictionary.
    - Mengekstrak precision, recall, dan f1-score dari laporan klasifikasi untuk kelas 'weighted avg'.
    - Menambahkan hasil evaluasi model baru (New Model, New Accuracy, New Precision, New Recall, New F1 Score) ke dalam list new_results_list dalam bentuk dictionary.
4. Konversi ke DataFrame:
    - Setelah semua model baru dilatih dan dievaluasi, berikutnya mengonversi list of dictionaries new_results_list menjadi DataFrame baru yang bernama new_results_train_df.

## 6. Evaluation

Hasil algoritma model machine learning yang dapat dilihat metriknya antara lain: _Accuracy, precision, recall,_ dan _F1 Score_

Tabel 6.1 Tabel hasil model _training default parameter_ dengan metrik _Accuracy, Precision, Recall,_ dan _F1 Score_
| Model | Accuracy | Precision | Recall | F1 Score |
| ---------------------------- | -------- | --------- | ------ | -------- |
| Gradient Boosting Classifier | 0.922 | 0.925 | 0.922 | 0.923 |
| Random Forest | 0.904 | 0.907 | 0.904 | 0.905 |
| Support Vector Machine | 0.568 | 0.661 | 0.568 | 0.481 |
| K-Nearest Neighbors | 0.792 | 0.801 | 0.792 | 0.794 |

Insight:

-   Model Gradient Boosting Classifier dan Random Forest menunjukkan performa yang lebih baik dalam hal akurasi, presisi, recall, dan F1-score dibandingkan dengan model Support Vector Machine dan K-Nearest Neighbors.
-   Support Vector Machine menunjukkan akurasi yang rendah, hal ini mungkin disebabkan oleh pengaturan parameter yang tidak optimal atau kurangnya pemrosesan data.
-   Model K-Nearest Neighbors memiliki akurasi yang cukup baik tetapi tidak sebaik Gradient Boosting Classifier dan Random Forest. Hal ini bisa disebabkan oleh pemilihan jumlah tetangga yang tidak optimal atau karakteristik data yang tidak cocok dengan model ini.

Dari hasil di atas, dapat disimpulkan bahwa Gradient Boosting Classifier dan Random Forest adalah pilihan yang lebih baik untuk tugas klasifikasi ini berdasarkan performa mereka yang lebih baik dalam semua metrik evaluasi. Namun, tetap diperlukan penyesuaian lebih lanjut dan eksperimen dengan pengaturan model dan pemrosesan data untuk meningkatkan performa model klasifikasi.

Hasil Evaluasi Model dengan _Hyperparameter Tunning_

Tabel 6.2 Tabel hasil model _training hyperparamter tunning_ dengan metrik _Accuracy, Precision, Recall,_ dan _F1 Score_
| New Model | New Accuracy | New Precision | New Recall | New F1 Score |
| ---------------------------- | ------------ | ------------- | ---------- | ------------ |
| Gradient Boosting Classifier | 0.930 | 0.930 | 0.930 | 0.930 |
| Random Forest | 0.905 | 0.907 | 0.905 | 0.906 |
| Support Vector Machine | 0.602 | 0.637 | 0.602 | 0.607 |
| K-Nearest Neighbors | 0.858 | 0.861 | 0.858 | 0.859 |

Insight:

-   Model Gradient Boosting Classifier dan Random Forest masih menunjukkan performa yang baik dalam hal akurasi, presisi, recall, dan F1-score.
-   Model Support Vector Machine menunjukkan peningkatan dalam hal akurasi dibandingkan sebelumnya, tetapi masih memiliki performa yang lebih rendah dibandingkan dengan model lainnya.
-   Model K-Nearest Neighbors juga menunjukkan peningkatan dalam hal akurasi, presisi, recall, dan F1-score, dan menjadi model dengan performa terbaik kedua setelah Gradient Boosting Classifier.
-   Gradient Boosting Classifier tetap menjadi pilihan terbaik berdasarkan performa secara keseluruhan, namun K-Nearest Neighbors menunjukkan potensi sebagai alternatif yang baik terutama untuk kasus yang memerlukan komputasi yang cepat dan mudah diinterpretasikan.

## 7. Kesimpulan

Berdasarkan insight di atas, kesimpulannya adalah bahwa model yang harus dipilih tergantung pada kebutuhan dan tujuan spesifik dari proyek atau tugas yang sedang dihadapi:

-   Jika performa model yang optimal menjadi prioritas utama, maka Gradient Boosting Classifier adalah pilihan yang tepat.
-   Jika kecepatan komputasi dan interpretasi model menjadi faktor penting, maka K-Nearest Neighbors dapat menjadi alternatif yang baik.
-   Jika kestabilan dan konsistensi performa model diperlukan tanpa memperhatikan faktor interpretasi, maka Random Forest dapat menjadi pilihan yang cocok

Perbandingan Model tanpa _Hyperparameter Tunning_ versus Model dengan _Hyperparameter Tunning_

Tabel 7.1 Tabel hasil perbandingan Akurasi Model Lama dengan Model Baru
| Model | Akurasi Lama | Akurasi Baru |
| ---------------------------- | -----------: | -----------: |
| Gradient Boosting Classifier | 0.922078 | 0.930070 |
| Random Forest | 0.904096 | 0.905095 |
| Support Vector Machine | 0.568432 | 0.602398 |
| K-Nearest Neighbors | 0.792208 | 0.858142 |

Berdasarkan hasil tersebut, Model Gradient Boosting Classifier adalah model terbaik karena memiliki akurasi tertinggi di antara semua model, yaitu 0.930070. Oleh karena itu, untuk tujuan pemodelan ini, disarankan untuk menggunakan Model _Gradient Boosting Classifier_.

Dapat disimpulkan bahwa algoritma Gradient Boosting Classifier menunjukkan potensi yang besar dalam meningkatkan akurasinya dengan melakukan Hyperparameter tuning. Meskipun akurasinya sudah cukup tinggi, penyesuaian lebih lanjut terhadap parameter-parameter seperti learning rate, max depth, dan jumlah estimators dapat membantu meningkatkan kinerja model secara signifikan. Oleh karena itu, Hyperparameter tuning perlu dilakukan untuk memaksimalkan potensi algoritma Gradient Boosting Classifier dalam memodelkan data dengan akurasi yang lebih tinggi.

## Referensi

[1] Rizkiana, A., Nugroho, A. P., & Sutiarso, L. (2020). Perancangan Model Prediksi Pertumbuhan Tanaman Pada _Plant Factory_ Dengan Metode Jaringan Saraf Tiruan. Universitas Gadjah Mada.
