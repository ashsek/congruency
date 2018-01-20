#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:34:44 2018

@author: ashwin

keep a check on negative coordinates :/
"""
import itertools 
import helper as hl
import matplotlib.pyplot as plt

points = []
triangles_all = []
triangles_possible = []
triangle_pairs = []
plot = []

# it takes the input from the user as points and store them as coordinate obejcts 
for i in range(int(input())):
    a,b = list(map(int,input().split()))
    points.append(hl.coordinate(a,b))

triangles_all.extend(itertools.combinations(points, 3))

for points in triangles_all:
    """gives a list of all possible triangles"""
    pl1 = points[0]
    pl2 = points[1]
    pl3 = points[2]
    to = hl.triangle(pl1,pl2,pl3)
    if hl.ispossibletriangle(to):
        triangles_possible.append(to)

#gives combination of all possible triangles  
triangle_pairs.extend(itertools.combinations(triangles_possible, 2))

#checks for congurency of triangles 
for m in triangle_pairs:
    tq1 = m[0]
    tq2 = m[1]
    hl.cong(tq1,tq2)
    
print('Congurent Triangles are',hl.congurent)

#[[1,1], [2,1], [2,2], [1,2]]
for u in hl.congurent:
    a0 = [[u[0].p1.x,u[0].p1.y],[u[0].p2.x,u[0].p2.y],[u[0].p3.x,u[0].p3.y]]
    a1 = [[u[1].p1.x,u[1].p1.y],[u[1].p2.x,u[1].p2.y],[u[1].p3.x,u[1].p3.y]]
    if a0 not in plot:
        plot.append(a0)
    if a1 not in plot:
        plot.append(a1)
    break

print('-----------',plot)
    