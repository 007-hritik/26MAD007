import numpy as np

x = np.array([[2, 10],
              [4, 20],
              [6, 30]])

x_norm = (x - x.min(axis=0)) / (x.max(axis=0) - x.min(axis=0))

print(x_norm)