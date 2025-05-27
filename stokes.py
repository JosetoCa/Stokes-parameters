import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


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

    def parameters(self, I_1:str = None, 
                   I_2:str = None, 
                   I_3:str = None, 
                   I_4:str = None, 
                   I_5:str = None, 
                   I_6:str = None,
                   I_7:str = None,
                   I_8:str = None,
                   I_9:str = None,
                   I_10:str = None
                   ):
        
        self.imagenI_1 = np.array(Image.open(I_1).convert('L'), dtype=np.int32)

        self.imagenI_2 = np.array(Image.open(I_2).convert('L'), dtype=np.int32)

        self.imagenI_3 = np.array(Image.open(I_3).convert('L'), dtype=np.int32)

        self.imagenI_4 = np.array(Image.open(I_4).convert('L'), dtype=np.int32)

        self.imagenI_5 = np.array(Image.open(I_5).convert('L'), dtype=np.int32)

        self.imagenI_6 = np.array(Image.open(I_6).convert('L'), dtype=np.int32)

        self.imagenI_7 = np.array(Image.open(I_7).convert('L'), dtype=np.int32)

        self.imagenI_8 = np.array(Image.open(I_8).convert('L'), dtype=np.int32)

        self.imagenI_9 = np.array(Image.open(I_9).convert('L'), dtype=np.int32)

        self.imagenI_10 = np.array(Image.open(I_10).convert('L'), dtype=np.int32)


        intensidades = [np.sum(self.imagenI_1), np.sum(self.imagenI_2), 
                        np.sum(self.imagenI_3), np.sum(self.imagenI_4), 
                        np.sum(self.imagenI_5), np.sum(self.imagenI_6), 
                        np.sum(self.imagenI_7), np.sum(self.imagenI_8), 
                        np.sum(self.imagenI_9), np.sum(self.imagenI_10)]

        A = 0
        B = 0
        C = 0
        D = 0

        for i in range(0, len(intensidades)):
            A += intensidades[i]
        A = A * 2/(len(intensidades))

        for i in range(0, len(intensidades)):
            B += intensidades[i] * np.sin((2*i*np.pi)/len(intensidades))
        B = B * 4/(len(intensidades))

        for i in range(0, len(intensidades)):
            C += intensidades[i] * np.cos((4*i*np.pi)/len(intensidades))
        C = C * 4/(len(intensidades))

        for i in range(0, len(intensidades)):
            D += intensidades[i] * np.sin((4*i*np.pi)/len(intensidades))
        D = D * 4/(len(intensidades))



        self.s_0 = A - C
        self.s_1 = 2* C / self.s_0
        self.s_2 = 2 * D/self.s_0
        self.s_3 = B / self.s_0
        self.s_0 = 1


        print("s_0: ", self.s_0)
        print("s_1: ", self.s_1)
        print("s_2: ", self.s_2)
        print("s_3: ", self.s_3)


