# First set up the figure, the axis, and the plot element we want to animate

from class_customer import Customer
import numpy as np
from matplotlib import pyplot as plt


# fig = plt.figure()
# ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
# # d, = ax.plot([dot.x for dot in dots],
# #              [dot.y for dot in dots], 'ro')
# circle = plt.Circle((5, 5), 1, color='b', fill=False)
# ax.add_artist(circle)
customer_list = []
for k in range(0,10):
    customer_list.append(Customer(k))



### Creation of map ###########

##### Adapt this with your location of market.png###### 
PATH = "/home/gkuer/spiced_kurs/spiced_projects/re-netto-project/visualization/market.png"
#####            ####### 

img = plt.imread(PATH)
fig, ax = plt.subplots()
ax.imshow(img, extent=[-5, 120, -2, 60])
# Dimensions of locations:

plt.show()