# Enter your code here. Read input from STDIN. Print output to STDOUT
size = int(input())
elements = list(map(int, input().split()))
weighted = list(map(int, input().split()))

sum = 0
weights = 0
for i in range(size):
    sum += elements[i] * weighted[i]
    weights += weighted[i]
    weightedMean = sum / weights

print(round((weightedMean),1))

