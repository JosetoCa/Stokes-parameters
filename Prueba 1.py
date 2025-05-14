import stokes
import numpy as np
import matplotlib.pyplot as plt


a = "C:\Proyectos\Stokes-parameters"
prueba1 = stokes.intensidades()
prueba1.parameters(nombre_I_0= a+'\images\I_0_prueba.tif', nombre_I_90 = a+'\images\I_90_prueba.tif', nombre_I_45=a+'\images\I_45_prueba.tif', nombre_I_135=a+'\images\I_135_prueba.tif', nombre_I_RHC=a+'\images\I_RHC_prueba.tif', nombre_I_LHC=a+'\images\I_LHC_prueba.tif')
prueba2 = stokes.intensidades()
prueba2.parameters(nombre_I_0= a+'\images\I_0_prueba1.tif', nombre_I_90 = a+'\images\I_90_prueba1.tif', nombre_I_45=a+'\images\I_45_prueba1.tif', nombre_I_135=a+'\images\I_135_prueba1.tif', nombre_I_RHC=a+'\images\I_RHC_prueba1.tif', nombre_I_LHC=a+'\images\I_LHC_prueba1.tif')