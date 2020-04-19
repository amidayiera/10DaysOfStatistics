# # Enter your code here. Read input from STDIN. Print output to STDOUT
# QUESTION: A manufacturer of metal pistons finds that, on average,  of the pistons they 
# manufacture are rejected because they are incorrectly sized.
#  What is the probability that a batch of  pistons will contain:
# 1. No more than  rejects?
# 2. At least  rejects?

import math
def binomial_prob(n, p, x):
    b = (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))
    return b

n = 10
p = 0.12
print(round(sum([binomial_prob(n, p, x) for x in range(3)]), 3))  
print(round(sum([binomial_prob(n, p, x) for x in range(2, 11)]), 3))  