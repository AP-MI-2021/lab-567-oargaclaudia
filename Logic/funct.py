from Domain.obiect import getLocatie, creeazaObiect, getId, getNume, getDescriere, getPret

def mutareObiecte(substringLocatieVeche, lista, locatieNoua):
    '''

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