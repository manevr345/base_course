from module_const import planck_const as hplanck
from module_const import g
from module_const import sigma_steff_bolc as sigma

import math
h = 100
a = math.pi / 4
b = (math.pi * 35)/180
u = math.sqrt((g * h * (math.tan(b)**2))/(2 * (math.cos(a)**2 * (1 - math.tan(b)*math.tan(a)))))
print(f' U = {u}')


T = 200
era = 300

N = 2/math.sqrt(math.pi) * math.sqrt(hplanck) * (sigma * T)**1.5 * era**(T/2) * (math.e)**(era/(sigma * T))
print(f'N = {N}')
print(math.e)