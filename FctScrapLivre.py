import os

import requests
from bs4 import BeautifulSoup
from FctProjet2 import*
import urllib.request

def ScrapLivre(url):
    ListUrlImgError = []
    ListeNameImgError=[]
    ListeChampsLivre = []
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser') #html.parser
                            # content signifie récupération brute de la page téléchargée
                            # Beautifulsoup saura quel code html est utilisé tout seul en ayant téléchargé de façon brute

        ListeChampsLivre.append (url)

        #UPC
        # for i in range(7): #test de l'index correspondant
        i = 0
        Upc = soup.find_all('td')[i].get_text()
        #UpcNew = Upc.replace('Price (incl. tax)', "")
        UpcNew = Upc
        ListeChampsLivre.append (UpcNew)

        #RECUPERATION DU TITRE ok
        titles = soup.find('h1')
        #print ("Titres         " + str(titles))
        chaineTitle = str(titles)
        # ChaineTitle contient le titre avec les balises qu'il faudra supprimer avec la fonction Projet2Chaine
        # fonction qui recherche la position précédente de ce que l'on veut récupérer avec charcherch et
        # récupère jusqu'au caractere à ne pas récupéré défini en entrée EndChar
        #print ("Titre du livre :"  + (Projet2Chaine(chaineTitle, "<h1>", "<"))+ "\n") #TITRE A RECUPERER
        titre = (Projet2Chaine(chaineTitle, "<h1>", "<"))
        ListeChampsLivre.append (titre)
        # FIN RECUPERATION DU TITRE

        #PRICE_INCLUDING_TAX
        #for i in range(7):#test de l'index correspondant
        i = 3
        PriceInclTax = soup.find_all('td')[i].get_text()
        PriceInclTaxNew = PriceInclTax.replace('Price (incl. tax)', "")
        #print(PriceInclTaxNew)
        PriceInclTaxNew = PriceInclTaxNew.replace('Â', "")
        #print("PricInclTax : " + PriceInclTaxNew + "\n")
        ListeChampsLivre.append (str(PriceInclTaxNew))

        # PRICE_EXCLUDING_TAX
        #for i in range(7): #test de l'index correspondant
        i = 2
        PriceExclTax = soup.find_all('td')[i].get_text()
        PriceExclTaxNew = PriceExclTax.replace('Price (incl. tax : )', "")
        #print (PriceExclTaxNew)
        PriceExclTaxNew = PriceExclTaxNew.replace('Â', "")
        #print("PricExclTax : " +PriceExclTaxNew + "\n" )
        ListeChampsLivre.append (PriceExclTaxNew)

        # NUMBER AVAILABLE
        #for i in range(7): #test de l'index correspondant
        i = 5
        NumberAvble = soup.find_all('td')[i].get_text()
        #print(str(i))
        NumberAvbleNew = NumberAvble.replace('Price (incl. tax)', "")
        NumberAvbleNew = NumberAvbleNew.replace('Â£', "")
        #print (NumberAvbleNew)
        NumberAvbleNew = (re.findall('\d+',NumberAvbleNew)[0])
        #print("Number Available : " + NumberAvbleNew + "\n")
        ListeChampsLivre.append (str(NumberAvbleNew))


        #RECUPERATION PRODUIT DESCRIPTION avec balise p, à la 3eme balise, on a ce que l'on cherche
        #auparavant, un for range a permis d'afficher le resultat de toutes les balises p et en parallèle,
        #la valeur de i
        # for i in range(3):
        i=3
        ProduitDescription = soup.find_all('p')[i].get_text()
        ListeChampsLivre.append (ProduitDescription)
        #FIN RECUPERATION PRODUIT DESCRIPTION

        # CATEGORY
        # for i in range(2): #test de l'index correspondant
        i = 2
        Category = soup.find_all('li')[i].get_text()
        # print(i)
        #print("Category :" + Category + "\n")
        ListeChampsLivre.append (Category)

        #REVIEW RATING
        mydivs = soup.findAll("p", {"class": "star-rating"})
        chaine = str(mydivs)
        chaine = chaine[0:30]
        char = "g"
        PositDebNbre = (chaine.find(char))
        char = ">"
        PositFinNbre = (chaine.find(char))
        #print (str(PositDebNbre) + "    " + str(PositFinNbre) )
        NbrStar = chaine [(PositDebNbre + 1) : (PositFinNbre - 1)]
        #print (NbrStar)
        ListeChampsLivre.append(NbrStar)

        #Le nombre d'étoiles a récuperer est juste apres star-rating dans la chaine.
        #1-Recherche de la positon de fin de 'star_rating' dans la trame
        #2-Recuperation de la trame (Newchaine) juste après le dernier caractère de star-rating
        #3 rechercher la position du caractere (") qui est à la suite du nombre dans la nouvelle trame
        #4 récupération des caractere de la nouvelle trame jusqu a la position du caractere qui suit le nombre

        #IMAGE_URL
        #for i in range(1):
        Category = soup.findAll("div", {"class": "item active"})
        #print (Category)

        chaine = str(Category)
        #Récupération adresse url à partir du soup en combinant ce qu'il y a ajouter et supprimer dans la chaine
        ImgUrl= (Projet2Chaine(chaine, "src=\"", "\""))#"src=\"", "\""))
        ImgUrl = ImgUrl[5:-3] #[5:-3]
        #print (ImgUrl)
        ImgUrl = "http://books.toscrape.com" + ImgUrl + "jpg"
        #print (ImgUrl)
        NameImage = (titre + ".jpg")
        ListeChampsLivre.append(ImgUrl)
        #print(os.path.join('d:', os.sep, 'D:\\Image'))

        try : #télécharger les images
            #cheminFichier = ("\home\lionel\openclassrooms\projet2\Image\" + str(NameImage))
            urllib.request.urlretrieve(ImgUrl, NameImage)
           #time.slepp(0.1)

        except :
            print ("Erreur de fichier au téléchargement de l'image " + NameImage + " - " + ImgUrl)
            #print(Category)

            try:  # télécharger les images
                NameImage = NameImage.replace('/', '_')
                urllib.request.urlretrieve(ImgUrl, NameImage)
                print("Essai numéro 2 après suppression de caractère : / dans le nom de l'image ok")
                #f =open(NameImage,'wb')
                #f.write(urllib.request.urlopen(ImgUrl).read())
                #f.close()
                #urllib.request.urlretrieve(ImgUrl, NameImage)
            except:
                print("Erreur de fichier au téléchargement au 2eme essai de l'image " + NameImage + " - " + ImgUrl)
                ListeNameImgError.append(NameImage)
                ListUrlImgError.append(ImgUrl)

        files = NameImage
        import shutil
        # Création du répertoire Image si absent
        wd = os.getcwd()
        WorkingDirectory = ("working directory is ", wd)
        WorkingDirectory = str(wd)
        WorkingDirectoryImage = WorkingDirectory + "/Image/"

        if not os.path.exists(WorkingDirectoryImage):
            os.makedirs(WorkingDirectoryImage)

        #Envoi du fichier dans le répertoire
        try:
            shutil.move(files, WorkingDirectoryImage)
        except :

            print ("Déplacement du fichier impossible. Vérifier que des fichiers du même nom ne sont pas déjà présents dans le répertoire ?")
            print("suppression de l'ancien fichier en double et remise du nouveau à la place : " + str(WorkingDirectoryImage) + str(files))
            SuppOldFichier = (str(WorkingDirectoryImage) + str(files))
            print (SuppOldFichier)
            os.remove(SuppOldFichier)
            shutil.move(files, WorkingDirectoryImage)

        # ou, selon ce qui sera le plus pratique
        Category = soup.find_all('div')[i].get_text()
        #print("Category : " + (Projet2Chaine(chaine, "src=\"", "\"")))

        return (ListeChampsLivre,ListeNameImgError,ListUrlImgError)

