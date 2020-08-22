import numpy as np

# Use Broadcasting to create a 4 x 4 ndarray that has its first
# column full of 1s, its second column full of 2s, its third
# column full of 3s, etc.. 
A = np.ones((4,4),dtype = int) 
B = np.arange(4)
X = A + B
print(X) 