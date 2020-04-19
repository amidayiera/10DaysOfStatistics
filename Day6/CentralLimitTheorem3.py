# QUESTION : You have a sample of 100 values from a population with mean of 500 
# and with standard deviation of 80. Compute the interval that covers the middle 95% 
# of the distribution of the sample mean; in other words, compute A and B such that P(A<x<B) = 0.95. 
# Use the value of z = 1.96 . Note that  is the z-score.

# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import sqrt

s = int(input()) #100
mean = int(input()) #500
std = int(input()) #80
interval = float(input()) #.95
z = float(input()) #1.96

print(round(mean - (std / sqrt(s)) * z, 2))
print(round(mean + (std / sqrt(s)) * z, 2))