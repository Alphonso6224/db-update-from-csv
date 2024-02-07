---

# Mise à jour des logins à partir d'une base de données MySQL

Ce script Python permet de mettre à jour les logins à partir d'un fichier CSV en recherchant des correspondances dans une base de données MySQL.

## Description

Le script lit un fichier CSV contenant des logins et des noms/prénoms d'employés, puis recherche des correspondances dans une table de la base de données MySQL. Pour chaque login trouvé dans la base de données, le script ajoute le nom, le prénom et le matricule de l'employé associé au login dans un fichier Excel de correspondances.

## Prérequis

Avant d'exécuter le script, assurez-vous d'installer les bibliothèques Python nécessaires en exécutant :

```bash
pip install pandas mysql-connector-python
```

## Utilisation

1. Assurez-vous que vos données sont correctement organisées dans le fichier CSV. Le fichier CSV doit contenir une colonne `login` pour les logins et une colonne `prenom&nom` pour les noms/prénoms des employés.

2. Assurez-vous que votre base de données MySQL est accessible et que vous avez les autorisations nécessaires pour vous y connecter.

3. Exécutez le script en utilisant la commande suivante :

```bash
python script.py
```

4. Après l'exécution, trois fichiers Excel seront générés :
   - `correspondance_matricule_renseigne.xlsx` : Contient les correspondances trouvées avec les matricules renseignés.
   - `correspondances.xlsx` : Contient toutes les correspondances trouvées.
   - `logins_non_correspondants.xlsx` : Contient les logins pour lesquels aucune correspondance n'a été trouvée dans la base de données.

## Notes

- Assurez-vous que les informations de connexion à la base de données sont correctement configurées dans le script avant de l'exécuter.

- Ce script utilise la bibliothèque Pandas pour manipuler les données tabulaires et la bibliothèque mysql-connector-python pour se connecter à la base de données MySQL.

---