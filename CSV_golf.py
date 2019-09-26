
import csv

def csv_exist(nom_fichier):
    try:
        f = open(nom_fichier, 'r', newline='')
        return True
    except :
        return False
        

def inserer(nom_fichier, liste_valeur):
    with open(nom_fichier, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(liste_valeur)


    
    

