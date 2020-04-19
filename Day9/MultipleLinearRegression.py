import numpy as np 

X = []
Y = []

m,n = list(map(int, input().split()))

for _ in range(n):
    row = list(map(float, input().split()))
    X.append([1,*row[0:-1]])
    Y.append([row[-1]])


# b = inverse(transpose(x)x)*(transpose(x)*y)
X = np.matrix(X)
Y = np.matrix(Y)

B = ((X.getT()*X).getI())*(X.getT()*Y)

for _ in range(int(input())):
    x = list(map(float, input().split()))
    x = np.matrix([1, *x])
    print(float(x*B)) 