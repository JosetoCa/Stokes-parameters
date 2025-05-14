import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


class intensidades:

    def __init__(self):
        
        self.imagenI_0 = None
        self.imagenI_90 = None
        self.imagenI_45 = None
        self.imagenI_135 = None
        self.imagen_RHC = None
        self.imagen_LHC = None
        self.s_0 = None
        self.s_1 = None
        self.s_2 = None
        self.s_3 = None

    def parameters(self, nombre_I_0:str = None, nombre_I_90:str = None, nombre_I_45:str = None, nombre_I_135:str = None, nombre_I_RHC:str = None, nombre_I_LHC:str = None):
    
        self.imagenI_0 = np.array(Image.open(nombre_I_0).convert('L'), dtype=np.int32)

        self.imagenI_90 = np.array(Image.open(nombre_I_90).convert('L'), dtype=np.int32)
        
        self.imagenI_45 = np.array(Image.open(nombre_I_45).convert('L'), dtype=np.int32)
        
        self.imagenI_135 = np.array(Image.open(nombre_I_135).convert('L'), dtype=np.int32)

        self.imagen_RHC = np.array(Image.open(nombre_I_RHC).convert('L'), dtype=np.int32)

        self.imagen_LHC = np.array(Image.open(nombre_I_LHC).convert('L'), dtype=np.int32)
        a = np.sum(self.imagenI_45)
        b = np.sum(self.imagenI_135)

        self.s_0 = np.sum(self.imagenI_0) + np.sum(self.imagenI_90)
        self.s_1 = (np.sum(self.imagenI_0) - np.sum(self.imagenI_90))/self.s_0
        self.s_2 = (a - b)/self.s_0
        self.s_3 = (np.sum(self.imagen_RHC) - np.sum(self.imagen_LHC))/self.s_0
        self.s_0 = 1


        print("s_0: ", self.s_0)
        print("s_1: ", self.s_1)
        print("s_2: ", self.s_2)
        print("s_3: ", self.s_3)


