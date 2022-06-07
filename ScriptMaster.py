import os
import time

import requests
from bs4 import BeautifulSoup
import re #import de regular expression
from FctProjet2 import*
from FctScrapLivre import*
from Fct_Ecrire_CSV import*
import csv
import shutil

#Déclaration des listes et variables
ListeChampsLivre = []
NameCsv =""
ListeNameCategorie = []
ListNameErrImg = []
ListUrlErrImg = []

#Ecriture de l'entete des fichiers csv dans ListeEnTeteCol
ListeEnTeteCol = []
ListeEnTeteCol.append('product_page_url')
ListeEnTeteCol.append('universal_ product_code (upc)')
ListeEnTeteCol.append('title ')
ListeEnTeteCol.append('price_including_tax')
ListeEnTeteCol.append('price_excluding_tax')
ListeEnTeteCol.append('number_available')
ListeEnTeteCol.append('product_description')
ListeEnTeteCol.append('category')
ListeEnTeteCol.append('review_rating')
ListeEnTeteCol.append('image_url')

#Scraper les url des categories et les mettre dans ListeCategories
# 1- Pour toutes les catégories
#   1-1 Récupérer un nom de catégorie pour nommer le fichier csv
#   1-2 Mettre l'url de la 1ere page dans une liste d'url de pages -ListeUrlPage-
#   1-3Vérifier si Next Page
#   1-3-1 si NextPage, ajouter l'url de la page dans la liste d'url des pages
        # jusqu'à ce qu'il n'y ait plus de prochaine page

# 2 Scraper avec toutes les url des pages les url des livres, et mettre toutes ces url dans une même liste qui contient donc toutes les url
        # de tous les livres d'une catégorie, quel que soit le nombre de pages -ListBookInCategories002-

# Pour tous les livres de la catégorie scraper les champs à récupérer, et mettre le résultat dans la liste
# de liste des champs de livre d'une même catégorie -ListeChampsLivre-

# Mettre la liste d'entête des colonnes dans le fichier listeCSV
# Mettre la liste de liste des champs du livre à la suite de la listeCsv

# Ecrire le fichier Excel à partir du fichier listeCsv


#Scraper les url des categories et les mettre dans ListeCategories
url = 'http://books.toscrape.com/index.html'
ListeUrlCategories = (ScrapUrlCatlLivre(url))
print("Liste des Categories : " + str(ListeUrlCategories))

#Récupération de la longueur de la liste des url des catégories
LenListeUrlCategories =    ListeUrlCategories.__len__()

# Pour toutes les catégories
# 1-1 Récupérer un nom de catégorie pour nommer le fichier csv

