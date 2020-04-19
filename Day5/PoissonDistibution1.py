# Enter your code here. Read input from STDIN. Print output to STDOUT
# QUESTION : A random variable, X , follows Poisson distribution with mean of 2.5. Find the probability with which the random variable X is equal to 5.

from math import factorial, exp

x = 5
miu = 2.5
poisson_prob = ((miu**x) * exp(-miu)) / factorial(x)

print("%.3f" %poisson_prob)

