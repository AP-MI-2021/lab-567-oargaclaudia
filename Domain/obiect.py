def creeazaObiect(id, nume, descriere, pret, locatie):
    '''
    Creeaza un dictionar ce reprezinta un obiect
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :return: un dictionar ce contine un obiect
    '''
    return {
        "id": id,
        "nume": nume,
        "descriere": descriere,
        "pret": pret,
        "locatie": locatie
    }
def getId(obiect):
    '''
    Da id-ul unui obiect
    :param obiect: dictionar ce retine un obiect
    :return: id-ul obiectului
    '''
    return obiect["id"]
def getNume(obiect):
    '''
    Da numele unui obiect
    :param obiect: dictionar ce retine un obiect
    :return: numele obiectului
    '''
    return obiect["nume"]
def getDescriere(obiect):
    '''
    Da descrierea unui obiect
    :param obiect: dictionar ce retine un obiect
    :return: descrierea obiectului
    '''
    return obiect["descriere"]
def getPret(obiect):
    '''
    Da pretul unui obiect
    :param obiect: dictionar ce retine un obiect
    :return: pretul obiectului
    '''
    return obiect["pret"]
def getLocatie(obiect):
    '''
    Da locatia unui obiect
    :param obiect: dictionar ce retine un obiect
    :return: locatia obiectului
    '''
    return obiect["locatie"]
def toString(obiect):
    return "Id: {}, Nume: {}, Descriere: {}, Pret: {}, Locatie: {}".format(
        getId(obiect),
        getNume(obiect),
        getDescriere(obiect),
        getPret(obiect),
        getLocatie(obiect)
    )
