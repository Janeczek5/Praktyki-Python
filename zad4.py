A = [2,0,5,1,6,3]

for i in range(len(A)-1):
    for j in range(len(A)-1):
        if(A[j] > A[j+1]):
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp
print(A)