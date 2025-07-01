import cv2
import numpy as np

IMG_SIZE = (224, 224)

def preprocess_image(file_bytes):
    np_arr = np.frombuffer(file_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_GRAYSCALE)

    img = cv2.equalizeHist(img)
    img = cv2.resize(img, IMG_SIZE)

    img = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 11, 2
    )

    normalized = img / 255.0
    reshaped = normalized.reshape(1, IMG_SIZE[0], IMG_SIZE[1], 1)
    return reshaped
