from Domain.obiect import creeazaObiect, getId, getNume, getLocatie, getPret, getDescriere


def testObiect():
    obiect = creeazaObiect("1", "Dulap", "Utilizat pentru depozitarea obiectelor", 550.2, "APSM")

    assert getId(obiect) == "1"
    assert getNume(obiect) == "Dulap"
    assert getDescriere(obiect) == "Utilizat pentru depozitarea obiectelor"
    assert getPret(obiect) == 550.2
    assert getLocatie(obiect) == "APSM"
