#premenne a zoznamy
nulky = 0
jednotky = 0
pocet = 0
listik = []

#otvorenie vstupneho suboru
subor = open("kompresia_obrazka_vstup.txt","r")

#precitanie prveho riadku
prvy_riadok = subor.readline()
riadocek = prvy_riadok.split()

#vypisanie sirky, vysky a poctu bodov
print('Šírka obrázka:',riadocek[0])
print('Výška obrázka:',riadocek[1])
print('Počet bodov:',int(riadocek[0])*int(riadocek[1]))

def spracuj_riadok(): #funkcia na kompresiu hodnot
    #globalne premenne
    global prvy_riadok
    global nulky, jednotky
    global pocet

    #otvorenie vstupneho suboru
    subor1 = open("kompresia_obrazka_vystup.txt","w")

    #zapisanie prveho riadku do vystupneho suboru
    subor1.write(prvy_riadok)
    
    #podmienky na zapisanie udajov do vystupneho suboru
    for riadok in subor:
        #pokial riadok zacina 0, tak sa zapise
        if riadok[1] != "0":
            subor1.write('0 ')

        #zapisanie poctu 0/1 do zoznamu    
        for cislo in riadok:
            pocet += 1
            #ak je cislo 1
            if cislo == "1":
                if nulky != 0:
                    listik.append(nulky)
                nulky = 0
                jednotky += 1
            #ak je cislo 0
            elif cislo == "0":
                if jednotky != 0:
                    listik.append(jednotky)
                jednotky = 0
                nulky += 1
            #poistka pre spravne fungovanie, ked ide o posledne cislo
            if pocet == 20:
                if nulky != 0:
                    listik.append(nulky)
                if jednotky != 0:
                    listik.append(jednotky)

        #zapisanie hodnot zo zoznamu do vystupneho suboru
        for i in listik:
            subor1.write(str(i)+' ')
        subor1.write('\n')

        #vynulovanie hodnot
        pocet = 0
        nulky = 0
        jednotky = 0
        listik.clear()

    #zatvorenie vystupneho suboru            
    subor1.close()  

#vyvolanie funkcie     
spracuj_riadok()

#zatvorenie vstupneho suboru
subor.close()

