# Laporan Proyek Machine Learning - Mizwar
# Membuat sistem rekomendasi

## Project Overview

Latar belakang yang relevan dengan proyek sistem rekomendasi yang kami kerjakan adalah sebagai berikut:

Perkembangan Teknologi dan Internet: Dengan pesatnya perkembangan teknologi dan internet, semakin banyak pengguna yang memiliki akses ke berbagai jenis konten seperti film, musik, buku, dan produk lainnya. Namun, dengan banyaknya pilihan yang tersedia, pengguna sering mengalami kesulitan dalam menemukan konten yang sesuai dengan preferensi mereka. Oleh karena itu, sistem rekomendasi menjadi penting untuk membantu pengguna menemukan konten yang relevan dan menarik bagi mereka.

Peran Sistem Rekomendasi dalam E-Commerce: Di industri e-commerce, sistem rekomendasi telah menjadi elemen penting dalam meningkatkan pengalaman belanja pengguna. Dengan menganalisis data belanja pengguna, sistem rekomendasi dapat memberikan rekomendasi produk yang sesuai dengan preferensi dan riwayat belanja pengguna, membantu mereka menemukan produk yang relevan, meningkatkan kepuasan pengguna, dan mendorong penjualan.

Tren Konsumsi Konten Digital: Konsumsi konten digital seperti film, musik, dan acara televisi telah menjadi tren yang signifikan dalam beberapa tahun terakhir. Pengguna memiliki preferensi dan selera yang unik, dan dengan menggunakan sistem rekomendasi yang cerdas, platform streaming seperti Netflix dan Spotify dapat memberikan rekomendasi yang sangat personal kepada pengguna, membantu mereka menemukan konten yang relevan dan memuaskan.

Algoritma *Collaborative Filtering* dan *Matrix Factorization*: Dalam proyek ini, kami menggunakan algoritma *Collaborative Filtering* dengan metode *Matrix Factorization*, seperti *Singular Value Decomposition* (SVD). Algoritma ini merupakan pendekatan yang efektif dalam membangun sistem rekomendasi, dengan memanfaatkan data rating dari pengguna untuk menemukan pola dan hubungan antara pengguna dan item yang direkomendasikan.

Dataset MovieLens: Dataset MovieLens merupakan salah satu dataset paling populer untuk membangun sistem rekomendasi. Dataset ini berisi informasi rating pengguna terhadap film, serta data tambahan seperti informasi pengguna dan detail film. Dengan menggunakan dataset ini, kami dapat menguji dan melatih model sistem rekomendasi kami.

Dengan latar belakang tersebut, proyek ini memiliki relevansi dalam mengaplikasikan teknologi sistem rekomendasi untuk membantu pengguna menemukan konten yang sesuai dengan preferensi mereka, meningkatkan pengalaman pengguna, dan memfasilitasi peningkatan penjualan dalam industri e-commerce.

## Business Understanding

1. Meningkatkan Pengalaman Pengguna: Salah satu tujuan utama dari proyek ini adalah meningkatkan pengalaman pengguna. Dengan memberikan rekomendasi yang relevan dan personal kepada pengguna, sistem rekomendasi dapat membantu mereka menemukan konten yang sesuai dengan preferensi mereka. Hal ini dapat meningkatkan kepuasan pengguna, memperpanjang waktu interaksi dengan platform atau layanan, dan membangun loyalitas pengguna.

2. Meningkatkan Konversi dan Penjualan: Dalam konteks e-commerce, proyek ini dapat membantu meningkatkan konversi dan penjualan. Dengan menggunakan sistem rekomendasi untuk memberikan rekomendasi produk yang relevan kepada pengguna, platform e-commerce dapat mendorong pengguna untuk melakukan pembelian lebih banyak atau memilih produk dengan nilai transaksi yang lebih tinggi. Ini dapat menghasilkan peningkatan pendapatan dan pertumbuhan bisnis.

