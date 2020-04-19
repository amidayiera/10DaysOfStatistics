# QUESTION : The final grades for a Physics exam taken by a large group of students have a mean of 70 and a 
# standard deviation of 10. If we can approximate the distribution of these grades by a normal distribution, 
# what percentage of the students:
# 1. Scored higher than 80 (i.e., have a grade > 80)?
# 2. Passed the test (i.e., have a grade >= 60)?
# 3. Failed the test (i.e., have a grade< 60 )?
# Find and print the answer to each question on a new line, rounded to a scale of 2 decimal places.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

miu, stdev = map(float, input().split())
limit1 = float(input())
limit2 = float(input())

def normal_prob(miu, stdev, x):
    return 0.5 * (1 + math.erf((x-miu)/(stdev * 2**0.5)))    

print( '%.2f' %((1 - normal_prob(miu, stdev, limit1)) *100) )
print( '%.2f' %((1 - normal_prob(miu, stdev, limit2)) *100) )
print( '%.2f' %(normal_prob(miu, stdev, limit2) *100) )
# note: need to output percentage (not probability)

