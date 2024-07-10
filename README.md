# Klusterisasi Gambar menggunakan KMeans
#### AdamDwiMaulana 312210242 TI22B1

Kali ini kita akan klusterisasi sebuah foto atau gambar dengan algoritma KMeans.

sebelumnya kita berkenalan terlebih dahulu dengan KMeans

K-Means adalah salah satu algoritma clustering yang paling populer dalam analisis data. Tujuannya adalah untuk mengelompokkan data ke dalam k kelompok berdasarkan atribut yang mirip. Algoritma ini bekerja dengan cara mengiterasi antara dua langkah utama:

Assign: Mengatribusikan setiap titik data ke kelompok yang paling dekat dengannya berdasarkan nilai rata-rata (centroid) kelompok tersebut.

Update: Memperbarui posisi centroid untuk setiap kelompok dengan menghitung nilai rata-rata dari semua titik data yang telah diatribusikan ke kelompok tersebut.

Iterasi ini terus berlanjut hingga tidak ada perubahan signifikan dalam atribusi titik data ke kelompok atau posisi centroid. K-Means biasanya digunakan untuk analisis cluster di mana jumlah kelompok (k) telah ditentukan sebelumnya.


Pada script `kmean.py` akan menjalankan klusterisasi dalam beberapa kali tergantung
apa yang kita masukan pada bagian
`k = 7`

Untuk menjalankan program pastikan anda sudah menginstall library yang dibutuhkan sebagai berikut :
`pip install opencv-python numpy matplotlip scikit-learn`

setelah itu untuk merunning silahkan ketik `python kmean.py`

nanti akan muncul gambar original lalu anda bisa close untuk menampilkan iterasi gambar yang sudah terclusterisasi waktu tunggu sekitar 1 menit untuk proses cluterisasi setelah anda close gambar yang pertama

Berikut Foto original sebelum diklusterisasi


![image](/img/foto1.jpeg)


Berikut hasil foto yang sudah mengalami perubahan sebanyak 7 kali ini bergantung pada script ` k =`

### Segmented image

![segmented](/hasil_clusterisasi/Segmented.png)

### Cluster1 image

![cluster1](/hasil_clusterisasi/Cluster_1.png)

### Cluster_2 image

![cluster_2](/hasil_clusterisasi/Cluster_2.png)

### Cluster_3 image

![cluster_3](/hasil_clusterisasi/Cluster_3.png)

### Cluster_4 image

![cluster_4](/hasil_clusterisasi/Cluster_4.png)

### Cluster_5 image

![cluster_5](/hasil_clusterisasi/Cluster_5.png)

### Cluster_6 image

![cluster_6](/hasil_clusterisasi/Cluster_6.png)

### Cluster_7 image

![cluster_7](/hasil_clusterisasi/Cluster_7.png)

Untuk melakukan clusterisasi membutuhkan waktu untuk prosesnya jadi untuk memunculkan hasilnya butuh waktu sekitar 1 menit atau lebih ini bergantung kepada kapasitas device kita. semaking tinggi spesifikasi device semakin cepat dia dalam memprosesnya.


Selesai untuk nilai K  anda bisa memasukan sesuai keinginan anda.

Selamat mencoba, semoga bermanfaat

#### Link Tugas UTS pengolahan Citra

Github :
[https://github.com/adamdwidev/uts-pengolahan-citra](https://github.com/adamdwidev/uts-pengolahan-citra)

Hasil Streamlit :
[https://adamwebdev.streamlit.app/tugas](https://adamwebdev.streamlit.app/tugas)




