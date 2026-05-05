Szukane = 57
wynik = 0
tablcala = []
for i in range(1,1001):
    tablcala.append(i)



tablcala.sort()
tablPodstawowa = tablcala.copy()
tablmala = []

rob = True

while(rob):
    print(tablcala)
    polowa = round(len(tablcala) /2)
    if(tablcala[0]==Szukane):
        print("Liczba została znaleziona")
        wynik = tablcala[0]
        break
    if(Szukane < tablcala[polowa]):
        tablcala = tablcala[:polowa]
    else:
        tablcala = tablcala[polowa:]

inde = tablPodstawowa.index(wynik)

print("Jest to liczba: ", wynik, " na indeksie: ", inde)
    


    