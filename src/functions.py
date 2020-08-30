#Funciones utilizadas en el archivo de código jupyter notebook
import re
import numpy as np


def depure(x,current,new):
    if x==current:
        x=new
    return x
