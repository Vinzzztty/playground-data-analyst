# Laporan Proyek Machine Learning - Kevin Arnandes

### Proyek Machine Learning: Prediksi Pertumbuhan Selada Dengan Random Forest

-   **Nama:** Kevin Arnandes
-   **Email:** kevinarnandes21@gmail.com
-   **ID Dicoding:** kevinarnandes

## Domain Proyek

#### **Latar Belakang**

Selada telah lama dikenal di masyarakat Indonesia, namun pembudidayaannya masih belum meluas. Baru-baru ini, konsumsi selada mengalami peningkatan yang signifikan karena selada memiliki penampilan yang menarik, dengan warna hijau segar yang memikat konsumen, dapat dijadikan lalapan, dan memiliki manfaat kesehatan yang tinggi, terutama karena kandungan mineralnya yang melimpah. Selain itu, selada juga mudah ditemukan di pasaran dengan harga yang terjangkau (Sastradihardja, 2011).

Penerapan teknologi pertanian presisi pada plant factory melibatkan pengamatan intensif terhadap pertumbuhan tanaman untuk memahami perilakunya dan memprediksi waktu serta hasil panen. Tujuan dari penelitian ini adalah merancang model prediksi pertumbuhan tanaman menggunakan metode jaringan saraf tiruan resilient backpropagation dengan mempertimbangkan parameter lingkungan pada plant factory, serta mengevaluasi kinerjanya pada tanaman selada.

#### **Alasan**

Latar belakang ini perlu dipahami dan diselesaikan karena memahami faktor-faktor yang memengaruhi pertumbuhan selada secara holistik akan menjadi dasar yang kuat untuk merancang model prediksi dengan akurasi tinggi menggunakan algoritma Random Forest. Dengan demikian, informasi yang diperoleh dari latar belakang ini akan menjadi landasan yang solid untuk memasukkan variabel-variabel yang relevan ke dalam model prediksi, sehingga hasilnya dapat memberikan estimasi pertumbuhan selada yang lebih akurat dan dapat diandalkan.

#### **Referensi**

