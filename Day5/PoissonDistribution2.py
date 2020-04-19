# QUESTION : The manager of a industrial plant is planning to buy a machine of either type A or type B. 
# For each day’s operation:
# - The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88. 
#   The daily cost of operating A is C = 160 + 40X^2.
# - The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55. 
#   The daily cost of operating B is C = 128 + 40Y^2
# Assume that the repairs take a negligible amount of time and the machines are maintained nightly 
# to ensure that they operate like new at the start of each day. Find and print the expected daily cost for each machine.


# Enter your code here. Read input from STDIN. Print output to STDOUT
mean_A = 0.88
mean_B = 1.55

cost_A = 160 + 40 * (mean_A + pow(mean_A, 2))
cost_B = 128 + 40 * (mean_B + pow(mean_B, 2))

print("%.3f" %cost_A)
print("%.3f" %cost_B)