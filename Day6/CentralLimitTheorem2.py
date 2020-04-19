# QUESTION : The number of tickets purchased by each student for the University X vs. University Y 
# football game follows a distribution that has a mean of 24 and a standard deviation of 2.0.
# A few hours before the game starts, 100 eager students line up to purchase last-minute tickets. 
# If there are only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

x = int(input()) #250
n = int(input()) #100
mu = float(input()) #2.4
sigma = float(input()) #2.0

mu_sum = n * mu 
sigma_sum = math.sqrt(n) * sigma

def cdf(x, mu, sigma):
    Z = (x - mu)/sigma
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

print(round(cdf(x, mu_sum, sigma_sum), 4))