for i in range(LenListeUrlCategories): #Pour toutes les catégories
    NbrPage = 0
    indexNbrPage = 0
    url = (ListeUrlCategories[i]) #Mettre
    charFin="HTML"
    ListeUrlPage=[]
    LenListBookInCategories001 = []
    ListeUrlPage.clear()
    x,y =(CherchPosit(ListeUrlCategories[i], "books/", "/index.html"))
    #print (ListeCategories[i] [(x+6):(y)])
    NameCsv = (ListeUrlCategories[i] [(x+6):y]) + ".csv"

    # Récupérer l'url de la catégorie dans la liste des url categorie
    url = (ListeUrlCategories[i])
    index = 0
    ListeUrlPage.append(ListeUrlCategories[i])
    #Vérifier si une autre page
    PageNext, HtmlNextPage = VérifPageNext(url)
    #print(str(PageNext), HtmlNextPage)
    url2 = HtmlNextPage
    #print("url2 Scrape : " + url2)

    # Si une autre page, et tant qu'il y aura une autre page
    # Ajouter à la ListeUrlpage, toutes les url des pages jusqu'à ce qu'il n'y ait plus de prochaine page -Next-
    while (PageNext == "Next"):
        print("ListeUrlPage[indexNbrPage]" + ListeUrlPage[indexNbrPage])
        NbrPage = NbrPage +1
        #print ("nombre de page   "+str(NbrPage))

        PageNext, HtmlNextPage = VérifPageNext(ListeUrlPage[indexNbrPage])
        if (PageNext == "Next"):
            indexNbrPage = indexNbrPage + 1
            ListeUrlPage.append(HtmlNextPage)
        else:
            print ("Plus d'enregistrement d'url de page dans la catégorie. Nombre de pages trouvées " + str(NbrPage))
        #print ("Page Next = " + PageNext)
        #print (ListeUrlPage[indexNbrPage])

    ListeChampsLivre =[]
    ListeChampsLivre.clear()
    ListBookInCategories001 = []
    ListBookInCategories002 =[]
    ListeChampsLivreTemp =[]

    # Pour toutes les pages de la catégorie
    # Scraper les url des livres, et ajouter toutes les url de chaque page dans la même liste ListBookInCategories002
    LenListeUrlPage = ListeUrlPage.__len__()  # récupération de la longueur de la liste d'url de page pour la categorie
    #print ("nombre de pages dans la categorie ListeUrlPage.__len__()" + str(LenListeUrlPage) )
    ListBookInCategories002.clear()
    ipage = 0
    for i_page in range(LenListeUrlPage):
        ListBookInCategories001 = ScrapUrlLivre(ListeUrlPage[i_page])
        ListBookInCategories002.extend(ListBookInCategories001)

    print (ListBookInCategories002)
    LenListBookInCategories002 = ListBookInCategories002.__len__()
    print ("Attente scrapping des livres de la catégorie et du téléchargement des images pour les " + str(LenListBookInCategories002) + " livres de la catégorie ")
    Temps = LenListBookInCategories002 * 1.14
    print (" Approximativement " + str(round(Temps)) + " secondes")

    #print("LenListBookInCategories002")
    #print(LenListBookInCategories002)

    # Pour tous les url des livres de toutes les pages d'une catégorie, scraper tous les champs des livres
    # et les mettre dans une liste de liste ListeChampsLivre
    # cette liste contient tous les champs de tous les livres d'une catégorie
    LenListBookInCategories002 = ListBookInCategories002.__len__()  # récupération de la longueur de la liste de liste de livres dans la catégorie
    for i_PageBook in range(LenListBookInCategories002):  # Pour tous les livres jusqu'à la fin ajouter le livre dans la liste totale
        #
        ListeChampsLivreTemp, ListeNameImgError, ListUrlImgError = (ScrapLivre(ListBookInCategories002[i_PageBook]))
        ListeChampsLivre.append(ListeChampsLivreTemp)

        #print(ListeNameImgError)
        LenListeNameImgError = ListeNameImgError.__len__()
        if (LenListeNameImgError >0):
            print(LenListeNameImgError)
            time.sleep(60)
            ErrTelechImgUrl(LenListeNameImgError, ListeNameImgError, ListUrlImgError)

    LenListeChampsLivre = ListeChampsLivre.__len__()  # récupération de la longueur de la liste de liste

    ListeCsv = []
    ListeCsv.clear()
    # Mettre le ListeEnTeteCol dans la liste ListeCSV
    ListeCsv.append(ListeEnTeteCol)

    # Pour toute la liste de liste de champs des livres, ajouter la liste des champs d'un livre à la suite du
    # fichier CSV
    for ib in ListeChampsLivre:  # Pour tous les livres jusqu'à la fin ajouter le livre dans la liste totale
        ListeCsv.append(ib)

    LenListeCsv = ListeCsv.__len__()
    print("Nombre de livres scrapés dans le fichier csv : " + str(LenListeCsv -1 ))

    #Ecrire le fichier csv à partir du fichier ListeCSV en utilisant comme nom, le nom tiré du nom de la catégorie
    # récupéré plus haut à partir de l'url de la catégorie
    #Decriptage utf8, sig indique au fichier excel que ce sera celui utilisé
    encodage = 'utf-8-sig'
    WriteCsv(str(NameCsv), ListeCsv, str(encodage))

    #Transfert du fichier csv dans le répertoire CSV
    files = NameCsv
    # Création du répertoire Csv si absent
    # Création des répertoires pour ranger les images et fichiers Csv
    wd = os.getcwd()
    #WorkingDirectory = ("working directory is ", wd)
    WorkingDirectory = str(wd)
    WorkingDirectoryCsv = WorkingDirectory + "/Csv/"
    if not os.path.exists(WorkingDirectoryCsv):
        os.makedirs(WorkingDirectoryCsv)

    #if not os.path.exists(WorkingDirectoryImage):
    #    os.makedirs(WorkingDirectoryImage)

    #wd = os.getcwd() #Recup répertoire courant
    #WorkingDirectory = ("working directory is ", wd)
    #WorkingDirectory = str(wd)
    #WorkingDirectoryCsv = WorkingDirectory + "/Csv/"
    #WorkingDirectoryCsv = ("/home/lionel/openclassrooms/projet2/Csv")
    try:
        shutil.move(files, WorkingDirectoryCsv)
    except:
        print("Déplacement du fichier impossible. Vérifier que des fichiers du même nom ne sont pas présents ?")
        print("suppression de l'ancien fichier en double et remise du nouveau à la place : " + str(
            WorkingDirectoryCsv) + str(files))
        SuppOldFichier = (str(WorkingDirectoryCsv) + str(files))
        os.remove(SuppOldFichier)
        shutil.move(files, WorkingDirectoryCsv)

