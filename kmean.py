import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# membaca gambar / foto
image = cv2.imread('./img/foto1.jpeg')  # ganti image sesuai dengan path ke file gambar Anda
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
plt.title("Original Image")
plt.show()

# me reshape gambar ke bentuk 2D
pixel_values = image.reshape((-1, 3))
pixel_values = np.float32(pixel_values)

# mendefinisikan kriteria, nilai K, dan melakukan KMeans
k = 7  # ubah nilai K sesuai kebutuhan
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
_, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# mengkonversi kembali ke 8-bit values
centers = np.uint8(centers)
segmented_image = centers[labels.flatten()]

# reshape ke bentuk gambar asli
segmented_image = segmented_image.reshape(image.shape)
plt.imshow(segmented_image)
plt.title("Segmented Image")
plt.show()

# menampilkan setiap cluster
labels = labels.flatten()
segmented_images = []
for i in range(k):
    masked_image = np.copy(image)
    masked_image = masked_image.reshape((-1, 3))
    masked_image[labels != i] = [0, 0, 0]
    masked_image = masked_image.reshape(image.shape)
    segmented_images.append(masked_image)
    plt.imshow(masked_image)
    plt.title(f"Cluster {i+1}")
    plt.show()
