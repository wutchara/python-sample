import numpy as np
# If you not installed numpy yet, Please use this command to install
# 'python -m pip install numpy'

def max(lists):
    return np.max(lists)


array = [1, 5, 9, 10, 99, 5, 85]
print("Lists: ", array)
print("Maximum: ", max(array))