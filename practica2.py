import numpy as np
from matplotlib import pyplot as plt
import cv2 #opencv
#from tkinder import*

imagen1x = cv2.imread('mar.png',1)
ancho = imagen1x.shape [1]
alto = imagen1x.shape[0]
imagen1x_out= cv2.resize(imagen1x,(550,350),interpolation= cv2.INTER_CUBIC)
imagen2x = cv2.imread('espacio.png',1)
ancho = imagen2x.shape [2]
alto = imagen2x.shape[1]
imagen2x_out= cv2.resize(imagen2x,(550,350),interpolation= cv2.INTER_CUBIC)
cv2.imshow("Mar1",imagen1x_out)
cv2.imshow("Espacio1", imagen2x_out)
cv2.waitKey(0)
cv2.destroyAllWindows()

imagen1 = cv2.imread('mar.png',1)
ancho = imagen1.shape [1]
alto = imagen1.shape[0]
imagen1_out= cv2.resize(imagen1,(400,200),interpolation= cv2.INTER_CUBIC)
imagen2 = cv2.imread('espacio.png',1)
ancho = imagen2.shape [1]
alto = imagen2.shape[0]
imagen2_out= cv2.resize(imagen2,(400,200),interpolation= cv2.INTER_CUBIC)
res1 = cv2.resize(imagen1, (300,150), interpolation= cv2.INTER_CUBIC)
res2 = cv2.resize(imagen2, (300,150), interpolation= cv2.INTER_CUBIC)

suma_f = cv2.add(res1,res2) #suma
resta_f = cv2.subtract(res1,res2) #resta
multiplicacion_f = cv2.addWeighted(res1,0.2,res2,0.8,0) #multiplicacion
Matriz = np.float32([[1,0,350],[0,1,10]]) #Traslacion
traslacion_f = cv2.warpAffine(res1,Matriz,(ancho,alto))

cv2.imshow('Traslacion',traslacion_f)
cv2.imshow("Mar",imagen1_out)
cv2.imshow("Espacio", imagen2_out)
cv2.imshow('Adicion',suma_f)
cv2.imshow('Resta',resta_f)
cv2.imshow('Multiplicacion',multiplicacion_f)
cv2.waitKey(0)
cv2.destroyAllWindows()