3. Personalisasi Layanan: Sistem rekomendasi juga memungkinkan personalisasi layanan. Dengan memahami preferensi pengguna dan memberikan rekomendasi yang sesuai, platform atau layanan dapat menciptakan pengalaman yang unik dan disesuaikan untuk setiap pengguna. Hal ini dapat membantu membangun hubungan yang lebih dekat antara pengguna dan merek atau platform, serta meningkatkan loyalitas dan retensi pengguna.

4. Meningkatkan Efisiensi Pencarian: Dengan adanya sistem rekomendasi yang efektif, pengguna tidak perlu lagi menghabiskan waktu yang lama untuk mencari atau memilih konten yang relevan. Sistem rekomendasi dapat menyaring dan menyajikan pilihan yang paling relevan, menghemat waktu dan usaha pengguna dalam mencari konten yang mereka sukai.

5. Analisis Data dan Informasi: Dalam proyek ini, penggunaan data rating pengguna dan informasi film digunakan untuk membangun model rekomendasi. Hal ini juga memberikan peluang bagi perusahaan untuk menganalisis data tersebut, mendapatkan wawasan tentang preferensi pengguna, tren konsumsi, dan perilaku pengguna lainnya. Informasi ini dapat digunakan untuk pengambilan keputusan bisnis, seperti pengembangan produk, strategi pemasaran, dan penargetan audiens.

Dengan pemahaman bisnis ini, proyek sistem rekomendasi dapat membantu perusahaan meningkatkan pengalaman pengguna, meningkatkan konversi dan penjualan, personalisasi layanan, meningkatkan efisiensi pencarian, serta memberikan wawasan berharga dari analisis data dan informasi yang dihasilkan.

### Problem Statements

Berikut adalah beberapa pernyataan masalah (problem statements) yang terkait dengan proyek sistem rekomendasi tersebut:

1. Bagaimana pengguna menemukan konten yang sesuai dengan preferensi mereka di tengah banyaknya pilihan yang tersedia?
2. Bagaimana menghadapi tantangan dalam meningkatkan konversi dan penjualan produk dalam konteks e-commerce?
3. Bagaimana meningkatkan pengalaman pengguna yang lebih personal dan disesuaikan dengan preferensi mereka saat menggunakan platform atau layanan?
4. Bagaimana meningkatkan efisiensi pencarian pengguna dalam menemukan konten yang mereka sukai?
5. Bagaimana Perusahaan ingin memanfaatkan data rating pengguna dan informasi film untuk menganalisis preferensi pengguna, tren konsumsi, dan perilaku pengguna lainnya guna pengambilan keputusan bisnis yang lebih baik?

Dengan merumuskan pernyataan masalah ini, proyek sistem rekomendasi dapat difokuskan untuk mengatasi kendala-kendala di atas dan memberikan solusi yang relevan.

### Goals

Tujuan proyek sistem rekomendasi ini adalah untuk mengatasi pernyataan masalah yang telah disebutkan sebelumnya. Tujuan ini mencakup:

1. Membantu pengguna menemukan konten yang sesuai dengan preferensi mereka: Tujuan utama proyek ini adalah memberikan solusi bagi pengguna yang mengalami kesulitan dalam menemukan konten yang sesuai dengan preferensi mereka. Dengan menggunakan algoritma rekomendasi yang cerdas, sistem akan memberikan rekomendasi yang relevan dan personal kepada pengguna, sehingga mereka dapat menemukan konten yang sesuai dengan minat mereka dengan lebih mudah.

2. Meningkatkan konversi dan penjualan produk: Dalam konteks e-commerce, tujuan proyek ini adalah meningkatkan konversi dan penjualan produk dengan memberikan rekomendasi yang relevan kepada pengguna. Dengan memperlihatkan produk yang sesuai dengan preferensi dan riwayat belanja pengguna, sistem rekomendasi dapat mempengaruhi pengguna untuk melakukan pembelian lebih banyak atau memilih produk dengan nilai transaksi yang lebih tinggi.

