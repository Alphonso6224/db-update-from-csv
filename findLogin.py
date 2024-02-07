import pandas as pd
from sqlalchemy import create_engine, inspect, select, text, bindparam, MetaData, Table
import mysql.connector

#   Fonction pour séparer le nom et le prénom
def separate_nom_prenom(_nom_complet):
    mots = _nom_complet.split(" ")
    prenom = ' '.join(mots[:-1])
    nom = mots[-1]
    return prenom, nom

# Charger le fichier CSV
df_csv = pd.read_csv('ldap_data.csv', header=None, names=['login', 'prenom&nom'])

#   Diviser la colonne prenom et nom
df_csv[['prenom', 'nom']] = df_csv['prenom&nom'].apply(lambda x: pd.Series(separate_nom_prenom(x)))

#   Créer un DataFrame pour stocker les correspondances trouvées
correspondances = []

try: 
    
    # Etablir la connexion
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="user",
        password="password",
        database="database"
    )
    
    print("Connexion à la base de données réussie ! ")
    
    
    #   Créer un curseur pour exécuter les requêtes SQL
    mycursor = mydb.cursor()

    #   Parcourir chaque ligne du fichier csv
    for index, row in df_csv.iterrows():
        #   Requête sql pour récupérer les employés dont le nom correspond
        query = "SELECT nom, prenom, matricule_definitif, old_matricule FROM employes WHERE nom = %s"

        
        # Exécuter la requête sql
        mycursor.execute(query, (row['nom'],))  # Utilisation d'un paramètre de requête pour le nom
    
        # Récupérer les résultats
        employes = mycursor.fetchall()
        
        # Initialiser une variable pour suivre si une correspondance a été trouvée
        correspondance_trouvee = False
        
        #   Afficher les résultats
        for employe in employes:
            #   Vérifier si le prénom est inclus 
            if row['prenom'] in employe[1]: # Utilisation de l'indice pour le prénom
                #   Correspondance trouvée
                #   Ajouter la correspondance trouvée au DataFrame
                correspondances.append({'Nom': employe[0], 'Prenom': employe[1], 'Matricule': employe[2], 'Login': row['login']})
                correspondance_trouvee = True
                break  #    Sortir de la boucle si une correspondance a été trouvée
        
        #   Si aucune correspondance n'a été trouvée, ajouter le login à la liste des logins non correspondants
        if not correspondance_trouvee:
            correspondances.append({'Nom': row['nom'], 'Prenom': row['prenom'], 'Matricule': None, 'Login': row['login']})      
    
    #   Fermer le curseur 
    mycursor.close()
    
    #   Créer un DataFrame à partir des correspondances trouvées
    df_correspondances = pd.DataFrame(correspondances)
    
    #   Filtrer les entrées avec un matricule renseigné
    df_matricule_renseigne = df_correspondances.dropna(subset=['Matricule'])
    
    #   Sauvegarder le DataFrame des corresponcance avec un matricules renseigné au format Excel
    df_matricule_renseigne.to_excel('correspondance_matricule_renseigne.xlsx', index=False)
    
    #   Sauvegarder le DataFrame au format Excel
    df_correspondances.to_excel('correspondances.xlsx', index=False)
    
    #   Sauvegarder les logins non correspondants dans un nouveau fichier excel
    df_non_correspondants = df_correspondances[df_correspondances['Matricule'].isnull()]
    df_non_correspondants.to_excel('logins_non_correspondants.xlsx', index=False)  
    
    #   Fermer la connexion
    mydb.close()
except Exception as e:
    print("Erreur lors de la connexion à la base données:", e)