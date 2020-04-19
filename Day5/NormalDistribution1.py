# QUESTION : In a certain plant, the time taken to assemble a car is a random variable, X, 
# having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours. 
# What is the probability that a car can be assembled at this plant in:
# 1. Less than 19.5 hours?
# 2. Between 20 and 22 hours?

# INPUT FORMAT:
# eg: There are  lines of input (shown below):
# 20 2
# 19.5
# 20 22
# -The first line contains 2 space-separated values denoting the respective mean and standard deviation for X. 
# -The second line contains the number associated with question 1. 
# -The third line contains 2 space-separated values describing the respective lower and upper range boundaries for question 2.

# Enter your code here. Read input from STDIN. Print output to STDOUT

# cumulative probability formula : https://www.hackerrank.com/challenges/s10-normal-distribution-1/tutorial

#  X ~ N( miu, std**2)
# mean = miu
miu = 20
stdev = 2

# miu, stdev = map(int, input().split())

import math
def normal_prob(miu, stdev, x):
    return 0.5 * (1 + math.erf((x-miu)/(stdev * 2**0.5)))

# less than 19.5 hrs
print( '%.3f' %normal_prob(miu, stdev, 19.5) )

# between 20 and 22 hrs
print( '%.3f' %(normal_prob(miu, stdev, 22) - normal_prob(miu, stdev, 20)) )
