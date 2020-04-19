# Enter your code here. Read input from STDIN. Print output to STDOUT
def mean(x):
    return sum(x)/len(x)

def lsr(x,y):
    b = sum([(x[i]-mean(x))*(y[i]-mean(y)) for i in range(len(x))])/sum([(j-mean(x))**2 for j in x])
    a = mean(y)-(b*mean(x))
    return a+(b*80)

x = []
y = []
for i in range(5):
    a,b = list(map(int, input().split()))
    x.append(a)
    y.append(b)

print(round(lsr(x,y),3))