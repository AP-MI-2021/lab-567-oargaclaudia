from Domain.obiect import getId, getNume, getDescriere, getPret, getLocatie
from Logic.CRUD import adaugaObiect, getById, stergeObiect, modificaObiect


def testAdaugaObiect():
    lista=[]
    lista=adaugaObiect("1", "Dulap", "Utilizat pentru depozitarea obiectelor", 550.2, "APSM",lista)
    assert len(lista) == 1
    assert getId(getById("1",lista))=="1"
    assert getNume(getById("1",lista))=="Dulap"
    assert getDescriere(getById("1",lista))=="Utilizat pentru depozitarea obiectelor"
    assert getPret(getById("1",lista))==550.2
    assert getLocatie(getById("1",lista))=="APSM"

def testStergeObiect():
    lista = []
    lista = adaugaObiect("1", "Dulap", "Utilizat pentru depozitarea obiectelor", 550.2, "APSM", lista)
    lista=adaugaObiect("2", "Veioza", "Utilizat pentru luminarea spatiului de lucru", 100, "ASAC", lista)

    lista=stergeObiect("1",lista)
    assert len(lista)==1
    assert getById("1",lista) is None
    assert getById("2", lista) is not None

    try:
        lista = stergeObiect("100", lista)
        assert False
    except ValueError:
        assert len(lista) == 1
        assert getById("2", lista) is not None
    except Exception:
        assert False


def testModificaObiect():
    lista = []
    lista = adaugaObiect("1", "Dulap", "Utilizat pentru depozitarea obiectelor", 550.2, "APSM",lista)
    lista = adaugaObiect("2", "Veioza", "Utilizat pentru luminarea spatiului de lucru", 100, "ASAC", lista)

    lista = modificaObiect("1", "Pix", "Obiect de scris",5,"ALCS", lista)

    obiectUpdatat = getById("1", lista)
    assert getId(obiectUpdatat) == "1"
    assert getNume(obiectUpdatat) == "Pix"
    assert getDescriere(obiectUpdatat) == "Obiect de scris"
    assert getPret(obiectUpdatat) == 5
    assert getLocatie(obiectUpdatat) == "ALCS"

    obiectNeupdatat = getById("2", lista)
    assert getId(obiectNeupdatat) == "2"
    assert getNume(obiectNeupdatat) == "Veioza"
    assert getDescriere(obiectNeupdatat) == "Utilizat pentru luminarea spatiului de lucru"
    assert getPret(obiectNeupdatat) ==100
    assert getLocatie(obiectNeupdatat) == "ASAC"

    lista = []
    lista = adaugaObiect("1", "Dulap", "Utilizat pentru depozitarea obiectelor", 550.2, "APSM", lista)
    lista = adaugaObiect("2", "Veioza", "Utilizat pentru luminarea spatiului de lucru", 100, "ASAC", lista)
    obiectNeupdatat = getById("1", lista)
    assert getId(obiectNeupdatat) == "1"
    assert getNume(obiectNeupdatat) == "Dulap"
    assert getDescriere(obiectNeupdatat) == "Utilizat pentru depozitarea obiectelor"
    assert getPret(obiectNeupdatat) == 550.2
    assert getLocatie(obiectNeupdatat) =="APSM"