3. Personalisasi pengalaman pengguna: Proyek ini bertujuan untuk memberikan pengalaman pengguna yang lebih personal dan disesuaikan. Dengan memahami preferensi pengguna dan memberikan rekomendasi yang sesuai, sistem rekomendasi dapat menciptakan pengalaman yang unik dan disesuaikan untuk setiap pengguna. Tujuannya adalah menciptakan hubungan yang lebih dekat antara pengguna dan platform atau layanan, sehingga meningkatkan loyalitas dan retensi pengguna.

4. Meningkatkan efisiensi pencarian: Salah satu tujuan proyek ini adalah meningkatkan efisiensi pencarian pengguna. Dengan menggunakan sistem rekomendasi yang efektif, pengguna tidak perlu lagi menghabiskan waktu yang lama untuk mencari atau memilih konten yang relevan. Sistem akan menyaring dan menyajikan pilihan yang paling relevan, menghemat waktu dan usaha pengguna dalam mencari konten yang mereka sukai.

5. Menganalisis data dan informasi untuk pengambilan keputusan bisnis: Proyek ini juga bertujuan untuk memanfaatkan data rating pengguna dan informasi film untuk menganalisis preferensi pengguna, tren konsumsi, dan perilaku pengguna lainnya. Dengan melakukan analisis data yang mendalam, perusahaan dapat mendapatkan wawasan berharga yang dapat digunakan untuk pengambilan keputusan bisnis yang lebih baik, seperti pengembangan produk, strategi pemasaran, dan penargetan audiens.

Dengan mencapai tujuan-tujuan ini, proyek sistem rekomendasi diharapkan dapat memberikan solusi bagi pernyataan masalah yang telah diidentifikasi sebelumnya dan memberikan manfaat yang signifikan bagi pengguna dan bisnis yang terlibat.

## Data Understanding

