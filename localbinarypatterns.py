import os
import cv2
import numpy as np
from skimage.feature import local_binary_pattern
from matplotlib import pyplot as plt

# Função para calcular o histograma do LBP
def calculate_lbp_histogram(image, num_points, radius):
    lbp = local_binary_pattern(image, num_points, radius, method='uniform')
    hist, _ = np.histogram(lbp.ravel(), bins=np.arange(0, num_points + 3), range=(0, num_points + 2))
    hist = hist.astype("float")
    hist /= (hist.sum() + 1e-7)  # Normalização do histograma LBP
    return hist

# Pasta onde estão as imagens
folder_covid = 'images_full/covid'
folder_normal = 'images_full/normal'

# Parâmetros do LBP
num_points = 24  # Número de pontos vizinhos para o LBP
radius = 8  # Raio do círculo para o LBP

# Função para processar imagens em uma pasta e calcular características
def process_images_in_folder(folder):
    features = []
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        if os.path.isfile(img_path):
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            lbp_hist = calculate_lbp_histogram(img, num_points, radius)
            features.append(lbp_hist)
    return np.array(features)

# Processar imagens da pasta "covid"
covid_features = process_images_in_folder(folder_covid)

# Processar imagens da pasta "normal"
normal_features = process_images_in_folder(folder_normal)

# Calcular média das características para cada classe (covid e normal)
avg_covid_features = np.mean(covid_features, axis=0)
avg_normal_features = np.mean(normal_features, axis=0)

# Exibir as características (histogramas) médias para cada classe
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.bar(range(len(avg_covid_features)), avg_covid_features)
plt.title('Average Features - COVID')

plt.subplot(1, 2, 2)
plt.bar(range(len(avg_normal_features)), avg_normal_features)
plt.title('Average Features - Normal')

plt.tight_layout()
plt.show()
