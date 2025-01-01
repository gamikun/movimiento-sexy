from math import sin, cos, pi

def circumference(n, r=1, xy=(0, 0), time=1.0):
    x, y = xy
    t = pi * 2 / n
    return [
        (cos(t * i) * r + x, -sin(t * i) * r + y)
        for i in range(n)
    ]

def arc_pos(n, i, r=1.0, xy=(0, 0), time=1.0):
    x, y = xy
    t = pi * 2 / n
    return (
        cos(t * i * time) * r + x,
        sin(t * i * time) * r + y,
    )