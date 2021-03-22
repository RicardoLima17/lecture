# messing with histograms


import numpy as np
import matplotlib.pyplot as plt

# same number generator 
#np.random.seed(1)
#normdata = np.random.normal(size=10)

#plt.hist(normdata)
#plt.show()

fruit = np.array(['apples', 'orange', 'banana'])
numbers = np.array([23, 77, 500])

plt.pie(numbers, labels = fruit)
plt.legend()
plt.show()