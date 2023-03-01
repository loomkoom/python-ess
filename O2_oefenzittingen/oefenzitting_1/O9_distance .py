"""
Calculating the distance between two points in a two-dimensional area.
More information can be found here: https://en.wikipedia.org/wiki/Euclidean_distance#Two_dimensions

The program should read in the x and y coordinates of the two points separately, and write out a complete answer string, for example
  
  Enter the x-value for the first point: 3.4
  Enter the y-value for the first point: 3.5
  Enter the x-value for the second point: 7.8
  Enter the y-value for the second point: 2
  The distance between ( 3.4 , 3.5 ) and ( 7.8 , 2 ) is 4.64865571967

Examples of distance:
 x1     y1     x2     y2     d 
 0      0      0      0      0
 10     0      0      10     14.1421356237
 3      4      0      0      5
 3      0      4      0      1.0
 -20.7  13.4   45.2   57.2   79.1280607623
"""

from math import *

x1 = float(input('Enter the x-value for the first point: '))
y1 = float(input('Enter the y-value for the first point: '))
x2 = float(input('Enter the x-value for the second point: '))
y2 = float(input('Enter the y-value for the second point: '))

distance = sqrt((x1-x2)**2+(y1-y2)**2)



print('The distance between','(',end=' ')
print(x1,y1,sep=' , ',end=' ')
print(')','and','(',end=' ')
print(x2,y2,sep=' , ',end=' ')
print(')','is: ',distance )


