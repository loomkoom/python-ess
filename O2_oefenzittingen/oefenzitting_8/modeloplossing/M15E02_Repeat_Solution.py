def repeat(f,n,x):
    """ 
    A function that applies the function f n times on 
    the argument x and returns the result, for example 
    repeat(f,3,x) is equivalent with f(f(f(x))).
    """
    if n > 1:
    	return repeat(f, n-1, f(x))
    elif n == 1:
    	return f(x)


plus = lambda x,y: repeat(lambda z:z+1,x,y)
assert plus(2,2) == 4

times = lambda x,y: repeat(lambda z:plus(x,z),y,0)
assert times(3,4) == 12

power = lambda x,y: repeat(lambda z:times(x,z),y,1)
assert power(2,10) == 1024

