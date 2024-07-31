from typing import List


def de_casteljau_complex(points: List[complex], t: float) -> complex:
    a = 0 + 0j
    b = 0 + 0j
    midpoints = []
    while len(points) > 1:
        num = len(points) - 1
        for i in range(0, num):
            a = points[i]
            b = points[i+1]
            midpoints.append(complex(
                a.real + (b.real - a.real) * t,
                a.imag + (b.imag - a.imag) * t,   
            ))

        points = midpoints
        midpoints = []

    return points[0] # Object.assign(points[0], {in: a, out: b});
