import os #J'importe la librairie os

os.getcwd() #Je donne le dossier actuel
folder = os.listdir(os.getcwd()) #Je donne tous les fichiers dans le dossier actuel 

def archive():  
    for repertoire in os.listdir('/Users/mxns0ur/Desktop/Python/Repertoire/ARCHIVE') : #Je créer une boucle for afin de lister les fichiers du dossier ARCHIVE
        print(str(repertoire) + " - Traité") #J'affiche les fichiers du dossier ARCHIVE en ajoutant la phrase "Traité"
    
def rejected() :
    for repertoire in os.listdir('/Users/mxns0ur/Desktop/Python/Repertoire/REJECTED') : #Je créer une boucle for afin de lister les fichiers du dossier REJECTED
        print(str(repertoire) + " - Non traité ") #J'affiche les fichiers du dossier REJECTED en ajoutant la phrase "Non Traité" 
        
def all() : #Je créer cette fonction afin de rassembler mes deux dernieres fonctions
    archive() 
    rejected()
    
def readarchive(): #Je créer une fonction afin de lire le contenu de tous les fichiers
    
    for i in os.listdir('/Users/mxns0ur/Desktop/Python/Repertoire/ARCHIVE') : #Je créer une boucle for qui va me permettre de lire le contenu de chaque fichier qui ne se termine pas par ".py"
        
        if i.endswith(".py") : # Je créer une condition qui stipule de ne pas lire les fichiers de format ".py" afin de ne pas causer de problèmes au programme
            pass
        else :
            try : #J'utilise "try" afin d'éviter une erreur au programme
                with open(i, 'r') as f:
                    fichier = f.read()
                    print("#########################")
                    print(fichier)
            except Exception as e : #J'utilise "except" afin de créer une exception aux erreurs si il y en a et "Exception" afin d'afficher les erreurs si il y en a 
                print(e)
                
def readline(): #Je créer une fonction afin de lire ligne par ligne le contenu de chaque fichiers
    filepath = '/Users/mxns0ur/Desktop/Python/Repertoire/ARCHIVE/mail2.txt'
    with open(filepath, 'r') as f :  
        ligne = f.readline()
        a = 1
        while ligne : #Je créer une boucle while afin de de lire ligne par ligne le contenu de chaque fichiers
            print("Ligne : "+ str(a) + " : " + ligne.strip())
            a += 1
            ligne = f.readline()

