from Domain.obiect import getLocatie, getDescriere, getId
from Logic.CRUD import adaugaObiect, getById
from Logic.funct import mutareObiecte
from Logic.funct import concatenare, PretMaximLocatie, OrdonareDupaPret, sumaPreturilor


def testMutareObiecte():
    lista=[]
    lista=adaugaObiect("1","Telefon", "Faciliteaza comunicarea intre oameni", 1000, "ASPC",lista)
    lista=adaugaObiect("2","Laptop", "Asigura o buna desfasurare a proiectelor online", 3000, "ASPC",lista)
    lista=adaugaObiect("3", "Masina", "Deplasarea angajatilor", 20000, "AFCD",lista)
    lista=mutareObiecte("ASPC", lista, "AFCD")

    assert getLocatie(getById("1", lista)) == "AFCD"
    assert getLocatie(getById("2", lista)) == "AFCD"
    assert getLocatie(getById("3", lista)) == "AFCD"

def testSchimbaDescrierea():
    lista = []
    lista = adaugaObiect("1", "Telefon", "Faciliteaza comunicarea intre oameni", 1000, "ASPC", lista)
    lista = adaugaObiect("2", "Laptop", "Asigura o buna desfasurare a proiectelor online", 3000, "ASPC", lista)
    lista = adaugaObiect("3", "Masina", "Deplasarea angajatilor", 20000, "AFCD", lista)
    lista=concatenare(" asa", lista, 2000)
    assert getDescriere(getById("1", lista))=="Faciliteaza comunicarea intre oameni"
    assert getDescriere(getById("2", lista))=="Asigura o buna desfasurare a proiectelor online asa"
    assert getDescriere(getById("3", lista))=="Deplasarea angajatilor asa"

def testPretMaximLocatie():
    lista = []
    lista = adaugaObiect("1", "Telefon", "Faciliteaza comunicarea intre oameni", 1000, "ASPC", lista)
    lista = adaugaObiect("2", "Laptop", "Asigura o buna desfasurare a proiectelor online", 3000, "ASPC", lista)
    lista = adaugaObiect("3", "Masina", "Deplasarea angajatilor", 21000, "AFCD", lista)
    lista = adaugaObiect("4", "Pix", "obiect de scris", 10, "ASPC", lista)
    lista = adaugaObiect("5", "Lanterna ", "Obiect de iluminat ", 3000, "ASDF", lista)
    lista = adaugaObiect("6", "Bicicleta", "Deplasarea angajatilor", 20000, "AFCD", lista)

    rezultat=PretMaximLocatie(lista)
    assert len(rezultat)==3
    assert rezultat["ASPC"]==3000
    assert rezultat["AFCD"]==21000
    assert rezultat["ASDF"]==3000

def testOrdonareDupaPret():
    lista=[]
    lista = adaugaObiect("1", "Telefon", "Faciliteaza comunicarea intre oameni", 1000, "ASPC", lista)
    lista = adaugaObiect("2", "Laptop", "Asigura o buna desfasurare a proiectelor online", 3000, "ASPC", lista)
    lista = adaugaObiect("3", "Masina", "Deplasarea angajatilor", 21000, "AFCD", lista)
    lista = adaugaObiect("4", "Pix", "obiect de scris", 10, "ASPC", lista)
    lista = adaugaObiect("5", "Lanterna ", "Obiect de iluminat ", 3000, "ASDF", lista)
    lista = adaugaObiect("6", "Bicicleta", "Deplasarea angajatilor", 20000, "AFCD", lista)
    rezultat=OrdonareDupaPret(lista)
    assert getId(rezultat[0])=="4"
    assert getId(rezultat[1])=="1"
    assert getId(rezultat[2])=="2"
    assert getId(rezultat[3])=="5"
    assert getId(rezultat[4])=="6"
    assert getId(rezultat[5])=="3"

def testsumaPreturilor():
    lista=[]
    lista = adaugaObiect("1", "Telefon", "Faciliteaza comunicarea intre oameni", 1000, "ASPC", lista)
    lista = adaugaObiect("2", "Laptop", "Asigura o buna desfasurare a proiectelor online", 3000, "ASPC", lista)
    lista = adaugaObiect("3", "Masina", "Deplasarea angajatilor", 21000, "AFCD", lista)
    rezultat=sumaPreturilor(lista)
    assert len(rezultat)==2
    assert rezultat["ASPC"]==4000
    assert rezultat["AFCD"]==21000