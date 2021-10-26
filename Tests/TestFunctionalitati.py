from Domain.obiect import getLocatie
from Logic.CRUD import adaugaObiect, getById
from Logic.funct import mutareObiecte

def testMutareObiecte():
    lista=[]
    lista=adaugaObiect("1","Telefon", "Faciliteaza comunicarea intre oameni", 1000, "ASPC",lista)
    lista=adaugaObiect("2","Laptop", "Asigura o buna desfasurare a proiectelor online", 3000, "ASPC",lista)
    lista=adaugaObiect("3", "Masina", "Deplasarea angajatilor", 20000, "AFCD",lista)
    lista=mutareObiecte("ASPC", lista, "AFCD")

    assert getLocatie(getById("1", lista)) == "AFCD"
    assert getLocatie(getById("2", lista)) == "AFCD"
    assert getLocatie(getById("3", lista)) == "AFCD"
