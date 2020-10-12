# De la tastatură se întroduce numărul de rînd al culorii curcubeului. De afişat
#denumirea culorii. Convenim că culoarea roşie are numărul de rînd 1.
#
#rosu oranj galben verde albastru indigo violet
a= int(input("Introduceti nr culorii= "))
if a==1:
    print ('Rosu')
elif a==2:
    print ('Oranj')
elif a==3:
    print ('Galben')
elif a==4:
    print ('Verde')
elif a==5:
    print ('Albastru')
elif a==6:
    print ('Indigo')
elif a==7:
    print ('Violet')
elif a>7:
    print ('Invata culorile')
