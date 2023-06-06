# Laporan Proyek Machine Learning - Mizwar
# Membuat sistem rekomendasi

## Project Overview

Latar belakang yang relevan dengan proyek sistem rekomendasi yang kami kerjakan adalah sebagai berikut:

Perkembangan Teknologi dan Internet: Dengan pesatnya perkembangan teknologi dan internet, semakin banyak pengguna yang memiliki akses ke berbagai jenis konten seperti film, musik, buku, dan produk lainnya. Namun, dengan banyaknya pilihan yang tersedia, pengguna sering mengalami kesulitan dalam menemukan konten yang sesuai dengan preferensi mereka. Oleh karena itu, sistem rekomendasi menjadi penting untuk membantu pengguna menemukan konten yang relevan dan menarik bagi mereka.

Peran Sistem Rekomendasi dalam E-Commerce: Di industri e-commerce, sistem rekomendasi telah menjadi elemen penting dalam meningkatkan pengalaman belanja pengguna. Dengan menganalisis data belanja pengguna, sistem rekomendasi dapat memberikan rekomendasi produk yang sesuai dengan preferensi dan riwayat belanja pengguna, membantu mereka menemukan produk yang relevan, meningkatkan kepuasan pengguna, dan mendorong penjualan.

Tren Konsumsi Konten Digital: Konsumsi konten digital seperti film, musik, dan acara televisi telah menjadi tren yang signifikan dalam beberapa tahun terakhir. Pengguna memiliki preferensi dan selera yang unik, dan dengan menggunakan sistem rekomendasi yang cerdas, platform streaming seperti Netflix dan Spotify dapat memberikan rekomendasi yang sangat personal kepada pengguna, membantu mereka menemukan konten yang relevan dan memuaskan.

Algoritma Collaborative Filtering dan Matrix Factorization: Dalam proyek ini, kami menggunakan algoritma Collaborative Filtering dengan metode Matrix Factorization, seperti Singular Value Decomposition (SVD). Algoritma ini merupakan pendekatan yang efektif dalam membangun sistem rekomendasi, dengan memanfaatkan data rating dari pengguna untuk menemukan pola dan hubungan antara pengguna dan item yang direkomendasikan.

Dataset MovieLens: Dataset MovieLens merupakan salah satu dataset paling populer untuk membangun sistem rekomendasi. Dataset ini berisi informasi rating pengguna terhadap film, serta data tambahan seperti informasi pengguna dan detail film. Dengan menggunakan dataset ini, kami dapat menguji dan melatih model sistem rekomendasi kami.

Dengan latar belakang tersebut, proyek ini memiliki relevansi dalam mengaplikasikan teknologi sistem rekomendasi untuk membantu pengguna menemukan konten yang sesuai dengan preferensi mereka, meningkatkan pengalaman pengguna, dan memfasilitasi peningkatan penjualan dalam industri e-commerce.

## Business Understanding

1. Meningkatkan Pengalaman Pengguna: Salah satu tujuan utama dari proyek ini adalah meningkatkan pengalaman pengguna. Dengan memberikan rekomendasi yang relevan dan personal kepada pengguna, sistem rekomendasi dapat membantu mereka menemukan konten yang sesuai dengan preferensi mereka. Hal ini dapat meningkatkan kepuasan pengguna, memperpanjang waktu interaksi dengan platform atau layanan, dan membangun loyalitas pengguna.

2. Meningkatkan Konversi dan Penjualan: Dalam konteks e-commerce, proyek ini dapat membantu meningkatkan konversi dan penjualan. Dengan menggunakan sistem rekomendasi untuk memberikan rekomendasi produk yang relevan kepada pengguna, platform e-commerce dapat mendorong pengguna untuk melakukan pembelian lebih banyak atau memilih produk dengan nilai transaksi yang lebih tinggi. Ini dapat menghasilkan peningkatan pendapatan dan pertumbuhan bisnis.

3. Personalisasi Layanan: Sistem rekomendasi juga memungkinkan personalisasi layanan. Dengan memahami preferensi pengguna dan memberikan rekomendasi yang sesuai, platform atau layanan dapat menciptakan pengalaman yang unik dan disesuaikan untuk setiap pengguna. Hal ini dapat membantu membangun hubungan yang lebih dekat antara pengguna dan merek atau platform, serta meningkatkan loyalitas dan retensi pengguna.

