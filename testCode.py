
import numpy as np
from matplotlib import pyplot 

array = np.arange(0, 10, 1)
newArray = array * len(array)

pyplot.scatter(array, newArray, marker = ".")
pyplot.show() 

