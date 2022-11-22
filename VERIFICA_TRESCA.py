import pprint
import re

global nome,cognome
campionati={}

pp = pprint.PrettyPrinter(indent=4)
"""
Una bella analisi:

- Incomincio a creare le varie funzioni secondarie e primarie per poi
implementarle nel menu.
Aggiungo 3 tuple con il nome della disciplina,
il tempo riportato(min,sec,cent) ed infine la categoria.
"""

# Functions

def leggiNome():
    global nome
    nome=str(input("Inserire il nome dell' atleta"))
    while len(nome)==0:
        nome=str(input("Inserire il nome dell' atleta"))
        return nome
# ------------------------------------------       
def leggiCognome():
    global cognome
    cognome=str(input("Inserire il cognome dell' atleta"))
    while len(cognome)==0:
        cognome=str(input("Inserire il cognome dell' atleta"))
        return cognome
# ------------------------------------------       
def leggiChiave():
    nome=leggiNome()
    cognome=leggiCognome()    
    
    return nome+""+cognome
# ------------------------------------------
def numAtleti():
    nAtleti=int(input("Inserire il numero di atleti da voler aggiungere"))
    while nAtleti==0:
        print("Inserire un numero di atleti maggiore di 0")
        nAtleti=int(input("Inserire il numero di atleti da voler aggiungere"))
        return nAtleti
# ------------------------------------------       
def richiestaDisciplina():
    print("Discipline disponibili: // Corsa campestre // // Corsa 100 mt // // Corsa 200 mt // ")
    disciplina=str(input("Inserire la disciplina: "))
    while len(disciplina)==0:
        print("E obbligatorio inserire una discplina ")
        disciplina=str(input("Inserire la discplina: "))
        
        return disciplina
# ------------------------------------------       
campionati={"Giuseppe Gullo":[("Corsa campestre",(40,21,0),"Allievi"), ("Corsa 100mt",(0,12,0),"Juniores mas"),("Corsa 200mt",(0,29,19),"Juniores mas")],
                "Antonia Barbera":[("Corsa campestre",(0,39,11),"Juniores fem"), ("Corsa 100mt",(0,18,0),"Juniores fem"),("Corsa 200mt",(0,0,0),"Juniores fem")],
                "Nicola Esposito":[("Corsa campestre",(0,43,22),"Allievi"),("Corsa 100mt",(0,14,0),"Juniores mas",("Corsa 200mt",(0,36,19),"Juniores mas"))]}
pp.pprint(campionati)
    

    # ES 7 MINIMO ES 8 MASSIMO
# ES 2
campionati["Thomas Tresca"]=[("Corsa campestre",(20,10,0),"Juniores mas"), ("Corsa 100mt",(10,12,0),"Juniores mas"),("Corsa 200mt",(12,29,19),"Juniores mas")]
pp.pprint(campionati)

# ES 3

campionati["Giuseppe Gullo"]=[(("Corsa campestre",(40,21,0),"Allievi"), ("Corsa 100mt",(0,12,0),"Juniores mas"),("Corsa 200mt",(0,29,19),"Juniores mas"),("Corsa 400mt",(0,40,34),"Allievo"))]
campionati["Antonia Barbera"]=[("Corsa campestre",(0,39,11),"Juniores fem"), ("Corsa 100mt",(0,18,0),"Juniores fem"),("Corsa 200mt",(0,0,0),"Juniores fem"),("Corsa 400mt",(0,39,10),"Allieva")]
campionati["Nicola Esposito"]=[("Corsa campestre",(0,43,22),"Allievi"),("Corsa 100mt",(0,14,0),"Juniores mas",("Corsa 200mt",(0,36,19),"Juniores mas"),("Corsa 400mt",(0,40,10),"Allievo"))]
campionati["Thomas Tresca"]=[("Corsa campestre",(0,43,22),"Allievi"),("Corsa 100mt",(0,14,0),"Juniores mas",("Corsa 200mt",(0,36,19),"Juniores mas"),("Corsa 400mt",(0,40,26),"Allievo"))]