4. Meningkatkan Efisiensi Pencarian: Dengan adanya sistem rekomendasi yang efektif, pengguna tidak perlu lagi menghabiskan waktu yang lama untuk mencari atau memilih konten yang relevan. Sistem rekomendasi dapat menyaring dan menyajikan pilihan yang paling relevan, menghemat waktu dan usaha pengguna dalam mencari konten yang mereka sukai.

5. Analisis Data dan Informasi: Dalam proyek ini, penggunaan data rating pengguna dan informasi film digunakan untuk membangun model rekomendasi. Hal ini juga memberikan peluang bagi perusahaan untuk menganalisis data tersebut, mendapatkan wawasan tentang preferensi pengguna, tren konsumsi, dan perilaku pengguna lainnya. Informasi ini dapat digunakan untuk pengambilan keputusan bisnis, seperti pengembangan produk, strategi pemasaran, dan penargetan audiens.

6. Dengan pemahaman bisnis ini, proyek sistem rekomendasi dapat membantu perusahaan meningkatkan pengalaman pengguna, meningkatkan konversi dan penjualan, personalisasi layanan, meningkatkan efisiensi pencarian, serta memberikan wawasan berharga dari analisis data dan informasi yang dihasilkan.

Bagian laporan ini mencakup:

### Problem Statements

Berikut adalah beberapa pernyataan masalah (problem statements) yang terkait dengan proyek sistem rekomendasi tersebut:

1. Pengguna mengalami kesulitan dalam menemukan konten yang sesuai dengan preferensi mereka di tengah banyaknya pilihan yang tersedia.
2. Platform e-commerce menghadapi tantangan dalam meningkatkan konversi dan penjualan produk, karena pengguna sering kali kesulitan dalam memilih produk yang relevan.
3. Pengguna menginginkan pengalaman yang lebih personal dan disesuaikan dengan preferensi mereka saat menggunakan platform atau layanan.
4. Proses pencarian konten yang memakan waktu dan kurang efisien menghambat pengguna dalam menemukan konten yang mereka sukai.
5. Perusahaan ingin memanfaatkan data rating pengguna dan informasi film untuk menganalisis preferensi pengguna, tren konsumsi, dan perilaku pengguna lainnya guna pengambilan keputusan bisnis yang lebih baik.

Dengan merumuskan pernyataan masalah ini, proyek sistem rekomendasi dapat difokuskan untuk mengatasi kendala-kendala di atas dan memberikan solusi yang relevan.

### Goals

Menjelaskan tujuan proyek yang menjawab pernyataan masalah:
- Jawaban pernyataan masalah 1
- Jawaban pernyataan masalah 2
- Jawaban pernyataan masalah n

Semua poin di atas harus diuraikan dengan jelas. Anda bebas menuliskan berapa pernyataan masalah dan juga goals yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Menambahkan bagian “Solution Approach” yang menguraikan cara untuk meraih goals. Bagian ini dibuat dengan ketentuan sebagai berikut: 

    ### Solution statements
    - Mengajukan 2 atau lebih solution approach (algoritma atau pendekatan sistem rekomendasi).

## Data Understanding
Paragraf awal bagian ini menjelaskan informasi mengenai jumlah data, kondisi data, dan informasi mengenai data yang digunakan. Sertakan juga sumber atau tautan untuk mengunduh dataset. Contoh: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Restaurant+%26+consumer+data).

Selanjutnya, uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

Variabel-variabel pada Restaurant UCI dataset adalah sebagai berikut:
- accepts : merupakan jenis pembayaran yang diterima pada restoran tertentu.
- cuisine : merupakan jenis masakan yang disajikan pada restoran.
- dst

**Rubrik/Kriteria Tambahan (Opsional)**:
- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data beserta insight atau exploratory data analysis.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model sisten rekomendasi yang Anda buat untuk menyelesaikan permasalahan. Sajikan top-N recommendation sebagai output.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menyajikan dua solusi rekomendasi dengan algoritma yang berbeda.
- Menjelaskan kelebihan dan kekurangan dari solusi/pendekatan yang dipilih.

## Evaluation
Pada bagian ini Anda perlu menyebutkan metrik evaluasi yang digunakan. Kemudian, jelaskan hasil proyek berdasarkan metrik evaluasi tersebut.

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.
