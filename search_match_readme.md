---

# Mise à jour des logins à partir de correspondances floues

Ce script Python utilise la bibliothèque FuzzyWuzzy pour trouver les meilleurs matchs entre les noms/prénoms dans deux fichiers Excel et mettre à jour les logins en conséquence.

## Description

Le script prend en entrée deux fichiers Excel, `tableau1.xlsx` et `tableau2.xlsx`, qui contiennent des données sur les employés. Il cherche à mettre à jour les logins dans `tableau1.xlsx` en trouvant les meilleures correspondances pour les noms/prénoms dans `tableau2.xlsx`.

## Prérequis

Avant d'exécuter le script, assurez-vous d'installer les bibliothèques Python nécessaires en exécutant :

```bash
pip install pandas fuzzywuzzy
```

## Utilisation

1. Assurez-vous que vos données sont correctement organisées dans les fichiers Excel. Les fichiers doivent contenir une colonne `nom_prenom` pour les noms/prénoms des employés et une colonne `login` pour les logins.

2. Placez vos fichiers Excel `tableau1.xlsx` et `tableau2.xlsx` dans le même répertoire que le script.

3. Exécutez le script en utilisant la commande suivante :

```bash
python script.py
```

4. Après l'exécution, les résultats seront enregistrés dans un nouveau fichier Excel appelé `resultats.xlsx` dans le même répertoire que le script.

## Notes

- Si aucun match n'est trouvé pour un nom/prénom dans `tableau2.xlsx`, le login correspondant dans `tableau1.xlsx` restera inchangé.

- La bibliothèque FuzzyWuzzy est utilisée pour trouver des correspondances floues entre les noms/prénoms, ce qui peut être utile pour traiter des données avec des erreurs typographiques ou des variations mineures dans les noms/prénoms.

---