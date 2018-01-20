#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:34:44 2018

@author: ashwin

keep a check on negative coordinates :/
"""
import itertools 
import helper as hl

points = []
triangles_all = []
triangles_possible = []
triangle_pairs = []
        
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

