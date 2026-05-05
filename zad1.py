tabl= []
for i in range(1, 101):
    tabl.append(i)
for i in range(100):
    if(tabl[i]%5==0 and tabl[i]%3==0):
        tabl[i] = "FizzBuzz"
    elif(tabl[i]%3==0):
        tabl[i] = "Fizz"
    elif(tabl[i]%5==0):
        tabl[i] = "Buzz"
    
   
for i in tabl:
    print(i)
    