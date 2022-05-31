
import csv
from FctScrapLivre import*

def WriteCsv(NameCsv,ListeTotale,encodage):
# Fonction qui écrit un fichier csv à partir d'une liste, l'encodage étant à préciser
# ouverture du fichier excel en écriture

    with open(NameCsv, 'w', encoding=str(encodage), newline="") as myFile2:  # ,encoding='utf-8'#sig indique a excel que utf-8 est utilisé pour l'encodage
        writer = csv.writer(myFile2,delimiter=";")  # Ecriture dans le fichier excel Avec la virgule pour séparer les champs
        LenListeTotale = ListeTotale.__len__()  # #récupération de la longueur de la liste de liste, la liste commençant à 0
        #print("longueur de la liste avant writer.writerow " + str(LenListeTotale))

        for iListe in ListeTotale:  # Ecrire la totalité des listes de listes dans le fichier excel
            writer.writerow(iListe)