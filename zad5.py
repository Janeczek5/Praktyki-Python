L = 9
A = [1,3,5,2,11,4]
Czyjest = False
for i in range(len(A)-1):
    for j in range(len(A)):
        if(i!=j):
            if(A[i] + A[j] == L):
                Czyjest = True
                break
if(Czyjest):
    print("Znaleziono takie pary liczb")
else:
    print("Nie znaleziono takich par liczb")