#Date trei numere, să se calculeze toate sumele posibile de câte două numere. Afişarea
#să cuprindă şi termenii sumei, nu numai valoarea ei. Exemplu: Date de intrare : 2 13
# 4 Date de ieşire: 2+13 =15 2+4=6 13+4=17. 

a= int(input("Introduceti primul nr = "))
b= int(input("Introduceti al doilea nr = "))
c= int(input("Introduceti treilea nr = "))
suma1=a+b
suma2=b+c
suma3=a+c
print (a,' + ',b,' = ',suma1)
print (b,' + ',c,' = ',suma2)
print (c,' + ',a,' = ',suma3)
