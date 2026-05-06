import time;
import random;


wybor = input("Wybierz orła, lub reszkę: ")
print("\n")
print(wybor)


nieWybrano = True
while nieWybrano:
    if wybor == "orzeł" :
        print("Wybrano: Orzeł")
        nieWybrano = False
    elif wybor == "reszka":
        print("Wybrano: Reszka")
        nieWybrano = False
    else:
        print("Wpisz poprawną wartość")
        wybor = input("Wybierz orła, lub reszkę (o/r)")


for i in range(3):
    print(3 -i)
    time.sleep(1)

wybor2 = random.choice(["orzeł", "reszka"])
print(wybor2)

if wybor == wybor2:
    print("Wygrałeś")
else:
    print("Nie wygrałeś")
