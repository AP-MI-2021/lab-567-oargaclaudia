from Domain.obiect import creeazaObiect, getId


def adaugaObiect(id, nume, descriere, pret, locatie, lista):
    '''
    Adauga un obiect intr-o lista
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :param lista: lista de obiecte
    :return: o lista continand vechile obiecte si noul obiect
    '''
    obiect=creeazaObiect(id, nume, descriere, pret, locatie)
    return lista + [obiect]


def getById(id, lista):
    '''
    Da elementul din lista cu un id dat
    :param id: string
    :param lista: lista de obiecte
    :return: obiectul cu id-ul dat sau None daca nu exista
    '''
    for obiect in lista:
        if getId(obiect) == id:
            return obiect
    return None

def stergeObiect(id, lista):
    '''
    Sterge obiectul cu id-ul dat dintr-o lista
    :param id: id-ul obiectului care se va sterge
    :param lista: lista de obiecte
    :return: o lista de obiecte fara obiectul cu id-ul dat
    '''

    return [obiect for obiect in lista if getId(obiect)!= id]

def modificaObiect(id, nume, descriere, pret, locatie, lista):
    '''
    Modifica obiectul cu id-ul dat
    :param id: id-ul obiectului
    :param nume: numele obiectului
    :param descriere: descrierea obiectului
    :param pret: pretul obiectului
    :param locatie: locatia obiectului
    :param lista: o lista de obiecte
    :return: lista modificata
    '''
    listaNoua=[]
    for obiect in lista:
        if getId(obiect)==id:
            obiectNou=creeazaObiect(id, nume, descriere, pret, locatie)
            listaNoua.append(obiectNou)
        else:
            listaNoua.append(obiect)
    return listaNoua
