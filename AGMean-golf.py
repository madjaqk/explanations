"""
Program to calculate the arithmetic-geometric mean, inspired by this Stack Exchange challenge: 
http://codegolf.stackexchange.com/questions/66068/agm-series-hole-1-calculate-the-arithmetic-geometric-mean

The Arithmetic–Geometric Mean of two numbers is defined as the number that repeatedly taking the arithmetic and geometric means converges to. 

The golfed version, which incorporates feedback from user mathmandan, is:
f=lambda a,b,n:f((a+b)/2,(a*b)**.5,n-1)if n else(a,b)
"""

def AGMean(a,b,n):
	for count in range(0,n):
		a,b = (a+b)/2, (a+b)**.5 # Sets a to the arithmetic mean and b to the geometric mean
	return a,b