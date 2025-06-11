import stokes
import numpy as np
import matplotlib.pyplot as plt

a = r'C:\Proyectos\Speckle\Stokes-parameters\images'
prueba1 = stokes.intensidades()

media, desviacion = prueba1.darkness(ruta = r"C:\Proyectos\Stokes-parameters\images\Pol L Vert\darks")

prueba1.parameters(ruta= r"C:\Proyectos\Stokes-parameters\images\Pol L Vert", 
                    media_dark = media,
                    desviacion_dark= desviacion)
prueba2 = stokes.intensidades()

media, desviacion = prueba2.darkness(ruta = r"C:\Proyectos\Stokes-parameters\images\Pol L H\darks")
prueba2.parameters(ruta= r"C:\Proyectos\Stokes-parameters\images\Pol L H", 
                    media_dark = media,
                    desviacion_dark= desviacion)


prueba3 = stokes.intensidades()
media, desviacion = prueba3.darkness(ruta = r"C:\Proyectos\Stokes-parameters\images\Pol C I\darks")
prueba3.parameters(ruta= r"C:\Proyectos\Stokes-parameters\images\Pol C I", 
                    media_dark = media,
                    desviacion_dark= desviacion)

prueba4 = stokes.intensidades()
media, desviacion = prueba4.darkness(ruta = r"C:\Proyectos\Stokes-parameters\images\Pol C D\darks")
prueba3.parameters(ruta= r"C:\Proyectos\Stokes-parameters\images\Pol C D", 
                    media_dark = media,
                    desviacion_dark= desviacion)