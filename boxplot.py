import matplotlib.pyplot as plt
weights = [25, 28, 29, 29, 30, 34, 35, 35, 37, 38]
plt.boxplot(weights)
plt.xlabel('Weights (grams)')
plt.title('Box plot of box weights')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
x = np.random.rand(50)
y = -x + np.random.normal(0, 0.1, 50)
x = np.append(x, 0.2)
y = np.append(y, 2)
plt.scatter(x, y)
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Negative correlation with outlier')
plt.show()