#Funciones utilizadas en el archivo de código jupyter notebook
import re
import numpy as np
def reference(x):
    return re.split("shark",x)

def percentage(x,y):
    return x/len(y)
