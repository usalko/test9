from typing import List
from .point2d import Point2D


def de_casteljau(points: List[Point2D], t: float) -> Point2D:
    a = Point2D()
    b = Point2D()
    midpoints = []
    while len(points) > 1:
        num = len(points) - 1
        for i in range(0, num):
            a = points[i]
            b = points[i+1]
            midpoints.add(Point2D(
                a.x0 + (b.x0 - a.x0) * t,
                a.x1 + (b.x1 - a.x1) * t,   
            ))

        points = midpoints
        midpoints = []

    return points[0] # Object.assign(points[0], {in: a, out: b});
