#Programm kontrollib, kas etteantud failis on korrektne lahendus
#Mittekorrektse lahenduse korral ütleb programm, millises veerus, reas või 3x3 ruudus probleem esineb
import sys

def loe_andmed(failinimi):
    tabel = []
    with open(failinimi, encoding='UTF-8-sig') as f:
        for rida in f:
            rida = rida.split()
            if len(rida) == 9:
                tabel.append(rida)
            else:
                print('Sudoku lahendamine on pooleli!')
                return False
        return tabel

def veerg_on_korras(andmed_tabelina, veeru_indeks):
    väärtus = rida[veeru_indeks]
    if väärtus in uus:
        return False
    else:
        uus.append(väärtus)
    return True

def rida_on_korras(andmed_tabelina, rea_indeks):
    for el in andmed_tabelina[rea_indeks]:
        if el in uus:
            return False
        else:
            uus.append(el)
    return True

#andmete lugemine failist kahemõõtmelisse järjendisse
failinimi = sys.argv[1]
andmed_tabelina = loe_andmed(failinimi)
lahendus_on_korras = andmed_tabelina

#kontrollimise alustamine
if lahendus_on_korras:
    vead = []
    #kõikide veergude kontrollimine
    for i in range(9):
        uus = []
        for rida in andmed_tabelina:
            if not veerg_on_korras(andmed_tabelina, i):
                lahendus_on_korras = False
                vead.append(str(i + 1) + '. veerg.')
            else:
                veerud_on_korras = True

    #kõikide ridade kontrollimine
    for i in range(9):
        uus = []
        if not rida_on_korras(andmed_tabelina, i):
            lahendus_on_korras = False
            vead.append(str(i + 1) + '. rida.')
        else:
            read_on_korras = True

    #kõikide 3x3 ruutude kontrollimine
    ruutude_järjend = []
    ruudu_rea_algus = 0
    ruudu_rea_lõpp = 3
    ruudu_veeru_algus = 0
    ruudu_veeru_lõpp = 3
    numbreid = 0
    for i in range(9): 
        ruut = set()
        for rea_indeks in range(ruudu_rea_algus, ruudu_rea_lõpp):
            if ruudu_veeru_lõpp > 9: #Sain selleks osas mõtteid (kaasõpilaselt) Marten Jaagolt.
                ruudu_veeru_algus = 0
                ruudu_veeru_lõpp = 3
            for veeru_indeks in range(ruudu_veeru_algus, ruudu_veeru_lõpp):
                ruut.add(andmed_tabelina[rea_indeks][veeru_indeks])
        if len(ruut) != 9:
            lahendus_on_korras = False
            vead.append(str(i + 1) + '. ruut.')
        ruutude_järjend.append(ruut)
        ruudu_veeru_algus += 3
        ruudu_veeru_lõpp += 3
        
        if len(ruutude_järjend) % 3 == 0:
            ruudu_rea_algus += 3
            ruudu_rea_lõpp += 3

    if lahendus_on_korras:
        print('OK')
    else:
        print('Viga' + '\n''Programm tuvastas probleemi järgnevates asukohtades: ')
        for viga in vead:
            print(viga)
