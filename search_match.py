from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd

# Charger les données à partir des fichiers Excel
df1 = pd.read_excel("tableau1.xlsx")
df2 = pd.read_excel("tableau2.xlsx")

# Fonction pour trouver le meilleur match dans le tableau 2 et mettre à jour le login dans le tableau 1
def trouver_meilleur_match(nom_prenom):
    meilleur_match = process.extractOne(nom_prenom, df2['nom_prenom'], scorer=fuzz.token_sort_ratio)
    idx_match = df2.index[df2['nom_prenom'] == meilleur_match[0]][0]
    login = df2.loc[idx_match, 'login']
    return login

# Mettre à jour les logins dans le tableau 1
df1['login'] = df1['nom_prenom'].apply(trouver_meilleur_match)

# Enregistrer les résultats dans un nouveau fichier Excel
df1.to_excel("resultats.xlsx", index=False)

print("Les résultats ont été enregistrés dans 'resultats.xlsx'")
