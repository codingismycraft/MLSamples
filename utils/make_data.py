"""Creates the testing data that will be used from the M/L models."""

import collections

import math
import random

MIN_X = 0.1
MAX_X = 100

MIN_Y = 0.1
MAX_Y = 100


def make_distance_data(num_rows_to_create):
    """Creates the testing data for the distance model.

    :param int num_rows_to_create: The number of rows to create.
    """
    Point = collections.namedtuple('Point', ['x', 'y'])

    def get_distance():
        return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

    def make_point():
        return Point(random.uniform(MIN_X, MAX_X), random.uniform(MIN_Y, MAX_Y))

    with open("/vagrant/data/my_data.csv", "w") as f:
        f.write(f'v1,v2,v3,v4,target\n')
        for _ in range(num_rows_to_create):
            p1 = make_point()
            p2 = make_point()
            f.write(f'{p1.x},{p1.y},{p2.x},{p2.y},{get_distance()}\n')


if __name__ == '__main__':
    make_distance_data(num_rows_to_create=10000)
