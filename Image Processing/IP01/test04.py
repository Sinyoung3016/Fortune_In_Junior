import matplotlib.pyplot as plt
import numpy as np

a = range(0, 100, 10)
b = range(0, 100, 10)
c = np.random.randint(100, size = 20)
d = np.random.randint(100, size = 20)

plt.plot(a,b)
plt.scatter(c,d)

plt.xlabel('0 to 10 x')
plt.ylabel('0 to 10 y')

plt.title('plot and scatter')
plt.legend(['ab','cd'])
plt.show()