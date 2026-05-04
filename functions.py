import numpy as np        
import cv2                

def get_limits(color):    # fonction qui reçoit une couleur en BGR
    # format attendu par OpenCV : (height, width, channels)
    c = np.uint8([[color]])#Parce que chaque canal couleur utilise 8 bits.

    # convertir cette mini image de BGR vers HSV
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    # on prend Hue - 10 pour créer une petite plage de couleur
    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    # Hue + 10 donne la limite supérieure de la plage
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    # convertir les limites en tableaux numpy (format nécessaire pour OpenCV)
    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    # retourner les deux limites HSV
    return lowerLimit, upperLimit