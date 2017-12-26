from vector import Vector
from line import Line
from plane import Plane
from decimal import Decimal, getcontext
from util import Util
from linear_system import LinearSystem

print("-----Vectors------")
print('#1')
v = Vector([8.462, 7.893, -8.187])
w = Vector([6.984, -5.975, 4.778])
print(v.cross_product(w))

v = Vector([-8.987, -9.838, 5.031])
w = Vector([-4.268, -1.861, -8.866])
print(v.area_of_parallelogram_with(w))

v = Vector([1.5, 9.547, 3.691])
w = Vector([-6.007, 0.124, 5.772])
print(v.area_of_triangle(w))
print v.normalization()
print v.angle(w)

print("-----Lines------")
print("Quiz #1")
line1 = Line(Vector([4.046, 2.836]), 1.21)
line2 = Line(Vector([10.115, 7.09]), 3.025)
print "First Line:", line1.intersection(line2)

line1 = Line(Vector([7.204, 3.182]), 8.68)
line2 = Line(Vector([8.172, 4.114]), 9.883)
print "Second Line:", line1.intersection(line2)

line1 = Line(Vector([1.182, 5.562]), 6.744)
line2 = Line(Vector([1.773, 8.343]), 9.525)
print("Third Line:", line1.intersection(line2))

print("-----Planes-----")
print("Quiz #2")


def check_planes(plane1, plane2, current_pair_first_plane=1):
    result = "Regarding {0} and {1} planes. \n Are parallel: {2} \n Are same: {3}".format(
        Util.to_ordinal(current_pair_first_plane),
        Util.to_ordinal(current_pair_first_plane + 1),
        plane1.is_parallel_to(plane2),
        plane1 == plane2
    )
    print(result)


check_planes(
    Plane(Vector([-0.412, 3.806, 0.728]), -3.46),
    Plane(Vector([1.03, -9.515, -1.82]), 8.65)
)

check_planes(
    Plane(Vector([2.611, 5.528, 0.283]), 4.6),
    Plane(Vector([7.715, 8.306, 5.342]), 3.76),
    3
)

check_planes(
    Plane(Vector([-7.926, 8.625, -7.212]), -7.952),
    Plane(Vector([-2.642, 2.875, -2.404]), -2.443),
    5
)