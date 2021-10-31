from Domain.obiect import getLocatie, creeazaObiect, getId, getNume, getDescriere, getPret

def mutareObiecte(substringLocatieVeche, lista, locatieNoua):
    '''
    Mutarea tuturor obiectelor dintr-o locație în alta.
    :param substringLocatie: stringul dupa care se cauta locatia
    :param lista: lista de obiecte
    :return: lista in care obiectele care apartin de locatia data sunt mutate in alta locatie
    '''

    listaNoua=[]
    for obiect in lista:
        if substringLocatieVeche==getLocatie(obiect):
            obiectNou=creeazaObiect(
                getId(obiect),
                getNume(obiect),
                getDescriere(obiect),
                getPret(obiect),
                getLocatie(obiect).replace(getLocatie(obiect), locatieNoua)
            )
            listaNoua.append(obiectNou)
        else:
            listaNoua.append(obiect)
    return listaNoua

def concatenare(text, lista, pret):
    '''
    Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită
    :param text: stringul care trebuie adaugat la descrierile obiectelor cu pretul mai mare decat o valoare citita
    :param lista: lista de obiecte
    :param pret: valoarea dupa care comparam pretul fiecarui obiect pt a verifica daca ii modificam descrierea
    :return: o lista noua in care toate descrierile obiectelor cu pretul mai mare decat valoarea data au fost modificate, concatenandu-se un string
    '''
    listaNoua=[]
    for obiect in lista:
        if getPret(obiect)>pret:
            obiectNou=creeazaObiect(
                getId(obiect),
                getNume(obiect),
                getDescriere(obiect) + str(text),
                getPret(obiect),
                getLocatie(obiect)
             )
            listaNoua.append(obiectNou)
        else:
            listaNoua.append(obiect)
    return listaNoua


def PretMaximLocatie(lista):
    '''
    Determinarea celui mai mare preț pentru fiecare locație
    :param lista: lista de obiecte
    :return: un dictionar cu cel mai mare pret pentru fiecare locatie
    '''
    rezultat={}
    for obiect in lista:
        locatie=getLocatie(obiect)
        if locatie in rezultat:
            if getPret(obiect)>rezultat[locatie]:
                rezultat[locatie]=getPret(obiect)
        else:
            rezultat[locatie]=getPret(obiect)
    return rezultat

def OrdonareDupaPret(lista):
    '''
    Ordonarea obiectelor crescător după prețul de achiziție.
    :param lista: lista de obiecte
    :return: Obiectele ordonate crescator dupa pretul de achizitie
    '''
    return sorted(lista, key=lambda obiect: getPret(obiect))

def sumaPreturilor(lista):
    '''
    Afișarea sumelor prețurilor pentru fiecare locație.
    :param lista: lista de obiecte
    :return: suma preturilor pentru fiecare locatie
    '''
    rezultat={}
    for obiect in lista:
            locatie=getLocatie(obiect)
            if locatie in rezultat:
                rezultat[locatie]=rezultat[locatie]+getPret(obiect)
            else:
                rezultat[locatie]=getPret(obiect)
    return rezultat

