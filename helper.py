#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 14:11:37 2018

@author: ashwin
"""
congurent = []

class coordinate(object):
    """
    coordinate class for easy storing of points
    
    """
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def distance(self,other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx**2 + dy**2)**0.5
    
    def __str__(self):
        return "<%s,%s>"%(self.x, self.y)
    
    def __repr__(self):
        return "<%s,%s>"%(self.x, self.y)
    
class triangle(object):
    """
   class triangle which keeps a record of sides
    """
    
    def __init__(self,p1,p2,p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def __str__(self):
        return "Triangle(%s,%s,%s)"%(self.p1, self.p2, self.p3)
    
    def __repr__(self):
        return "Triangle(%s,%s,%s)"%(self.p1, self.p2, self.p3)
        
    def sides(self):
        s = []
        s.append(self.p1.distance(self.p2))
        s.append(self.p2.distance(self.p3))
        s.append(self.p3.distance(self.p1))
        s.sort()
        return s

def ispossibletriangle(triang):
    """
    This checks given any triangle object as input weather it is a valid triangle or not 
    """
    
    sp = triang.sides()
    if sp[0] < sp[1] + sp[2]:
        return True
    else:
        return False


def cong(t1,t2):
    """
    t1 and t2 are two triangle objects , it appends the result of congurent triangles 
    """
    if t1.sides() == t2.sides():
        congurent.append([t1,t2])