import cv2
import numpy as np

def img_filtrada(pasta_img):
    # Carregar a imagem
    img = cv2.imread(pasta_img)
    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    cv2.imshow('Imagem Original', cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR))
    cv2.waitKey(0)
    
    red_channel = img_rgb[:, :, 0]
    green_channel = img_rgb[:, :, 1]
    blue_channel = img_rgb[:, :, 2]
    
    # Equalizando o histograma de cada canal
    red_channel = cv2.equalizeHist(red_channel)
    green_channel = cv2.equalizeHist(green_channel)
    blue_channel = cv2.equalizeHist(blue_channel)
    
    img_rgb[:, :, 0] = red_channel
    img_rgb[:, :, 1] = green_channel
    img_rgb[:, :, 2] = blue_channel
    
    cv2.imshow('Imagem Após Equalização do Histograma', cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR))
    cv2.waitKey(0)
    
    img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
    
    sobel_x = cv2.Sobel(img_bgr, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(img_bgr, cv2.CV_64F, 0, 1, ksize=3)
    
    edges = cv2.magnitude(sobel_x, sobel_y)
    edges = np.uint8(np.clip(edges, 0, 255))
    
    cv2.imshow('Imagem com Bordas Destacadas', edges)
    cv2.waitKey(0)
    
    img_ruido = cv2.bilateralFilter(img_bgr, 9, 75, 75)
    
    cv2.imshow('Imagem Após Redução de Ruído', img_ruido)
    cv2.waitKey(0)
    
    img_ruido_rgb = cv2.cvtColor(img_ruido, cv2.COLOR_BGR2RGB)
    
    result = cv2.addWeighted(img_ruido_rgb, 0.9, edges, 0.1, 0)
    
    cv2.imshow('Bordas + Equalização', cv2.cvtColor(result, cv2.COLOR_RGB2BGR))
    cv2.waitKey(0)
    
    cv2.imwrite(r'resultado\img_filtrada_equa.jpg', cv2.cvtColor(result, cv2.COLOR_RGB2BGR))
    
    cv2.destroyAllWindows()

pasta_img = r'fonte\LFT_3374.png'

img_filtrada(pasta_img)
