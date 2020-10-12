#Un brăduţ este împodobit cu globuleţe albe, roşii şi albastre. Numărul globuleţelor
#albe se citeşte de la tastatură. Câte globuleţe are brăduţul, ştiind că numărul de
#globuleţe roşii este cu 3 mai mare decât numărul de globuleţe albe, iar globuleţele
#albastre sunt cu 2 mai puţine decât totalul celor albe şi roşii. Exemplu: Date de intrare:
#12 Date de ieşire: 52.
albe= int(input("Introduceti nr de globulete albe= "))
rosii=albe+3
albastre=(rosii+albe)-2
total=rosii+albe+albastre
print ('Bradul are = ',total,' globulete')

