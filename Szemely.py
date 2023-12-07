import datetime
class Szemely:
    def __init__(self,nev:str,szul:int,szSzam:int,nem:str):
        self.nev = nev
        self.szul = szul
        self.szSzam = szSzam
        self.nem = nem
        #Csak nőket
    def kor(self):
        #Tagfüggvény vagy osztály metódus  Az osztály adattagjain végeznek műveleteket
        #Kor számolás
        x = datetime.datetime.now()
        return x.year - self.szul