Data Understanding proyek sistem rekomendasi ini melibatkan pemahaman yang mendalam tentang dataset yang digunakan, yaitu [dataset MovieLens](http://files.grouplens.org/datasets/movielens/ml-100k.zip). Berikut ini adalah beberapa informasi penting tentang dataset tersebut:

1. Sumber Dataset: Dataset MovieLens dihasilkan oleh GroupLens Research dan menyediakan data rating pengguna terhadap film. Dataset ini digunakan secara luas dalam proyek-proyek sistem rekomendasi dan tersedia secara publik.

2. Jumlah Data: Dataset MovieLens tersedia dalam beberapa versi dengan jumlah data yang berbeda. Contohnya, versi MovieLens 100K terdiri dari sekitar 100.000 rating yang diberikan oleh sekitar 1.000 pengguna terhadap sekitar 1.700 film.

3. Informasi Pengguna: Dataset MovieLens mencakup informasi tentang pengguna seperti ID pengguna, usia, dan jenis kelamin. Informasi ini dapat digunakan untuk pemahaman lebih lanjut tentang preferensi pengguna.

4. Informasi Film: Dataset juga mencakup informasi tentang film seperti ID film, judul, genre, dan detail lainnya. Informasi ini dapat digunakan untuk memahami konten film yang direkomendasikan kepada pengguna.

5. Data Rating: Data rating pengguna adalah bagian inti dari dataset MovieLens. Setiap rating terdiri dari ID pengguna, ID film, rating, dan timestamp. Data rating ini menjadi dasar untuk membangun model sistem rekomendasi yang dapat menghasilkan rekomendasi berdasarkan pola dan hubungan antara pengguna dan film yang telah mereka beri rating.

6. Data Tambahan: Selain data rating, dataset MovieLens juga dapat mencakup data tambahan seperti tag yang diberikan oleh pengguna pada film tertentu atau informasi lain yang relevan. Data tambahan ini dapat memberikan konteks tambahan dalam membangun sistem rekomendasi.

Dalam proses Data Understanding ini, penting untuk memahami struktur dataset, informasi yang terkandung di dalamnya, serta potensi data yang dapat dieksplorasi untuk membangun sistem rekomendasi yang efektif.

Variabel-variabel yang terdapat dalam dataset MovieLens mencakup:

* UserID: Variabel ini mengidentifikasi pengguna dalam dataset. Setiap pengguna memiliki ID unik yang digunakan untuk menghubungkan rating dengan pengguna yang memberikan rating tersebut.

* MovieID: Variabel ini mengidentifikasi film dalam dataset. Setiap film memiliki ID unik yang digunakan untuk menghubungkan rating dengan film yang diberi rating.

* Rating: Variabel ini menunjukkan rating yang diberikan oleh pengguna untuk suatu film. Rating dapat berupa skala numerik, seperti dari 1 hingga 5, yang menggambarkan tingkat kesukaan pengguna terhadap film tersebut.

* Timestamp: Variabel ini menunjukkan waktu ketika rating diberikan oleh pengguna. Timestamp memberikan informasi tentang urutan waktu rating yang dapat digunakan untuk analisis temporal.

* Informasi Pengguna: Dataset MovieLens juga dapat mencakup variabel-variabel yang memberikan informasi tentang pengguna, seperti usia, jenis kelamin, dan preferensi lainnya. Informasi ini dapat digunakan untuk menganalisis preferensi pengguna dan membangun rekomendasi yang lebih personal.

* Informasi Film: Dataset juga dapat mencakup variabel-variabel yang memberikan informasi tentang film, seperti judul, genre, tahun rilis, dan detail lainnya. Informasi ini dapat digunakan untuk memahami konten film dan membangun rekomendasi yang sesuai dengan preferensi pengguna.

Selain variabel-variabel tersebut, dataset MovieLens juga dapat mencakup variabel-variabel tambahan seperti tag yang diberikan oleh pengguna pada film tertentu atau informasi lain yang relevan. Variabel-variabel ini memberikan konteks tambahan yang dapat digunakan dalam analisis dan pembangunan sistem rekomendasi.

## Data Preparation

1. Persiapan Awal: Mengimpor library yang diperlukan dan menginstal library yang diperlukan seperti pandas, numpy, dan scikit-learn.

2. Unduh dan Muat Dataset: Mengunduh dataset MovieLens dan memuat dataset ke dalam DataFrame menggunakan library pandas.

3. Eksplorasi Dataset: Melakukan eksplorasi dataset untuk memahami struktur dan informasi yang terkandung di dalamnya.

4. Persiapan Data: Melakukan pemrosesan data yang diperlukan, seperti menggabungkan DataFrame, menghapus kolom yang tidak diperlukan, dan mengubah format data jika diperlukan.

5. Membangun Model: Memilih model rekomendasi yang ingin digunakan, seperti SVD dari library surprise.

6. Melatih Model dan Uji Sistem: Melatih model rekomendasi menggunakan seluruh data rating dan menguji sistem dengan memberikan rekomendasi kepada pengguna.

Adapun langkah persiapan data meliputi:
* Penggabungan Data: Dalam sistem rekomendasi, kita perlu menggabungkan data dari beberapa sumber, seperti data pengguna, data peringkat, dan data film. Dengan menggabungkan data ini menjadi satu dataset, kita dapat menghasilkan pemahaman yang lebih lengkap tentang preferensi pengguna dan karakteristik film yang akan digunakan dalam proses rekomendasi.

* Penghapusan Kolom yang Tidak Diperlukan: Terkadang, dataset sumber dapat mengandung kolom-kolom yang tidak relevan atau tidak diperlukan dalam proses rekomendasi. Dengan menghapus kolom-kolom tersebut, kita dapat menyederhanakan dataset dan mengurangi dimensi data yang tidak perlu, sehingga mempercepat pemrosesan dan menghemat sumber daya komputasi.

* Pemrosesan Format Data: Dalam beberapa kasus, dataset sumber dapat mengandung format data yang tidak sesuai atau perlu diubah agar sesuai dengan format yang diperlukan oleh algoritma rekomendasi. Misalnya, dataset dapat menyimpan data dalam format teks atau tanggal yang perlu diubah menjadi format numerik agar dapat digunakan dalam proses rekomendasi.

* Pembersihan dan Pemrosesan Missing Values: Dataset sumber juga dapat mengandung missing values atau nilai yang hilang. Missing values dapat mempengaruhi kualitas model rekomendasi, oleh karena itu perlu dilakukan pembersihan dan pemrosesan missing values dengan menggantikan nilai yang hilang dengan nilai yang sesuai, seperti rata-rata atau median.

Melalui tahapan data preparation ini, kita dapat mempersiapkan dataset yang lebih bersih, lebih terstruktur, dan sesuai dengan kebutuhan algoritma rekomendasi. Hal ini akan mempengaruhi kualitas sistem rekomendasi yang kita bangun, memberikan hasil yang lebih akurat dan relevan dalam memberikan rekomendasi kepada pengguna.

## Modeling

Model sistem rekomendasi yang telah dibangun dalam proyek ini menggunakan algoritma Collaborative Filtering dengan metode Matrix Factorization, yaitu Singular Value Decomposition (SVD). SVD merupakan salah satu pendekatan populer dalam collaborative filtering yang memanfaatkan faktorisasi matriks untuk menghasilkan rekomendasi.

Berikut adalah langkah-langkah detail tentang bagaimana algoritma SVD bekerja dalam proyek ini:

1. Persiapan Data: Dataset MovieLens 100K yang berisi data rating film oleh pengguna dimuat dan diproses. Data rating dipisahkan menjadi kolom user_id, movie_id, dan rating.

2. Pembentukan Matriks Rating: Dataset rating digunakan untuk membentuk matriks rating (user-item matrix) di mana setiap baris mewakili pengguna, setiap kolom mewakili film, dan entri matriks adalah rating yang diberikan oleh pengguna untuk film tersebut.

3. Faktorisasi Matriks Menggunakan SVD: Matriks rating yang telah dibentuk kemudian dipecah menjadi tiga matriks menggunakan algoritma SVD, yaitu:

    * Matriks User (U): Matriks ini berisi representasi pengguna dalam ruang faktor. Setiap baris mewakili representasi pengguna dalam ruang faktor, dan setiap kolom mewakili faktor yang menggambarkan preferensi pengguna terhadap faktor-faktor tersebut.
    * Matriks Singular Value (S): Matriks diagonal ini berisi nilai singular values yang menggambarkan tingkat variasi atau pentingnya faktor dalam matriks rating.
    * Matriks Item (V^T): Transpose dari matriks ini berisi representasi film dalam ruang faktor. Setiap baris mewakili representasi film dalam ruang faktor, dan setiap kolom mewakili faktor yang menggambarkan karakteristik film terkait faktor-faktor tersebut.

4. Reduksi Dimensi: Dalam faktorisasi SVD, sejumlah faktor teratas digunakan untuk merekonstruksi matriks rating. Dalam proyek ini, kita memilih sejumlah faktor yang optimal dengan menggunakan Cross Validation untuk mendapatkan kinerja terbaik.

5. Prediksi Rating: Dengan menggunakan matriks faktor User (U), Singular Value (S), dan Item (V^T), kita dapat melakukan prediksi rating untuk film yang belum ditonton oleh pengguna. Prediksi rating dilakukan dengan mengalikan matriks faktor User dan Item, kemudian menambahkan rata-rata rating pengguna.

6. Top-N Recommendation: Setelah prediksi rating untuk film-film yang belum ditonton dihitung, film-film tersebut diurutkan berdasarkan prediksi rating tertinggi. Kemudian, top-N film dengan prediksi rating tertinggi dipilih sebagai rekomendasi untuk pengguna.

Dalam proyek ini, algoritma SVD menggunakan faktorisasi matriks untuk mengekstrak informasi dari dataset rating dan mengidentifikasi pola dan hubungan antara pengguna dan film. Dengan memanfaatkan matriks faktor User, Singular Value, dan Item, algoritma SVD dapat memberikan rekomendasi film yang personal dan relevan kepada pengguna berdasarkan preferensi mereka.

Selain itu, evaluasi kinerja model dilakukan menggunakan metrik RMSE dan MAE untuk memastikan bahwa model memberikan prediksi rating yang akurat dan berkualitas.

Berikut adalah contoh rekomendasi yang dihasilkan dari proyek ini:

Rekomendasi untuk Pengguna ID 5:

Film: Pulp Fiction (1994)
Prediksi Rating: 4.3

Film: North by Northwest (1959)
Prediksi Rating: 4.2

Film: Citizen Kane (1941)
Prediksi Rating: 4.2

Film: Sunset Blvd. (1950)
Prediksi Rating: 4.2

Film: Terminator 2: Judgment Day (1991)
Prediksi Rating: 4.2

Rekomendasi ini didasarkan pada prediksi rating yang diberikan oleh model sistem rekomendasi berdasarkan preferensi dan riwayat penilaian pengguna. Daftar film di atas merupakan rekomendasi teratas yang diurutkan berdasarkan prediksi rating tertinggi.

Penting untuk dicatat bahwa rekomendasi ini bersifat contoh dan mungkin berbeda untuk pengguna lain atau dalam kasus yang berbeda. Sistem rekomendasi yang dibangun dalam proyek ini dapat digunakan untuk memberikan rekomendasi yang lebih personal dan relevan kepada pengguna berdasarkan preferensi mereka.

## Evaluation
Dalam proyek ini, untuk melakukan evaluasi kinerja model sistem rekomendasi, kita menggunakan dua metrik evaluasi yang umum digunakan dalam *collaborative filtering*:

1. *Root Mean Squared Error* (RMSE): Metrik ini mengukur sejauh mana prediksi model berbeda dari nilai sebenarnya dalam skala rating. RMSE menghitung akar dari rata-rata kuadrat selisih antara prediksi rating dan rating sebenarnya. Semakin rendah nilai RMSE, semakin baik kinerja model dalam memprediksi rating.

2. *Mean Absolute Error* (MAE): Metrik ini mengukur nilai rata-rata dari selisih absolut antara prediksi rating dan rating sebenarnya. MAE menghitung rata-rata dari selisih absolut antara prediksi dan rating sebenarnya. Semakin rendah nilai MAE, semakin baik kinerja model dalam memprediksi rating.

Hasil proyek ini berdasarkan metrik evaluasi tersebut adalah sebagai berikut:

* RMSE: Menghasilkan nilai RMSE sebesar 0.94. Ini menunjukkan bahwa rata-rata selisih antara prediksi rating dan rating sebenarnya adalah sekitar 0.94. Semakin rendah nilai RMSE, semakin baik kualitas prediksi model.

* MAE: Menghasilkan nilai MAE sebesar 0.74. Ini menunjukkan bahwa rata-rata selisih absolut antara prediksi rating dan rating sebenarnya adalah sekitar 0.74. Semakin rendah nilai MAE, semakin baik kualitas prediksi model.

Berdasarkan metrik evaluasi RMSE dan MAE, model SVD yang digunakan dalam sistem rekomendasi ini memiliki kinerja yang baik dalam memprediksi rating film pada dataset MovieLens. Nilai RMSE dan MAE yang rendah menunjukkan bahwa model dapat dengan akurat memperkirakan preferensi pengguna terhadap film-film yang belum ditonton.

Dengan demikian, dapat disimpulkan bahwa model sistem rekomendasi yang dibangun dalam proyek ini dapat memberikan rekomendasi yang akurat dan relevan kepada pengguna berdasarkan preferensi mereka.

## Kesimpulan

Dalam proyek ini, telah berhasil dibangun sebuah sistem rekomendasi menggunakan algoritma Collaborative Filtering dengan metode Matrix Factorization (SVD) berdasarkan dataset MovieLens. Proses pengembangan sistem rekomendasi melibatkan tahapan-tahapan seperti persiapan data, pembangunan model, dan evaluasi kinerja.

Hasil yang diperoleh dari proyek ini adalah sebuah sistem rekomendasi yang dapat memberikan rekomendasi film yang personal dan relevan kepada pengguna berdasarkan preferensi mereka. Dalam evaluasi kinerja model, metrik RMSE dan MAE digunakan untuk mengukur sejauh mana prediksi rating model berbeda dari nilai sebenarnya.

Dalam kasus ini, model SVD yang digunakan dalam sistem rekomendasi menunjukkan kinerja yang baik dengan nilai RMSE sebesar 0.94 dan MAE sebesar 0.74. Nilai-nilai ini menunjukkan bahwa model mampu memberikan prediksi rating dengan tingkat akurasi yang baik.

Dengan adanya sistem rekomendasi ini, pengguna dapat menerima rekomendasi film yang sesuai dengan preferensi mereka, membantu mereka menemukan film-film baru yang mungkin mereka sukai berdasarkan data rating yang ada. Dengan demikian, sistem rekomendasi ini dapat meningkatkan pengalaman pengguna dalam menjelajahi dan menemukan konten yang menarik dalam domain film.

Kesimpulannya, proyek ini berhasil membangun sebuah sistem rekomendasi lengkap dengan menggunakan algoritma SVD berdasarkan dataset MovieLens. Sistem rekomendasi ini dapat memberikan rekomendasi film yang personal dan relevan kepada pengguna berdasarkan preferensi mereka, dengan kinerja yang baik dalam memprediksi rating.

## Daftar Pustaka

[1]      Koren, Y., Bell, R., & Volinsky, C. (2009). *Matrix factorization techniques for recommender systems. Computer*, 42(8), 30-37.


[2]      Ricci, F., Rokach, L., Shapira, B., & Kantor, P. B. (2011). *Introduction to recommender systems handbook. In Recommender Systems Handbook* (pp. 1-35). Springer.


[3]      Shani, G., & Gunawardana, A. (2011). *Evaluating recommendation systems. In Recommender Systems Handbook* (pp. 257-297). Springer.


[4]      Leskovec, J., Rajaraman, A., & Ullman, J. D. (2014). *Mining of Massive Datasets*. Cambridge University Press.


[5]      Koren, Y. (2008). *Factorization Meets the Neighborhood: A Multifaceted Collaborative Filtering Model. In Proceedings of the 14th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining* (KDD '08), 426-434.


[6]      Salakhutdinov, R., & Mnih, A. (2008). *Probabilistic matrix factorization. In Advances in neural information processing systems* (pp. 1257-1264).


[7]      Paterek, A. (2007). *Improving regularized singular value decomposition for collaborative filtering. In Proceedings of the KDD Cup and Workshop* (Vol. 2007, No. 1, pp. 39-42).


[8]      Resnick, P., & Varian, H. R. (1997). *Recommender systems. Communications of the ACM*, 40(3), 56-58.


[9]      Sarwar, B., Karypis, G., Konstan, J., & Riedl, J. (2001). *Item-based collaborative filtering recommendation algorithms. In Proceedings of the 10th International Conference on World Wide Web* (WWW '01), 285-295.


[10]     Herlocker, J. L., Konstan, J. A., Terveen, L. G., & Riedl, J. T. (2004). *Evaluating collaborative filtering recommender systems. ACM Transactions on Information Systems* (TOIS), 22(1), 5-53.
