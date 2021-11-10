from Tests.TestFunctionalitati import testMutareObiecte, testSchimbaDescrierea, testPretMaximLocatie, testOrdonareDupaPret, testsumaPreturilor
from Tests.testCRUD import testAdaugaObiect, testStergeObiect, testModificaObiect
from Tests.testDomain import testObiect
from Tests.testUndoRedo import testundoredo


def runAllTests():
    testObiect()
    testAdaugaObiect()
    testStergeObiect()
    testModificaObiect()
    testMutareObiecte()
    testSchimbaDescrierea()
    testPretMaximLocatie()
    testOrdonareDupaPret()
    testsumaPreturilor()
    testundoredo()