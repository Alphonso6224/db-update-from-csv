const fs = require('fs');
const csv = require('csv-parser');
const mysql = require('mysql');

// Créer une connexion à la base de données
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'wip',
    password: 'wip',
    database: 'wipdb'
});

// Se connecter à la base de données
connection.connect();

// Lire le fichier csv
fs.createReadStream('ldap_data.csv')
    .pipe(csv())
    .on('data', (row) => {
        
    })