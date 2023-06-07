# -*- coding: utf-8 -*-
"""Proyek Akhir: Membuat Sistem Rekomendasi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WX8mtv4REtMkSpP1itc0O4K6GXTVfO1j

## **1. Pendahuluan**
Sistem rekomendasi adalah teknologi yang digunakan untuk memberikan rekomendasi atau saran kepada pengguna berdasarkan preferensi mereka. Dalam proyek ini, kami akan menggunakan dataset MovieLens dan membangun sistem rekomendasi menggunakan algoritma Collaborative Filtering dengan metode Matrix Factorization, yaitu Singular Value Decomposition (SVD).

## **2. Langkah-langkah**
### **2.1. Persiapan Awal**
Impor library yang diperlukan, seperti pandas, numpy, dan scikit-learn. Menginstal library surprise yang digunakan untuk algoritma rekomendasi.
"""

!pip install scikit-learn
!pip install pandas
!pip install numpy
!pip install scikit-surprise

import pandas as pd
import numpy as np

"""### **2.2. Unduh dan Muat Dataset**
Mengunduh dataset MovieLens dan memuat dataset ke dalam DataFrame menggunakan library pandas. Kita akan menggunakan dataset MovieLens 100K.
"""

!wget http://files.grouplens.org/datasets/movielens/ml-100k.zip
!unzip ml-100k.zip

# Muat data pengguna
users_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('ml-100k/u.user', sep='|', names=users_cols, encoding='latin-1')

# Muat data peringkat
ratings_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=ratings_cols, encoding='latin-1')

# Muat data film
movies_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
movies = pd.read_csv('ml-100k/u.item', sep='|', names=movies_cols, usecols=range(5), encoding='latin-1')

"""### **2.3. Eksplorasi Dataset**
Melakukan eksplorasi dataset untuk memahami struktur dan informasi yang terkandung di dalamnya. Menggunakan perintah seperti head(), info(), dan describe() untuk melihat beberapa baris awal, informasi kolom, dan statistik deskriptif.
"""

print(users.head())

print(ratings.head())

print(movies.head())

print(users.info())

print(ratings.info())

print(movies.info())

print(ratings.describe())

"""### **2.4. Persiapan Data**
Melakukan pemrosesan data yang diperlukan, seperti menggabungkan DataFrame, menghapus kolom yang tidak diperlukan, dan mengubah format data jika diperlukan.
"""

# Menggabungkan data pengguna, peringkat, dan film
data = pd.merge(pd.merge(ratings, users), movies)

# Hapus kolom yang tidak diperlukan
data = data.drop(['unix_timestamp', 'zip_code', 'release_date', 'video_release_date', 'imdb_url'], axis=1)

# Cetak jumlah unik pengguna dan film
num_users = data.user_id.nunique()
num_movies = data.movie_id.nunique()

print("Jumlah Pengguna:", num_users)
print("Jumlah Film:", num_movies)

"""### **2.5. Membangun Model**
Memilih model rekomendasi yang ingin digunakan, dalam hal ini memilih SVD (Singular Value Decomposition) dari library surprise.
"""

from surprise import SVD, Dataset, Reader
from surprise.model_selection import cross_validate

# Membuat objek Reader untuk membaca dataset
reader = Reader(rating_scale=(1, 5))

# Memuat dataset MovieLens ke objek Dataset
data = Dataset.load_from_df(ratings[['user_id', 'movie_id', 'rating']], reader)

# Inisialisasi model SVD
svd = SVD()

# Evaluasi model menggunakan cross-validation
cross_validate(svd, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

"""### **2.6. Melatih Model dan Menguji Sistem**
Melatih model rekomendasi menggunakan seluruh data rating dan menguji sistem dengan memberikan rekomendasi kepada pengguna.
"""

# Latih model dengan seluruh data rating
trainset = data.build_full_trainset()
svd.fit(trainset)

# Contoh memberikan rekomendasi untuk pengguna dengan ID 5
user_id = 5
user_ratings = ratings[ratings['user_id'] == user_id]
user_unseen_movies = movies[~movies['movie_id'].isin(user_ratings['movie_id'])]

# Buat prediksi rating untuk film yang belum ditonton pengguna
user_unseen_movies['predicted_rating'] = user_unseen_movies['movie_id'].apply(lambda x: svd.predict(user_id, x).est)

# Urutkan film berdasarkan prediksi rating
user_recommendations = user_unseen_movies.sort_values(by='predicted_rating', ascending=False).head(5)

print(user_recommendations)

"""## **3. Kesimpulan**
Dalam proyek ini, kami berhasil membangun sistem rekomendasi menggunakan dataset MovieLens dan algoritma Collaborative Filtering dengan metode Matrix Factorization (SVD).

Sistem rekomendasi ini dapat memberikan rekomendasi film kepada pengguna berdasarkan preferensi mereka.

Proyek ini menunjukkan pentingnya penggunaan algoritma rekomendasi untuk memberikan pengalaman yang lebih personal kepada pengguna.

Kita dapat mengembangkan proyek ini lebih lanjut dengan mengeksplorasi teknik lain seperti Content-Based Filtering atau Hybrid Filtering untuk meningkatkan kinerja sistem rekomendasi.
"""