def ScrapUrlCatlLivre(url):

    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser') #html.parser
                            # content signifie récupération brute de la page téléchargée
                            # Beautifulsoup saura quel code html est utilisé tout seul en ayant téléchargé de façon brute
                            # si response.content, on laisse beautifulsoup deviner l'encodage
        #titles = soup.find('li')

        #print(titles)
        AllSideCat = soup.find("div",{"class":"side_categories"})
        AllCategories = str(AllSideCat)
        #print ("all categories********************************************************"+ AllCategories)
        #Rechercher les positions de debut -commence par href- et fin -se termine par html- dans une chaine à partir
        # des caracteres de début et de fin
        #Récupérer les strings à partir du caractere de debut indiqué + x caarcateres
        # et jusqu'au caractere de fin indiqué + x caracteres
        #Une fois le string récupéré, le mettre dans une liste en concaténant avec le string manquant si besoin
        charStart= "href"
        charEnd="html"
        ListeCategories =[]
        for i in range(51):#tes
            #print(CherchPosit(AllCategories, charStart, charEnd))
            DebutStr,FinStr = CherchPosit(AllCategories, charStart, charEnd)
            DebutStr = DebutStr + 6
            FinStr = FinStr + 4
            stringCat = (AllCategories [DebutStr:FinStr])
            if i>0 :
                urlCat = "http://books.toscrape.com/" + stringCat
                #print(urlCat)
                ListeCategories.append(urlCat)
            AllCategories = (AllCategories [FinStr:-1]) #récupère la chaine de Fin string à partir de la position de fin du string récupéré
    return(ListeCategories)

