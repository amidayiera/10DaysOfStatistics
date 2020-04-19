# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics

n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

miu_x = sum(X) / n
miu_y = sum(Y) / n

stdev_x = statistics.pstdev(X)
stdev_y = statistics.pstdev(Y)

covariance = sum([(X[i] - miu_x) * (Y[i] -miu_y) for i in range(n)])

pearson_coefficient = covariance / (n * stdev_x * stdev_y)

print(round(pearson_coefficient, 3))
