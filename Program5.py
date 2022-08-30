# The radius of a circle is 30 meters.
# • Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
# • Calculate the circumference of a circle and assign the value to a variable name of
# _circum_of_circle_
# • Take radius as user input and calculate the area

import math

#declaring radius
radius = 30

#calculate area
_area_of_circle = math.pi * radius * radius
print(f"The area of circle with radius 30 is {round(_area_of_circle,2)}")

#circumference of a circle
_circum_of_circle_ = 2 * math.pi * radius
print(f"The circumference of circle with radius 30 is {round(_circum_of_circle_,2)}")

#taking radius as user input
r = float(input("enter radius of your choice:"))
print(f"The area of circle with radius {r} is {round(math.pi * r * r,2)}")