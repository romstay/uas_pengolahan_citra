import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# Membaca gambar dari file
image = cv2.imread('foto1.jpeg')  # Ganti dengan path ke file gambar Anda
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Konversi BGR ke RGB

# Menampilkan gambar asli
plt.figure(figsize=(8, 8))
plt.imshow(image)
plt.title('Gambar Asli')
plt.show()

# Mengubah gambar menjadi bentuk 2D
pixel_values = image.reshape((-1, 3))
pixel_values = np.float32(pixel_values)

# Membuat label untuk KNN (misalnya, kita gunakan label manual untuk latihan)
# Pada praktiknya, Anda akan memiliki data label untuk segmentasi
labels = np.zeros((pixel_values.shape[0],), dtype=int)

# Misal kita labeli beberapa pixel secara manual untuk KNN
# Label 1 untuk latar belakang, 2 untuk objek yang ingin disegmentasi
# Contoh data latih (manual untuk contoh)
labels[1000:2000] = 1  # beberapa piksel untuk latar belakang
labels[5000:6000] = 2  # beberapa piksel untuk objek

# Melatih model KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(pixel_values, labels)

# Prediksi label untuk setiap piksel dalam gambar
segmented_labels = knn.predict(pixel_values)

# Mengubah label hasil segmentasi ke bentuk gambar
segmented_image = segmented_labels.reshape(image.shape[0], image.shape[1])

# Menampilkan gambar hasil segmentasi
plt.figure(figsize=(8, 8))
plt.imshow(segmented_image, cmap='viridis')
plt.title('Gambar Hasil Segmentasi')
plt.show()

# Menyimpan gambar hasil segmentasi
cv2.imwrite('segmented_image_knn.jpg', segmented_image)
