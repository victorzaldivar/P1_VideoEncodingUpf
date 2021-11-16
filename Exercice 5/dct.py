import os
import sys
from scipy.fftpack import dct
from scipy.fftpack import idct
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("Lena.png") #cargar el archivo .png al script
imageGRAY = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #cargo imagen en blanco y negro ya que el DCT se aplica sobre este tipo de imágenes
#aplicamos DCT y su inversa
dct_image = dct(imageGRAY)
idct_image = idct(dct_image)

#ploteamos Imagen original en Blanco y negro
plt.gray()
plt.subplot(121)
plt.imshow(image)
plt.title('Original image')

#ploteamos Imagen tras el methodo DCT
plt.subplot(122)
plt.imshow(idct_image)
plt.title('DCT image')

plt.show()

