import csv
import mysql.connector
import os
import time

class DatabaseUpdater:
    """Une classe pour mettre à jour une base de données MySQL à partir d'un fichier CSV.
    """
    def __init__(self, csv_file, host, username, password, database):
        """Initialise la classe avec  le chemin vers le fichier CSV

        Args:
            csv_file (str): Le chemin vers le fichier CSV
            host (str): L'adresse IP ou le n om d'hôte du serveur MySQL.
            username (str): Le nom d'utilisateur pour se connecter à MySQL.
            password (str): Le mot de passe pour se connecter à MySQL
            database (str): Le nom de la base de donnée à laquelle se connecter
        """
        self.csv_file = csv_file
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        
    def connect_to_mysql(self):
        """
        Etablit une connexion à la base de données MySQL.
        
        Returns:
            obj: L'objet de connexion MySQL.
        """
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database
            )
            print("Super soldat, la connexion à la base de données est réussie. 😄")
            return conn
        except mysql.connector.Error as err:
            print("Erreur lors de la connexion à MySQL: ", err)
            return None
        
    def update_database_from_csv(self):
        """
        Met à jour la base de données MySQL à partir du fichier CSV
        """
        start_time = time.time()
        
        # Connexion à la base de données
        conn = self.connect_to_mysql()
        if conn is None:
            return
        
        try:
            with open(self.csv_file, 'r', encoding='iso-8859-1') as file:
                csv_reader = csv.DictReader(file, delimiter=';')
                cursor = conn.cursor()
                batch_size = 1000 # Nombre de mises à jour par lot
                count = 0
                nombre_de_mise_a_jour = 0
                updates = []
                
                for row in csv_reader:
                    id_employe = row['id']
                    new_login = row['login']
                    updates.append((new_login, id_employe))
                    count += 1
                    nombre_de_mise_a_jour += 1
                    
                    # Si le nombre de mises à jour atteirt le batch_size, exécuter la mise à jour par lot
                    if count % batch_size == 0:
                        self._update_batch(cursor, updates)
                        updates = []
                        count = 0  # Réinitialisation du compteur après chaque lot de mises à jour
                        
                # Exécuter les mises à jour restantes qui n'ont pas atteint le batch_size
                if updates:
                    self._update_batch(cursor, updates)
                    
                conn.commit()
                print("Mise à jour  terminée. ✅")
                end_time = time.time()
                execution_time = end_time - start_time
                print("Temps d'exéction du script :", execution_time, "secondes pour", nombre_de_mise_a_jour, "mise à jour")
        except FileNotFoundError:
            print("Le fichier CSV spécifé est introuvable.")
        except Exception as e:
            print("Une erreur s'est produite lors de la mise à jour de la base de donnée: ", e)
            conn.rollback()
        finally:
            if conn is not None:
                conn.close()
                
    def _update_batch(self, cursor, updates):
        """Effectue des mises à jour par lot dans la base de données.

        Args:
            cursor: L'objet curseur pour exécter les requêtes SQL.
            updates (list): Listes de tuples (nouveau_login, id_employe) pour les mises à jour.
        """
        query = "UPDATE employes SET login = %s WHERE id = %s"
        cursor.executemany(query, updates)
        
if __name__ == "__main__":
    # Chemin vers le fichier CSV
    csv_file = 'login_map.csv'
    
    # Paramètres de connexion à la base de données MySQL
    host="127.0.0.1"
    username="wip"
    password="wip"
    database="wipdb"
    
    updater =DatabaseUpdater(csv_file, host, username, password, database)
    updater.update_database_from_csv()