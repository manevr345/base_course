
import os
filenames = [f'pic{i}.png' for i in range(100)]
for filename in filenames:
    os.remove(filename)
