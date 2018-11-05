import numpy as np
import colour
import math
from __future__ import division

def sigmoid(x, stretch, shift):
    return 1 / (1 + math.exp(stretch * -x + shift))

def brightness(t, duration):
    return sigmoid((t / (duration / 2), 9, 6))

def temperature(t, duration):
    x = t / duration
    if (x < 1):
        return 3200 + (x * 2300)
    return 5500

def color(t, duration):
    xy = colour.CCT_to_xy_Kang2002(temperature(t, duration))
    xyz = colour.xy_to_XYZ(xy)

    illuminant_XYZ = np.array([0.34570, 0.35850])
    illuminant_RGB = np.array([0.31270, 0.32900])
    xyz_to_rgb_matrix = np.array(
        3.2404542, -1.5371385, -0.4985314,
        -0.9692660, 1.8760108, 0.0415560,
        0.0556434, -0.2040259, 1.0572252)
    return colour.XYZ_to_RGB(xyz, illuminant_XYZ, illuminant_RGB, xyz_to_rgb_matrix)

duration = 9000 # seconds



