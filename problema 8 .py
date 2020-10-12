#Se introduc de la tastatură trei cifre. Afişaţi pe aceeaşi linie 5 numere formate cu
#aceste cifre luate o singură dată. Exemplu : date de intrare : 3 4 2 Date de ieşire : 324
#342 243 234 432.
a= int(input("Introduceti prima cifra = "))
b= int(input("Introduceti al doua cifra = "))
c= int(input("Introduceti treia cifra = "))
nr1=(a*100)+(b*10)+c
nr2=(b*100)+(a*10)+c
nr3=(c*100)+(b*10)+a
nr4=(a*100)+(c*10)+b
nr5=(c*100)+(a*10)+b
print (nr1)
print (nr2)
print (nr3)
print (nr4)
print (nr5)
