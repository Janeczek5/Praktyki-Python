import random
import time
gracz = 0
komp = 0
wyborCzlowiek = ""
while(wyborCzlowiek!='0'):
    wyborKomp = random.choice(["orzeł", "reszka"])
    print("Proszę napisać co wybierzasz: (0 gdy koniec, o jak orzeł, r jak reszka) ")
    wyborCzlowiek = input()
    if(wyborCzlowiek=='0'):
        break
   

    if(wyborCzlowiek =='r'):
        if(wyborKomp == "reszka"):
            gracz+=1
    if(wyborCzlowiek =='o'):
        if(wyborKomp == "orzeł"):
            gracz+=1
    if(wyborCzlowiek =='o'):
        if(wyborKomp == "reszka"):
            komp+=1
    if(wyborCzlowiek =='r'):
        if(wyborKomp == "orzeł"):
            komp+=1
    if(wyborCzlowiek != 'r' and wyborCzlowiek !='o' and wyborCzlowiek != '0'):
        print("Podaj poprawną wartość a nie niewiadomo co - ZA KARE MUSISZ ZACZĄĆ GRANIE OD NOWA")
        break

    for i in range(3):
        print("Wybuch za: ", 3 - i)
        time.sleep(1)
    print("BUMMMMMMM - KOMPUTER WYBRAŁ", wyborKomp)
    print("Gracz ma: ", gracz, " punktów, a komputer ma: ", komp, " punktów")
    print("=====================")
 
