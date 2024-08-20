
from unittest import TestCase

import matplotlib.patches as mpatches
import matplotlib.path as mpath
import matplotlib.pyplot as plt
import numpy as np

from utils import *


class TestDeCasteljau(TestCase):

    def draw_path(self, path, file_name):
        t = np.arange(0, 1, 0.01)

        def de_casteliau_numpy_ufunc_for_custom_path(t: float) -> complex:
            return de_casteljau_complex(path, t)

        # define numpy universal function
        de_casteliau_numpy_ufunc_for_custom_path_ufunc = np.frompyfunc(
            de_casteliau_numpy_ufunc_for_custom_path, 1, 1)
        curve = de_casteliau_numpy_ufunc_for_custom_path_ufunc(t)

        # extract real part
        x = [ele.real for ele in curve]
        # extract imaginary part
        y = [ele.imag for ele in curve]

        # Reset previous graphic
        plt.clf()
        
        # plot the complex numbers
        plt.scatter(x, y)
        # draw red points
        point_number = 1
        for point in path:
            plt.plot(point.real, point.imag, 'ro')
            plt.text(point.real + 0.02, point.imag + 0.02, point_number,
                     color='red',
                     backgroundcolor='#ffffff'
                     ).set_bbox({
                         'alpha': 0.85,
                         'facecolor': '#ffffff',
                         'edgecolor': '#f0f0f0',
                         'boxstyle': 'round,pad=0,rounding_size=0.2',
                     })
            point_number += 1

        # Axis labels
        plt.ylabel('Imaginary')
        plt.xlabel('Real')
        # plt.show()

        plt.savefig(file_name)

    def test_1(self):
        path = [
            complex(0.1, 0.1),
            complex(0.4, 0.9),
            complex(0.3, 0.3),
            complex(-0.9, -0.4),
            complex(0.1, 0.4),
        ]
        # Simple checkpoint
        zero_one_point = de_casteljau_complex(path, 0.1)
        self.assertIsNotNone(zero_one_point)

        return self.draw_path(path, 'test-output-1.svg')

    def test_2(self):
        path = [
            complex(0.1, 0.1),
            complex(0.3, 0.3),
            complex(-0.9, -0.4),
            complex(0.1, 0.4),
            complex(-0.9, -0.9),
            complex(-0.4, -0.9),
        ]
        # Simple checkpoint
        zero_one_point = de_casteljau_complex(path, 0.1)
        self.assertIsNotNone(zero_one_point)

        return self.draw_path(path, 'test-output-2.svg')
