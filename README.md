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

**Rubrik/Kriteria Tambahan (Opsional)**:
- Jelaskan mengapa proyek ini penting untuk diselesaikan.
- Menyertakan hasil riset terkait atau referensi. Referensi yang diberikan harus berasal dari sumber yang kredibel dan author yang jelas.
  
  Format Referensi: [Judul Referensi](https://scholar.google.com/) 

## Business Understanding

Pada bagian ini, Anda perlu menjelaskan proses klarifikasi masalah.

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah:
- Pernyataan Masalah 1
- Pernyataan Masalah 2
- Pernyataan Masalah n

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
