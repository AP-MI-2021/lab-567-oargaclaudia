from Domain.obiect import toString
from Logic.CRUD import adaugaObiect, stergeObiect, modificaObiect
from Logic.funct import mutareObiecte, concatenare, PretMaximLocatie, OrdonareDupaPret,sumaPreturilor


def printMenu():
    print("1. Adaugare obiect ")
    print("2. Stergere obiect ")
    print("3. Modificare obiect ")
    print("4. Mutati obiectele dintr-o locatie in alta ")
    print("5. Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.")
    print("6. Determinarea celui mai mare preț pentru fiecare locație")
    print("7. Ordonarea obiectelor crescator dupa pretul de achizitie ")
    print("8. Afișarea sumelor prețurilor pentru fiecare locație.")
    print("a. Afisare obiect ")
    print("X. Iesire")


def uiAdaugaObiect(lista):
    try:
        id=input("Dati id-ul ")
        nume=input("Dati numele ")
        descriere=input("Dati descrierea ")
        pret=float(input("Dati pretul "))
        locatie=input("Dati locatia ")

        return adaugaObiect(id, nume, descriere, pret, locatie, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergeObiect(lista):
    try:
        id = input("Dati id-ul obiectului pe care vreti sa il stergeti ")
        return stergeObiect(id,lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificaObiect(lista):
    try:
        id = input("Dati id-ul obiectului de modificat ")
        nume = input("Dati noul nume ")
        descriere = input("Dati noua descriere ")
        pret = float(input("Dati noul pret "))
        locatie = input("Dati noua locatie ")
        return modificaObiect(id, nume, descriere, pret, locatie, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiMutaObiecte(lista):
    substringLocatie = input("Dati locatia din care vreti sa mutati obiectele ")
    substringLocatieNoua = input("Dati locatia in care vreti sa mutati obiectele: ")
    return mutareObiecte(substringLocatie, lista, substringLocatieNoua)


def showAll(lista):
    for obiect in lista:
        print(toString(obiect))


def uiConcatenare(lista):
    try:
        substring=input("Dati stringul de la tastatura: ")
        pret=float(input("Dati pretul: "))
        return concatenare(substring,lista,pret)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiLocatie(lista):
    rezultat=PretMaximLocatie(lista)
    for locatie in rezultat:
        print("Locatia {} are pretul maxim {}".format(locatie, rezultat[locatie]))


def uiOrdoneaza(lista):
    showAll(OrdonareDupaPret(lista))


def uiSumaPreturilor(lista):
    rezultat = sumaPreturilor(lista)
    for locatie in rezultat:
        print("Locatia {} are suma preturilor {}".format(locatie, rezultat[locatie]))


def runMenu(lista):
    while True:
        printMenu()
        optiune=input("Dati optiunea: ")
        if optiune=="1":
            lista=uiAdaugaObiect(lista)
        elif optiune=="2":
            lista=uiStergeObiect(lista)
        elif optiune=="3":
            lista=uiModificaObiect(lista)
        elif optiune=="4":
            lista=uiMutaObiecte(lista)
        elif optiune=="5":
            lista=uiConcatenare(lista)
        elif optiune=="6":
            lista=uiLocatie(lista)
        elif optiune=="7":
            uiOrdoneaza(lista)
        elif optiune=="8":
            uiSumaPreturilor(lista)
        elif optiune=="a":
            showAll(lista)
        elif optiune=="x":
            break
        else:
            print("Optiune invalida! Reincercati!")
