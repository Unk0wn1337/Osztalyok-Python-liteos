

etelNev = ["Húsleves","Paradicsomlevees","gyümölcsleves"]
etelAr = [1200,1100,2000]
#Most annyi lista van, ahány tulajdonsága van az adott ételnek!
#Úgy lenne a jobb, ha csak 1 listánk lenne
#És 1 ételenek egybe kezelhetnék a tulajdonságait!
#Létrehozunk egy étel tipust - ez az étel általános leírását jelenti
#Konkrét étel tipus példányoisításkor jön létre
print("Az első leves ára",etelNev[0],etelAr[0])
from Etel import Etel
etelek=[]
etel=Etel("húsleves",1200,"leves") #Példányosítás
etelek.append(etel)
etel=Etel("paradicsomleves",1100,"leves")
etelek.append(etel)
etel= Etel("pörkölt",2300,"főétel")
etelek.append(etel)

index = 0
while index < len(etelek):
    print(f"Az {index}.indexedik étel {etelek[index].nev}nev {etelek[index].ar}ar {etelek[index].tipus}tipus")
    index+=1

from Szemely import Szemely
szemelyek = []
szemely = Szemely("Károly",2000,365251,"Férfi")
szemelyek.append(szemely)
szemely = Szemely("Géza",1999,315551,"Férfi")
szemelyek.append(szemely)
szemely = Szemely("Ferenc",1998,315651,"Férfi")
szemelyek.append(szemely)
szemely = Szemely("Anita",1996,215651,"Nő")
szemelyek.append(szemely)
szemely = Szemely("Krisztina",1997,2153651,"Nő")
szemelyek.append(szemely)
szemely = Szemely("Liza",1999,2158651,"Nő")
szemelyek.append(szemely)
index = 0
while index < len(szemelyek):
    print(f"Név: {szemelyek[index].nev}, Kor: {szemelyek[index].szul}, Igazolványszám: {szemelyek[index].szSzam}, Nem: {szemelyek[index].nem} ")
    print(f"{szemelyek[index].nev}, {szemelyek[index].kor()} éves.")
    index+=1