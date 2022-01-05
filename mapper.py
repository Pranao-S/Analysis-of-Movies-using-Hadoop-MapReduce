import sys

x_r=2
x_c=3
y_r=3
y_c=2

i=0
for line in sys.stdin:
    el=list(map(int,line.split()))
    if(i<x_r):
            for j in range(len(list(el))):
                for k in range(y_c): print ("{0}\t{1}\t{2}\t{3}".format(i, k, j, el[j]))
    else:
            for j in range(len(list(el))):         
                for k in range(x_r): print ("{0}\t{1}\t{2}\t{3}".format(k, j, i-x_r,el[j]))             
    i=i+1
