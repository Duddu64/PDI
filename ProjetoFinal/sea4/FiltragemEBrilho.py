import cv2
import numpy as np

def filtro_image_canny(image_path):
    img = cv2.imread(image_path)
    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    img_rgb_bright = cv2.convertScaleAbs(img_rgb, alpha=1.1, beta=3)  # alpha: contraste, beta: brilho
    
    cv2.imshow('Imagem com Ajuste de Brilho', cv2.cvtColor(img_rgb_bright, cv2.COLOR_RGB2BGR))
    cv2.waitKey(0)
    
    img_bgr_bright = cv2.cvtColor(img_rgb_bright, cv2.COLOR_RGB2BGR)
    
    edges = cv2.Canny(img_bgr_bright, 200, 200)
    
    cv2.imshow('Bordas Detectadas com Canny', edges)
    cv2.waitKey(0)
    
    edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    
    result = cv2.addWeighted(img_bgr_bright, 0.7, edges_colored, 0.3, 0)
    
    cv2.imshow('Imagem Final (Brilho + Bordas)', result)
    cv2.waitKey(0)
    
    cv2.imwrite(r'resultado\filtro_image_canny2.jpg', result)
    
    cv2.destroyAllWindows()

image_path = r'fonte\000090.JPG'

filtro_image_canny(image_path)
