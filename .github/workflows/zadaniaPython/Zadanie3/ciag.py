ciag = "Ala ma kota";

tempLista = []

temp1 = ciag.split(" ");
temp2 = ciag.replace(" ", "").lower()

n = 0
for i in ciag:
    if i != ' ':
        n = n + 1

print(len(temp1))
print(n)      

for i in temp2:
    if not tempLista.__contains__(i):
        temp = temp2.split(i)
        print(i, len(temp)-1)
    tempLista.append(i)
    
    




