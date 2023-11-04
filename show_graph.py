import matplotlib.pyplot as plt
import numpy as np
import find_point

#점 4개 찍으면 무게중심 찾아줌
dots = np.array([
])

gravity_point = find_point.get_square_gravity(dots)
plt.figure()
for dot in dots:
    plt.plot(dot[0], dot[1], "bo-")
plt.plot(gravity_point[0], gravity_point[1], "ro-")

plt.show()
