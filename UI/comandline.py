from Logic.CRUD import adaugaObiect, getById, stergeObiect, modificaObiect
from UI.Console import showAll


def command_line_console(lista):
    while True:
        try:
            print("Pentru ajutor scrie help ")
            comanda = input("Dati comanda ")
            if comanda == "help":
                print("Pentru a adauga un nou obiect scrieti add urmat de date")
                print("pe care doriti sa le introduceti separate prin virgula ")
                print("Pentru a modifica,scrieti update,apoi virgula si id-ul obiectului ce urmeaza")
                print("Sa fie modificat,urmat de noile date")
                print("Pentru a sterge un obiect scrieti delete,apoi virgula si id-ul obiectului ce urmeaza sa se stearga")
                print("Pentru a afisa obiectele scrie showall")
                print("Puteti scrie mai multe comenzi separandu-le prin ;")
                print("Exemplu: add,1,pix,obiect de scris,10,ASCD")
                print("add,2,lampa,obiect de iluminat,200,ASDS")
                print("delete,1;showall")
                print("se face un update si vom avea 2,lampa,obiect de iluminat,200,ASDS")
                print("stop pentru iesi")
            elif comanda == "stop":
                break
            else:
                executa = comanda.split(";")
                for i in range(len(executa)):
                    comanda_separata = executa[i].split(",")
                    if comanda_separata[0] == "add":
                        if len(comanda_separata) != 6:
                            raise ValueError("Trebuie sa introduceti exact 5 comenzi! ")
                        id = comanda_separata[1]
                        nume = comanda_separata[2]
                        descriere = comanda_separata[3]
                        pret = float(comanda_separata[4])
                        locatie = comanda_separata[5]
                        lista = adaugaObiect(id, nume, descriere, pret, locatie, lista)
                    elif comanda_separata[0] == "delete":
                        id = comanda_separata[1]
                        lista = stergeObiect(id, lista)
                        print("S-a sters un obiect")
                    elif comanda_separata[0] == "update":
                        if len(comanda_separata) != 6:
                            raise ValueError("Trebuie sa introduceti exact 5 date! ")
                        id = comanda_separata[1]
                        nume = comanda_separata[2]
                        descriere = comanda_separata[3]
                        pret = float(comanda_separata[4])
                        locatie = comanda_separata[5]
                        lista = modificaObiect(id, nume, descriere, pret, locatie, lista)
                        print("Au fost modificate date")
                    elif comanda_separata[0] == "showall":
                        showAll(lista)
                    else:
                        print("Comanda gresita ")
        except ValueError as ve:
            print("Eroare: {}".format(ve))