[Perancangan Model Prediksi Pertumbuhan Tanaman Pada Plant Factory Dengan Metode Jaringan Saraf Tiruan](https://etd.repository.ugm.ac.id/penelitian/detail/189162)

## Business Understanding

### Problem Statements

-   Pertanyaan 1: Bagaimana pengaruh variasi parameter lingkungan seperti 'temperature', 'humidity', 'light', 'pH', 'EC', 'TDS', dan 'WaterTemp' terhadap pattern pertumbuhan selada yang diinginkan?

-   Pertanyaan 2: Bagaimana algoritma Random Forest dapat digunakan untuk memprediksi pola pertumbuhan atau label yang optimal pada tanaman selada berdasarkan parameter-parameter lingkungan tersebut?

### Goals

-   Jawaban 1: Variasi parameter lingkungan seperti 'temperature', 'humidity', 'light', 'pH', 'EC', 'TDS', dan 'WaterTemp' dapat berpengaruh signifikan terhadap pattern pertumbuhan selada. Misalnya, suhu yang terlalu tinggi atau rendah, kelembaban udara yang tidak sesuai, atau tingkat pH yang tidak stabil dapat memengaruhi pertumbuhan dan kesehatan tanaman selada.

-   Jawaban 2: Algoritma Random Forest dapat digunakan dengan memasukkan parameter-parameter lingkungan seperti 'temperature', 'humidity', 'light', 'pH', 'EC', 'TDS', dan 'WaterTemp' sebagai fitur-fitur untuk melatih model prediksi. Melalui proses pembelajaran mesin, algoritma ini akan mampu menemukan pola kompleks di antara parameter-parameter ini dan menghasilkan prediksi yang optimal untuk pola pertumbuhan atau label yang diinginkan pada tanaman selada.

**Rubrik/Kriteria Tambahan (Opsional)**:

### Solution statements

-   Solusi Pertanyaan 1: Kami akan melakukan analisis statistik dan visualisasi data untuk mengidentifikasi hubungan antara parameter lingkungan dan pola pertumbuhan selada.

-   Solusi Pertanyaan 2: Kami akan melatih model ini menggunakan dataset yang telah dikumpulkan, kemudian melakukan evaluasi performa menggunakan metrik yang sesuai.

## Data Understanding

[Dataset Selada](https://raw.githubusercontent.com/Vinzzztty/playground-data-analyst/main/Machine%20Learning%20Terapan/2.%20Sentiment%20Analysis/submission/dataset_selada.csv).

### Variabel-variabel pada Dataset selada adalah sebagai berikut:

-   Jam : waktu yang dicatat ketika nilai baru terekam.
-   temperature : nilai suhu dengan meteran Celcius
-   humidity: nilai kelembaban
-   light: nilai intensitas cahaya
-   pH: nilai pH
-   EC: nilai konduktivitas listrik
-   TDS: nilai total zat terlarut
-   WaterTemp: Suhu air
-   Label: Jenis tanaman
-   Pattern: nilai pola atau tren

Dataset memiliki tipe data:

-   Terdapat 1 kolom tipe object yaitu Label
-   Terdapat 4 kolom numerik dengan tipe data float64 yaitu: Jam, temperature, pH, WaterTemp
-   Terdapat 5 kolom numerik edngan tipe data int64 yaitu: humidity, light, EC, TDS, Pattern

## Data Preparation

Data Cleaning padda kesalahan penulisan atau typo nilai kolom temperature, langkah langkah yang dilakukan antara lain:

-   Filter baris nilai kolom temperature yang lebih besar dari 100
-   Kemudian nilai tersebut dibagi dengan 100,
-   Nilai yang awalnya 2619.0 menjadi 26.19

Melakukan Data Pre-Processing

-   Membuat kolom features antara lain: temperature, humidity, light, pH, EC, TDS, adn WaterTemp sebagai 'X'
-   Membuat kolom pattern sebagai y, yang mana sebagai target variabel x

Melakukan pencarian Korelasi nilai matrix pada variabel features

-   Terlihat kolom EC dan TDS memiliki korelasi positif yang bernilai 1

Melakukan Split Data ke dalam Train, dan Test dengan rasio 80:20

-   Total # of sample in whole dataset: 5005
-   Total # of sample in train dataset: 4004
-   Total # of sample in test dataset: 1001

Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

Melakukan Standarisasi

-   Mengecek non-numeric kolom pada variabel X
-   Melakukan Standarisasi dengan StandardScaler()

## Modeling

Melakukan training data dengan algoritma machine learning Random Forest. Kita akan membandingkan algoritma Random Forest tanpa Hyperparameter Tunning dengan Random Forest Hyperparameter Tunning

-   Accuracy of Random Forest (Tanpa Hyperparameter Tunning) on the test set: 0.906093906093906
-   Accuracy of Random Forest (Dengan Hyperparameter Tunning) on the test set: 0.9010989010989011

Lebih baik menggunakan algoritma Random Forest dengan default Parameter dibandingkan dengan Random Forest Hyperparameter Tunning dengan selisih 0,005 .

## Evaluation

Menggunakan metrix evaluasi MSE (Mean Squared Error), dengan beberapa tahapan antara lain:

-   Persiapan DataFrame Kosong: Langkah pertama adalah membuat sebuah DataFrame kosong untuk menyimpan hasil evaluasi model. DataFrame ini akan memiliki kolom-kolom yang akan digunakan untuk menyimpan hasil evaluasi, seperti nama model, akurasi latihan (train accuracy), akurasi uji (test accuracy), MSE latihan (train MSE), dan MSE uji (test MSE).

-   Evaluasi Model: Selanjutnya, kita akan melakukan evaluasi terhadap setiap model yang telah disiapkan sebelumnya. Kita akan melakukan iterasi (loop) melalui setiap model dan melakukan evaluasi.

-   Evaluasi Akurasi pada Data Latihan: Untuk setiap model, kita akan menghitung akurasi pada data latihan (train accuracy) dengan menggunakan metode score() dari model tersebut. Akurasi ini memberikan gambaran seberapa baik model kita cocok dengan data latihan.

-   Prediksi pada Data Latihan dan Perhitungan MSE: Setelah itu, kita akan melakukan prediksi terhadap data latihan dengan menggunakan model yang bersangkutan. Dari prediksi tersebut, kita akan menghitung Mean Squared Error (MSE) dengan menggunakan fungsi mean_squared_error() dari scikit-learn. MSE merupakan metrik evaluasi yang mengukur seberapa dekat prediksi dengan nilai sebenarnya pada data latihan.

-   Penyimpanan Hasil dalam DataFrame: Semua hasil evaluasi akan disimpan dalam DataFrame yang telah disiapkan sebelumnya. Setiap baris DataFrame akan mewakili satu model, dengan nilai-nilai evaluasi yang sesuai untuk model tersebut.

Hasil Evaluasi Metrix dengan MSE

-   Model Random Forest memiliki performa yang sangat baik dalam memodelkan hubungan antara fitur-fitur dan target.
-   Model memiliki kemampuan yang baik dalam melakukan generalisasi, artinya model mampu memberikan prediksi yang baik tidak hanya pada data latihan tetapi juga pada data baru yang belum pernah dilihat sebelumnya.
-   Dikarenakan nilai Train Accuracy yang sempurna (100%) dan Train MSE yang nol (0.0), ada kemungkinan terjadinya overfitting. Ini berarti model mungkin telah terlalu dipasangkan dengan data latihan dan mungkin tidak akan menggeneralisasi dengan baik pada data yang belum pernah dilihat sebelumnya.
-   Namun, dengan akurasi yang masih tinggi pada data uji dan nilai MSE yang relatif rendah, model tersebut tampaknya masih memberikan hasil yang memuaskan.

Mean Squared Error (MSE) adalah salah satu metrik evaluasi yang umum digunakan dalam pemodelan statistik dan pembelajaran mesin untuk mengukur seberapa dekat prediksi model dengan nilai sebenarnya dari target atau variabel respons. MSE dihitung dengan cara menghitung rata-rata dari kuadrat selisih antara setiap nilai prediksi dengan nilai sebenarnya. Berikut adalah formulanya:

![Rumus MSE](https://elektrocode2018.wordpress.com/wp-content/uploads/2020/08/image-10.png?w=609)

Di mana:

-   tk adalah nilai sebenarnya dari target untuk observasi ke- k
-   yk adalah nilai prediksi dari model observasi ke -k
-   a adalah jumlah total observasi
    ​
