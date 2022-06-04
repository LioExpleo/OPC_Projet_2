# Projet_2
#Utilisez les bases de Python pour l'analyse de marché

#Projet effectué par Lionel R. dans le cadre de la formation « Openclassroom »  - développeur d’applications python-.

Contexte :
Un site site "http://books.toscrape.com/ est constitué de catégories de livres.

Dans chaque catégorie peuvent se trouver plusieurs pages, et dans chaque page peuvent se trouver de 1 à 20 livres.

Chaque livre contient des champs - product_page_url, universal_ product_code (upc), title, price_including_tax, 
price_excluding_tax, number_available, product_description, category, review_rating, image_url-

Le but général du programme est d'extraire les informations concernant les livres.


Que fait le programme :

1er scapping : Récupération des 50 « URL » des catégories dans une liste de catégorie. 

2ème scapping : Pour chaque catégorie dans la liste, récupération des URL des pages de la catégorie dans une liste de 
pages par catégorie.

3ème scrapping : Pour chaque page dans la liste de pages par catégorie, récupération des URL de chaque livre dans une 
liste de livres par catégorie.

4ème scrapping : pour chaque livre dans la liste de livres par catégorie, récupération de tous les champs dans une liste
de liste de champs par catégorie. Durant ce scrapping l'un des champs scrappé est l'url de l'image du livre. 
A ce moment, le téléchargement de l'image sera effectué, et le fichier sera rangé dans un répertoire Image créé par le 
script, l'image portera le nom du livre (champs titre récupéré en amont. 

Si un téléchargement de l'image est réalisé et que des précédents fichiers sont présents dans le répertoire, les 
précédents fichiers sont effacés et remplacés par les nouveaux.

La liste de liste de champs par catégorie sera utilisée pour écrire le fichier Csv qui portera le nom de la catégorie.csv
Ce fichier Csv sera rangé dans un répertoire Csv créé par le scrapping. Si un fichier du même nom est existant dans le 
répertoire, issu d'un précédent scrapping par exemple, ce précédent fichier sont effacés et remplacé par le nouveau.

Installation et lancement du programme :

1 - travail effectué sous WSL2 : WSL2 est donc nécessaire pour ces lignes de commandes.

Création du répertoire de projet avec la commande mkdir:
Mon_repertoire:~/openclassrooms$ "mkdir projet2Test"

Aller sous le projet  :
Mon_repertoire:~/openclassrooms$ "cd TestProjet2"

Installer virtualenv si nécéssaire :
"pip install virtualenv" 

créer un environnement virtuel avec la commande virtualenv env
Mon_repertoire:~/openclassrooms/TestProjet2$ "virtualenv env"

Activer l'environnement virtuel avec la commande "source env/bin/activate"
(env) Mon_repertoire:~/openclassrooms/TestProjet2$

Récupération du programme via le lien ci dessous.
https://github.com/LioExpleo/Projet_2.git

Mettre les 4 fichiers *.py sous le répertoire que l'on vient de créer.

Lancer la commande "pip install -r requirements.txt" pour installer les packages nécessaires.

Lancer la commande "python3 ScriptMaster.py"

Les données seront générées sous deux répertoires sous le répertoire créé en amont :
  - Csv
  - Image
