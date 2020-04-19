# Enter your code here. Read input from STDIN. Print output to STDOUT
# QUESTION : The probability that a machine produces a defective product is 1/3. 
# What is the probability that the first defect is found during the fifth inspection?

n = 5
p = 1/3
q = 2/3

def geometric_distribution(p, n):
    g = (1-p)**(n-1) * p
    return g

print(round(geometric_distribution(p, n),3))