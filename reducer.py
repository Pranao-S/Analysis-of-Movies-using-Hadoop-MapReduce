#!/usr/bin/env python3
import sys

x1_r=2
x1_c=3
y_r=3
y_c=2

matrix=[]
for row in range(x1_r):
    r=[]
    for col in range(y_c):
        s=0
        for el in range(x1_c):
            mul=1
            for num in range(2):
                line=sys.stdin.readline()
                y=list(map(int,line.split('\t')))[-1]
                mul*=y
            s+=mul
        r.append(s)
    matrix.append(r)  
print('\n'.join([str(x) for x in matrix]))