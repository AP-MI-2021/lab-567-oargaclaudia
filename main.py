from Logic.CRUD import adaugaObiect
from Tests.testAll import runAllTests
from UI.Console import runMenu
from UI.comandline import command_line_console


def main():
    runAllTests()
    lista=[]
    lista=adaugaObiect("1", "Dulap", "Utilizat pentru depozitarea obiectelor", 550.2, "APSM", lista)
    lista=adaugaObiect("2", "Veioza", "Utilizat pentru luminarea spatiului de lucru", 100, "ASAC", lista)
    command_line_console(lista)
main()
