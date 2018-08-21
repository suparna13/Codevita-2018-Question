#!/usr/bin/python3
import math

v1=int(input())
r1=int(input())
v2=int(input())
r2=int(input())
time=int(input())
angle_A=(time*v1)
angle_B=(time*v2)
if angle_A > angle_B:
    final_angle=angle_A-angle_B
else:
    final_angle=angle_B-angle_A
    
rad=math.radians(final_angle)
x=math.cos(rad)
Third_side=(r1*r1)+(r2*r2)-(2*r1*r2*x)
side=Third_side ** 0.5
print("%.2f" % round(side,2))

