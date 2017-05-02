import numpy
from matplotlib import pyplot as plt

_data_len = 50

# fake your data:
data_x, data_y = numpy.random.random((2,_data_len))

sizes = numpy.random.random((1,_data_len))
colours = numpy.random.random((_data_len))

fig, ax = plt.subplots()

ax.scatter(data_x,data_y,s=250*sizes, c=colours, alpha=0.5, cmap='Spectral')
ax.set_xlim(0,1)
ax.set_ylim(0,1)
plt.show()