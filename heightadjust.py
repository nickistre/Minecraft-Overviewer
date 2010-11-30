'''
Created on Nov 29, 2010

@author: nick
'''
import math
from PIL import ImageEnhance

def get_heightmap_func(type = None):
    """Creates and returns a function and the ImageEnhance module class to go 
    with it as a tuple, depending on the type passed in."""
    if type == 'heightlog':
        return [lambda z: (1/(1+math.exp(-1*(1.3*z/16)+6.0)))*.3, ImageEnhance.Brightness]
    if type == 'heightlog2':
        return [lambda z: (1/(1+math.exp(-1.*(z-70.)/11.)))*0.6-0.55, ImageEnhance.Brightness]
    if type == 'heightlinear':
        return [lambda z: ((z / 128.0) **2) * 0.3, ImageEnhance.Brightness]
    return [lambda x: 0, ImageEnhance.Brightness]