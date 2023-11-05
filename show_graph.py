import matplotlib.pyplot as plt
import numpy as np
import find_point
from tkinter import *
from tkinter import ttk


def show_graph():
    dots = np.random.rand(int(point_num.get()), 2)
    dots = find_point.sort_counterclockwise(dots)
    gravity_point = find_point.get_polygon_gravity(dots)
    dots = np.append(dots, dots[0])
    dots = dots.reshape((int(dots.size/2), 2))

    plt.figure()
    plt.plot(dots[:, 0], dots[:, 1])
    plt.plot(gravity_point[0], gravity_point[1], "ro-")

    plt.show()


window = Tk()
window.title("Find Gravity Point")
window.resizable(False, False)

# 서 북 동 남
mainframe = ttk.Frame(window, padding="20 20 20 20")
mainframe.grid(column=0, row=0)
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

title_label1 = Label(mainframe, text="Polygon Gravity Point", font="arial")
title_label1.grid(column=1, row=1, columnspan=2, pady=15)

point_num_label = Label(mainframe, text="Number of Points:")
point_num_label.grid(column=1, row=2, sticky=(E))
point_num = StringVar()
point_num.set('5')
point_num_entry = ttk.Entry(mainframe, width=10, textvariable=point_num)
point_num_entry.grid(column=2, row=2, pady=12)
rand_button = Button(mainframe, text="Generate Random Points", command=show_graph)
rand_button.grid(column=1, row=3, columnspan=2, pady=5)

window.mainloop()
