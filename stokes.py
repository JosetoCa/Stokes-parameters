import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os


class intensidades:

    def __init__(self):
        
        self.imagenI_1 = None
        self.imagenI_2 = None
        self.imagenI_3 = None
        self.imagenI_4 = None
        self.imagenI_5 = None
        self.imagenI_6 = None
        self.imagenI_7 = None
        self.imagenI_8 = None
        self.imagenI_9 = None
        self.imagenI_10 = None

        self.s_0 = None
        self.s_1 = None
        self.s_2 = None
        self.s_3 = None

    def parameters(self,
                   ruta:str = None,
                   media_dark = None,
                   desviacion_dark = None
                   ):
        
        archivos = [f for f in os.listdir(ruta) if f.endswith('.tif') ]
        print(archivos)
        imagenes = []
        

        for archivo in archivos:
            ruta_completa = os.path.join(ruta, archivo)
            img = Image.open(ruta_completa).convert('L')
            if media_dark is not None and desviacion_dark is not None:
                img = np.array(img, dtype=np.int32)
                img = (img - media_dark)
                img = np.where(img <= media_dark - 2*desviacion_dark, 0, img)
            imagenes.append(np.array(img, dtype=np.float32))
        stack = np.stack(imagenes, axis = 0)

        A = 0
        B = 0
        C = 0
        D = 0

        for i in range(10):
            A += np.sum(stack[i])
        A = A * 2/(10)

        for i in range(10):
            B += np.sum(stack[i]) * np.sin((2*i*np.pi)/10)
        B = B * 4/(10)

        for i in range(10):
            C += np.sum(stack[i]) * np.cos((4*i*np.pi)/10)
        C = C * 4/(10)

        for i in range(10):
            D += np.sum(stack[i]) * np.sin((4*i*np.pi)/10)
        D = D * 4/(10)



        self.s_0 = A - C
        self.s_1 = 2* C / self.s_0
        self.s_2 = 2 * D/self.s_0
        self.s_3 = B / self.s_0
        self.s_0 = 1


        print("s_0: ", self.s_0)
        print("s_1: ", self.s_1)
        print("s_2: ", self.s_2)
        print("s_3: ", self.s_3)
    
    def darkness(self, ruta:str = None):
        """ Lee las imágenes .tif en una carpeta y calcula media y desviación estándar de cada píxel.

        Args:
            ruta (str): Ruta de la carpeta con las imágenes .tif.
        Returns:
            media (ndarray): Imagen promedio (float32)
            desviacion (ndarray): Imagen de desviación estándar (float32)
        """
        archivos = [f for f in os.listdir(ruta) if f.endswith('.tif') ]
        imagenes = []

        for archivo in archivos:
            ruta_completa = os.path.join(ruta, archivo)
            img = Image.open(ruta_completa).convert('L')
            imagenes.append(np.array(img, dtype=np.float32))
        stack = np.stack(imagenes, axis = 0)
        media = np.mean(stack, axis = 0)
        desviacion = np.std(stack, axis = 0)
        
        
        return media, desviacion