def ScrapUrlLivre(url):
    ListeLivreInCat = []
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser') #html.parser
                            # content signifie récupération brute de la page téléchargée
                            # Beautifulsoup saura quel code html est utilisé tout seul en ayant téléchargé de façon brute
                            # si response.content, on laisse beautifulsoup deviner l'encodage

        AllBooksCat = soup.find("section")#, {"class": "a href"})
        AllBooksInCategories = str(AllBooksCat)

        #print ("all books in categories ********************************************************"+ AllBooksInCategories)
        #Rechercher les positions de debut -commence par href- et fin -se termine par html- dans une chaine à partir
        # des caracteres de début et de fin
        #Récupérer les strings à partir du caractere de debut indiqué + x caarcateres
        # et jusqu'au caractere de fin indiqué + x caracteres
        #Une fois le string récupéré, le mettre dans une liste en concaténant avec le string manquant si besoin
        charStart1 = "h3"
        charStart= "h3><a href"#a href
        charEnd="index.html"#index.html
        ListeLivreInCat =[]
        Inverseur = False
        FinListe = False

        for i in range(50):#tes
            #print(CherchPosit(AllBooksInCategories, charStart, charEnd))
            DebutStr, FinStr = CherchPosit(AllBooksInCategories, charStart, charEnd)
            #print ("test recherche scrap " + (AllBooksInCategories[DebutStr: FinStr]))

            #FinListe devient vrai quand on a "-1" en réponse de nouvelle recherche de chaine dans chaine
            if (DebutStr==-1):
                FinListe = True
                #print ("DebutStr ====== -1")
            else :
                FinListe = False

            #AllBooksInCategories = (AllBooksInCategories[FinStr:-1])  # récupère la chaine de Fin string à partir de la position de fin du string récupéré
            #Récupère la trame à partir de charStart1 jusqu'à la fin
            #DebutStr, FinStr = CherchPosit(AllBooksInCategories, charStart1,"")
            #AllBooksInCategories = (AllBooksInCategories[(DebutStr+1):-1])
            #Récupère le contenu en charchant de chartStart à charEnd,
            # et modification de la valeur de la position dans la trame pour récupérer les caractères voulus
            #print(CherchPosit(AllBooksInCategories, charStart, charEnd))
            DebutStr,FinStr = CherchPosit(AllBooksInCategories, charStart, charEnd)
            DebutStr = DebutStr + 17
            FinStr = FinStr + 10
            stringBook = (AllBooksInCategories [DebutStr:FinStr])

            #On retrouve 2 fois les mêmes éléments; Ne récupérer qu'une fois sur deux
            if (Inverseur and (FinListe==False)):
                urlCat = "http://books.toscrape.com/catalogue/" + stringBook
                #print(urlCat)
                if FinListe:
                    print ("Fin liste")
                else:
                    ListeLivreInCat.append(urlCat)
            Inverseur = not Inverseur
            AllBooksInCategories = (AllBooksInCategories [FinStr:-1]) #récupère la chaine de Fin string à partir de la position de fin du string récupéré
    return(ListeLivreInCat)

def VérifPageNext(url):
    response = requests.get(url)
    PageNext=""
    HtmlPageNext =""
    urlNew = ""
    Url1 = ""
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser') #html.parser
                            # content signifie récupération brute de la page
        RecherchePage2 = soup.find(('li'), {"class": "next"})
        # RecherchePage2 = soup.find('body')#, {"class": "pager"}
        #print("recherche page 2 : " + str(RecherchePage2))
        RecherchePage2New = str(RecherchePage2)
        PageNext=""
        if RecherchePage2New == "None":
            #print ("pas d'autre page ")
            PageNext = "None"
        else:
            #print("Page supplémentaire : " + str(RecherchePage2))
            PageNext = "Next"
        Page_x = str(RecherchePage2New.find("page-"))

        charStart ="a href"
        charEnd = "\">next"
        DebutStr, FinStr = CherchPosit(RecherchePage2New, charStart, charEnd)
        DebutStr = DebutStr + 8
        FinStr = FinStr #+ 10
        NumPage = (RecherchePage2New[DebutStr:FinStr])
        #print (NumPage)

        if (PageNext == "Next"):
            charStart =""
            charEnd = "ge"
            #print (url)
            Position=(url.find("books/"))
            Url1 = url[0:(Position +6)]
            Url2 = url[Position +6 : -1]
            #print (Url1)
            #print(Url2)
            Position = (Url2.find("/"))
            Url3 = Url2 [0:Position+1]
            #print (Url3)
            urlNew = Url1 + Url3 + NumPage
            #print (urlNew)
            HtmlPageNext = urlNew
        else :
            HtmlPageNext = url
    return(PageNext,HtmlPageNext)
