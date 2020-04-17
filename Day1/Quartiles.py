# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics 

length = int(input())
elements = sorted(list(map(int, input().split())))

print(int(statistics.median(elements[:length//2])))
print(int(statistics.median(elements)))
print(int(statistics.median(elements[(length+1)//2:])))
