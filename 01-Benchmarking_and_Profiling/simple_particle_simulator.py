#!python3

"""
NAME:       Aakash Sudhakar
DATE:       Sunday, June 3, 2018
DESC:       Program containing basic particle simulator. 
            Purpose is to achieve rudimentary benchmarking/profiling.
RATING:     ?/5
"""

class Particle:
    """ Generic particle class with object position and velocity. """
    def __init__(self, x, y, angular_velocity):
        self.x = x
        self.y = y
        self.angular_velocity = angular_velocity

