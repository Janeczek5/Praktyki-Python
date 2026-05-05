ciag = "Ala ma kota"
TablWyraz = []
TablIlosc = []
licznik = 1
for i in ciag:
    if(i != ' '):
        TablWyraz.append(i)
TablWyraz.sort()

for i in range(len(TablWyraz)):
    if(i!= len(TablWyraz)-1):
        if(TablWyraz[i]== TablWyraz[i+1]):
            licznik+=1
        else:
            TablIlosc.append(licznik)
            licznik=1
    else:
        if(TablWyraz[i-1]== TablWyraz[i]):
            licznik+=1
        else:
            TablIlosc.append(licznik)
            licznik=1
niepowtarzam = list(set(TablWyraz))
niepowtarzam.sort()


iloscLiter =0
spacje=0
for i in ciag:
    if(i==' '):
        spacje +=1
ilosc = len(ciag) -spacje
print("Ilość wyrazów: ", spacje+1)
print("Ilość liter: ", ilosc)

for i in range(len(niepowtarzam)):
    print("Litera: ", niepowtarzam[i], ", powtórzyła się: ", TablIlosc[i] )
