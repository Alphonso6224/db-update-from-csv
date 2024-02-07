---

# Mise à jour des logins dans une base de données MySQL à partir d'un fichier CSV

Ce script Python permet de mettre à jour les logins dans une base de données MySQL en utilisant les données d'un fichier CSV.

## Description

Le script lit un fichier CSV contenant des informations sur les employés, notamment leur identifiant et leur nouveau login. Il utilise ces données pour mettre à jour les logins correspondants dans une table de la base de données MySQL.

## Prérequis

Avant d'exécuter le script, assurez-vous d'installer les bibliothèques Python nécessaires en exécutant :

```bash
pip install pandas mysql-connector-python
```

## Utilisation

1. Assurez-vous que vos données sont correctement organisées dans le fichier CSV. Le fichier CSV doit contenir une colonne `id` pour les identifiants des employés et une colonne `login` pour les nouveaux logins.

2. Assurez-vous que votre base de données MySQL est accessible et que vous avez les autorisations nécessaires pour vous y connecter.

3. Modifiez les paramètres de connexion à la base de données MySQL dans le script selon vos besoins :

   ```python
   host = "127.0.0.1"  # L'adresse IP ou le nom d'hôte du serveur MySQL.
   username = "votre_nom_utilisateur"  # Le nom d'utilisateur pour se connecter à MySQL.
   password = "votre_mot_de_passe"  # Le mot de passe pour se connecter à MySQL.
   database = "votre_base_de_donnees"  # Le nom de la base de données à laquelle se connecter.
   ```

4. Exécutez le script en utilisant la commande suivante :

   ```bash
   python script.py
   ```

5. Après l'exécution, le script mettra à jour les logins dans la base de données MySQL en utilisant les données du fichier CSV et affichera un message indiquant que la mise à jour est terminée.

## Notes

- Assurez-vous que les informations de connexion à la base de données sont correctement configurées dans le script avant de l'exécuter.

- Ce script utilise la bibliothèque pandas pour lire le fichier CSV et la bibliothèque mysql-connector-python pour se connecter à la base de données MySQL.

---