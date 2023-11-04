import matplotlib.pyplot as plt
import numpy as np
import find_point

dots = np.random.rand(5, 2)

gravity_point = find_point.get_polygon_gravity(dots)
plt.figure()
for dot in dots:
    plt.plot(dot[0], dot[1], "bo-")
plt.plot(gravity_point[0], gravity_point[1], "ro-")

plt.show()
