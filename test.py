# ["Marian":5,"John":2,"Ioanide":10,"BJohnson":11] ; n = 4 ; 
# Avem o clasa,profesor - metoda de calcul a mediei aritmetice, n - nr elevi, catalog - dict dictionar
# de forma ["key":value]
# cauta doc self + class
# cream clasa "Clasa" unde definim doua metode ale clasei, prima __init__ - constructor al clasei,
# care ia numele acesteia, unde initializam variabilele unui nou obiect cu self

# Dam mai departe valorile inputului de intrare prin argumentele constructorului input_n si input_dict
# metoda calcul_medie are variabile declarate suma,nume_elev,nota_elev,medie si
# calculeaza media elevilor din catalog(dict) prin extragerea key(nume_elev),
# value(nota_elev) din lista de touple-uri de forma touple=(key(0),value(1))
# formata cu metoda self.dict.items() din for. In variabilele nume_elev,nota_elev se introduc valorile
# din primul touple de pe cele doua pozitii elev[0],elev[1]. in suma se va calcula suma notelor
# iar in medie se calculeaza impartirea sumei la numarul de studenti declarat in init self.n,
# retureaza variabila medie

# items() - metoda folosita pentru dictionare unde se salveaza toate perechiile ["key":value] ca o lista
# de touplete de forma touplet=(key(0),value(1)). 
# self - pointerul curent al obiectului, poate fi folosit doar in interiorul unei clase, trebuie
# folosit ca prim argument in metodele clasei




class Clasa():

    def __init__(self,input_n,input_dict):
        self.n = input_n
        self.dict = input_dict

    def calcul_medie(self):
        suma = 0
        
        for elev in self.dict.items(): 
            nume_elev = elev[0]
            nota_elev = elev[1]
            suma += nota_elev # suma = suma + nota_elev 
            print(nume_elev)
            print(nota_elev)
            print(suma)

        medie = suma / self.n
        return medie
    
dict_test = {"Marian":5,"John":2,"Ioanide":10,"BJohnson":11}
n_test = len(dict_test)  

Clasa_12I2 = Clasa(n_test, dict_test)  #constructor, Clasa12I2 obiect

print("Numar de elevi: "+str(Clasa_12I2.n))
print("Note elevi: "+str(Clasa_12I2.dict))

medie_test = Clasa_12I2.calcul_medie()
print("Media Clasei: "+str(medie_test))

# print("Apa Mar Apa\n Mar Apa Mar\t Muie")

# se declara variabilele de test dict si n cu valorile din catalog(dict) dict_test - dictionar propriu zis si
# n_test - lungimea dictionarului pentru rularea codului pentru erori
# Se instanteaza obiectul Clasa_12I2 cu constructorul Clasa cu argumentele n_test si dict_test care
# sunt preluate de metoda init.
# Se folosesc mai multe comezi de print pentru rezolvarea erorilor
# La final salvam in medie_test, rezultatul rularii unei metodei calcul_medie() a obiectului Clasa_12I2           