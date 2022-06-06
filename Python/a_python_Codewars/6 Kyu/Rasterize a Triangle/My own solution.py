import numpy as np
import math
import matplotlib.pyplot as plt
import timeit as t
from mpl_toolkits.axisartist import SubplotZero


class Axes():

    def __init__(self, xlim=(-5, 5), ylim=(-5, 5), figsize=(12, 5)):
        self.xlim = xlim
        self.ylim = ylim
        self.figsize = figsize
        self.points = []
        self.segments = []
        self.vectors = []
        self.lines = []
        self.scale_arrows()

    def __arrow__(self, x, y, dx, dy, width, length):
        plt.arrow(
            x, y, dx, dy,
            color='k',
            clip_on=False,
            head_width=self.head_width,
            head_length=self.head_length
        )

    def __drawAxis__(self):
        """
        Draws the 2D cartesian axis
        """
        # A subplot with two additional axis, "xzero" and "yzero"
        # corresponding to the cartesian axis
        ax = SubplotZero(self.fig, 1, 1, 1)
        self.fig.add_subplot(ax)

        # make xzero axis (horizontal axis line through y=0) visible.
        for axis in ["xzero", "yzero"]:
            ax.axis[axis].set_visible(True)
        # make the other axis (left, bottom, top, right) invisible
        for n in ["left", "right", "bottom", "top"]:
            ax.axis[n].set_visible(False)

        # Plot limits
        plt.xlim(self.xlim)
        plt.ylim(self.ylim)
        # Draw the arrows
        self.__arrow__(self.xlim[1], 0, 0.01, 0, 0.3, 0.2)  # x-axis arrow
        self.__arrow__(0, self.ylim[1], 0, 0.01, 0.2, 0.3)  # y-axis arrow

    def scale_arrows(self):
        """ Make the arrows look good regardless of the axis limits """
        xrange = self.xlim[1] - self.xlim[0]
        yrange = self.ylim[1] - self.ylim[0]

        self.head_width = min(xrange / 30, 0.25)
        self.head_length = min(yrange / 30, 0.3)

    def draw(self, image=None):
        self.scale_arrows()
        self.fig = plt.figure(figsize=self.figsize)
        # First draw the axis
        self.__drawAxis__()
        # Plot each point
        for point in self.points:
            point.draw()
        # Save the image?
        if image:
            plt.savefig(image)
        plt.show()

    def addPoints(self, points):
        for p in points:
            self.addPoint(p)

    def addPoint(self, p):
        self.points.append(p)


class Point():

    def __init__(self, x, y, color='#4ca3dd', size=50, add_coordinates=True):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.add_coordinates = add_coordinates
        self.y_offset = 0.2
        self.items = np.array([x, y])
        self.len = 2

    def __getitem__(self, index):
        return self.items[index]

    def __str__(self):
        return "Point(%.2f,%.2f)" % (self.x, self.y)

    def __repr__(self):
        return "Point(%.2f,%.2f)" % (self.x, self.y)

    def __len__(self):
        return self.len

    def draw(self):
        plt.scatter([self.x], [self.y], color=self.color, s=self.size)

        # Add the coordinates if asked by user
        if self.add_coordinates:
            plt.text(
                self.x, self.y + self.y_offset,
                        "(%.1f,%.1f)" % (self.x, self.y),
                horizontalalignment='center',
                verticalalignment='bottom',
                fontsize=12
            )

triangle = ((2,1), (0, 3), (5, 4))

A, B, C = np.array(triangle)
print("A point: ",A[0])


def bresenham(x1, y1, x2, y2) -> list:
    m_new = 2 * (y2 - y1)
    slope_error_new = m_new - (x2 - x1)

    y = y1
    for x in range(x1, x2 + 1):

        yield (x, y)

        # Add slope to increment angle formed
        slope_error_new = slope_error_new + m_new

        # Slope error reached limit, time to
        # increment y and update slope error.
        if (slope_error_new >= 0):
            y = y + 1
            slope_error_new = slope_error_new - 2 * (x2 - x1)


# driver function



poggers = [i for i in [bresenham(2, 1, 0, 3)]]
print(poggers)
for i in list(poggers):
    print("tst", i)
print("test", poggers)
poggers = bresenham(0, 3, 5, 4)
print("test", poggers)
poggers = bresenham(2,1, 5, 4)
print("test", poggers)
# lst.append(bresenham(A, B))
# lst.append(bresenham(B, C))
# lst.append(bresenham(C, A))
lst = []
axes = Axes(xlim=(-6, 6), ylim=(-6, 6), figsize=(9, 7))

point_lst = [[set(i)] for i in lst]

x_lst = [x for x, y in point_lst]
y_lst = [y for x, y in point_lst]

print("x: ", x_lst)
print("y: ",y_lst)
axes.addPoints(point_lst)
axes.draw()

def draw_triangle(triangle, n):
    for y in range(n):
        for x in range(n):
            print([x, y])
    pass


triangle = [(2, 1), (0, 3), (5, 4)]
# print(draw_triangle(triangle, 6))
# print("Run time:", t.timeit(lambda: draw_triangle(triangle, 6), number=10000))
#
# triangle = [(1, -49997), (2, 3), (3, 50002)]
# print(draw_triangle(triangle, 6))
# print("Run time:", t.timeit(lambda: draw_triangle(triangle, 6), number=10000))