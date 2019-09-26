from graph import *
windowSize(1000,600)
canvasSize(1000,600)
from graph import *
def ellips( a, b, x0, y0):
    """
    ellips_
    :param a : -size_gorizontal_line
    :param b : -size_vertical_line
    :param x0: -x coordinate_of_ellips_center
    :param y0: -y coordinate_of_ellips_center
    """
    x = a
    y = 0
    s = [(x0 + a, y0)]
    for i in range(2 * a):
        x -= 1
        y = ((1 - x ** 2 / (a ** 2)) * b ** 2) ** 0.5
        s.append((x + x0, y + y0))
    for i in range(2 * a):
        y = -(((1 - x ** 2 / (a ** 2)) * b ** 2) ** 0.5)
        s.append((x + x0, y + y0))
    polygon(s)

