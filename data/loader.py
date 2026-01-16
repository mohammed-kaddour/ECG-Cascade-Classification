import os
import cv2
import numpy as np

def load_ecg_images(folder, img_size=(224, 224)):
    images = []
    for filename in sorted(os.listdir(folder)):
        path = os.path.join(folder, filename)
        img = cv2.imread(path)
        if img is not None:
            img = cv2.resize(img, img_size)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = gray / 255.0  # Normalization
            images.append(gray)
    return np.array(images)
