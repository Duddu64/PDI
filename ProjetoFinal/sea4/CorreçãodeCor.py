import cv2
import numpy as np

def ajustar_contraste(image):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    l_clahe = clahe.apply(l)
    lab_clahe = cv2.merge((l_clahe, a, b))
    image_clahe = cv2.cvtColor(lab_clahe, cv2.COLOR_LAB2BGR)
    return image_clahe

def corrigir_cor(image):
    result = cv2.addWeighted(image, 1.5, cv2.GaussianBlur(image, (0, 0), 15), -0.8, 0)  # Ajuste pesado
    return result

def processar_imagem_subaquatica(caminho_imagem):
    image = cv2.imread(caminho_imagem)
    
    if image is None:
        print("Erro ao carregar a imagem.")
        return

    cv2.imshow('Imagem Original', image)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()

    image_contraste = ajustar_contraste(image)

    cv2.imshow('Imagem Após Ajuste de Contraste', image_contraste)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()

    image_corrigida = corrigir_cor(image_contraste)

    cv2.imshow('Imagem Corrigida', image_corrigida)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()

    cv2.imwrite('resultado\imagem_corrigida_turtle.jpg', image_corrigida)

caminho_imagem = r'fonte\000105.JPG'
processar_imagem_subaquatica(caminho_imagem)
