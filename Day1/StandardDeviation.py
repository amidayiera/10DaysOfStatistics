# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics

size = int(input())
elements = list(map(int, input().split()))

print(round(statistics.pstdev(elements), 1))
