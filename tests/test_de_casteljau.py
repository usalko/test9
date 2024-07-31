
from unittest import TestCase
from utils import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.path as mpath
import numpy as np


class TestDeCasteljau(TestCase):

    def test_quadratic_arc(self):
        path = [
            Point2D(0.1, 0.1),
            Point2D(0.4, 0.9),
            Point2D(0.3, 0.3),
            Point2D(-0.9, -0.4),
            Point2D(0.1, 0.4),
            Point2D(0.9, 0.1),
        ]
        # Simple checkpoint
        zero_one_point = de_casteljau(path, 0.1)
        self.assertIsNotNone(zero_one_point)

        t = np.arange(0, 1, 0.01)
        def de_casteliau_numpy_ufunc_for_custom_path(t: float) -> complex:
            value = de_casteljau(path, t)
            return complex(value.x0, value.x1)

        # define numpy universal function
        de_casteliau_numpy_ufunc_for_custom_path_ufunc = np.frompyfunc(de_casteliau_numpy_ufunc_for_custom_path, 1, 1)
        curve = de_casteliau_numpy_ufunc_for_custom_path_ufunc(t)
        
        # extract real part 
        x = [ele.real for ele in curve] 
        # extract imaginary part 
        y = [ele.imag for ele in curve] 
        
        # plot the complex numbers 
        plt.scatter(x, y) 
        plt.ylabel('Imaginary') 
        plt.xlabel('Real') 
        # plt.show() 

        plt.savefig('test-output.svg')
