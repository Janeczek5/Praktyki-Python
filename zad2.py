lista = [1,4,-4,7]
maxi = lista[0]
mini = lista[0]
for i in lista:
    if i > maxi:
        maxi = i
    elif i < mini:
        mini = i
print("Minimum: " , mini)
print("Maximum: " , maxi)
