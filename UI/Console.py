from Domain.obiect import toString
from Logic.CRUD import adaugaObiect, stergeObiect, modificaObiect
from Logic.funct import mutareObiecte


def printMenu():
    print("1. Adaugare obiect ")
    print("2. Stergere obiect ")
    print("3. Modificare obiect ")
    print("4. Mutati obiectele dintr-o locatie in alta ")
    print("a. Afisare obiect ")
    print("X. Iesire")


def uiAdaugaObiect(lista):
    id=input("Dati id-ul ")
    nume=input("Dati numele ")
    descriere=input("Dati descrierea ")
    pret=float(input("Dati pretul "))
    locatie=input("Dati locatia ")

    return adaugaObiect(id, nume, descriere, pret, locatie, lista)


def uiStergeObiect(lista):
    id = input("Dati id-ul obiectului pe care vreti sa il stergeti ")
    return stergeObiect(id,lista)


def uiModificaObiect(lista):
    id = input("Dati id-ul obiectului de modificat ")
    nume = input("Dati noul nume ")
    descriere = input("Dati noua descriere ")
    pret = float(input("Dati noul pret "))
    locatie = input("Dati noua locatie ")
    return modificaObiect(id, nume, descriere, pret, locatie, lista)
def uiMutaObiecte(lista):
    substringLocatie = input("Dati locatia din care vreti sa mutati obiectele ")
    substringLocatieNoua = input("Dati locatia in care vreti sa mutati obiectele: ")
    return mutareObiecte(substringLocatie, lista, substringLocatieNoua)

def showAll(lista):
    for obiect in lista:
        print(toString(obiect))


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
        elif optiune=="a":
            showAll(lista)
        elif optiune=="x":
            break
        else:
            print("Optiune invalida! Reincercati!")
