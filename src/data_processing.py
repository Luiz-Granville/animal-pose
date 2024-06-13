import cv2
import numpy as np
import matplotlib.pyplot as plt

def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def normalize_image(image):
    return image / 255.0

def apply_gaussian_filter(image, kernel_size=5):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

def detect_edges(image, low_threshold=50, high_threshold=150):
    return cv2.Canny(image, low_threshold, high_threshold)

def process_image(image, keypoints, new_width, new_height):
    # Redimensionar a imagem e ajustar os keypoints
    resized_image, adjusted_keypoints = resize_image_and_adjust_keypoints(image, keypoints, new_width, new_height)
    
    
    # Converter para escala de cinza
    grayscale_image = convert_to_grayscale(resized_image)
   
    # Normalizar a imagem
    normalized_image = normalize_image(grayscale_image)
   
    # Aplicar filtro gaussiano
    filtered_image = apply_gaussian_filter(normalized_image)
  
    
    # Detectar bordas
    edges_image = detect_edges((filtered_image * 255).astype(np.uint8))  # Converter de volta para uint8 para detecção de bordas
    
    
    return edges_image, adjusted_keypoints

def resize_image_and_adjust_keypoints(image, keypoints, new_width, new_height):
    original_height, original_width = image.shape[:2]
    
    # Redimensionar a imagem
    resized_image = cv2.resize(image, (new_width, new_height))
    
    # Calcular a escala
    x_scale = new_width / original_width
    y_scale = new_height / original_height
    
    # Ajustar os keypoints
    adjusted_keypoints = []
    for x, y, v in keypoints:
        if v > 0:  # Só ajustar pontos visíveis
            new_x = int(x * x_scale)
            new_y = int(y * y_scale)
            adjusted_keypoints.append((new_x, new_y, v))
        else:
            adjusted_keypoints.append((x, y, v))  # Mantém pontos invisíveis como estão
    
    return resized_image, adjusted_keypoints