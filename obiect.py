def creeazaObiect(id, nume, descriere, pret, locatie):
    '''
    Creeaza o lista ce reprezinta un obiect
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :return: o lista ce contine un obiect
    '''
    lista=[id,nume,descriere,pret,locatie]
    return lista
def getId(lista):
    '''
    Da id-ul unui obiect
    :param obiect: lista ce retine un obiect
    :return: id-ul obiectului
    '''
    return lista[0]
def getNume(lista):
    '''
    Da numele unui obiect
    :param obiect: lista ce retine un obiect
    :return: numele obiectului
    '''
    return lista[1]
def getDescriere(lista):
    '''
    Da descrierea unui obiect
    :param obiect: lista ce retine un obiect
    :return: descrierea obiectului
    '''
    return lista[2]
def getPret(lista):
    '''
    Da pretul unui obiect
    :param obiect: lista ce retine un obiect
    :return: pretul obiectului
    '''
    return lista[3]
def getLocatie(lista):
    '''
    Da locatia unui obiect
    :param obiect: lista ce retine un obiect
    :return: locatia obiectului
    '''
    return lista[4]
def toString(obiect):
    return "Id: {}, Nume: {}, Descriere: {}, Pret: {}, Locatie: {}".format(
        getId(obiect),
        getNume(obiect),
        getDescriere(obiect),
        getPret(obiect),
        getLocatie(obiect)
    )