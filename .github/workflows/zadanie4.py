lista =[2,0,5,1,6,3]

for j in range(len(lista)):
    for i in range(len(lista) - 1):
        if(lista[i] > lista[i+1]):
                lista[i], lista[i+1] = lista[i+1], lista[i];
                print(lista);