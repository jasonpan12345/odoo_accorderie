# ERPLibre Accorderie

Module ERPLibre pour les Accorderies du Québec.

## Base de données

Il est considéré pour la migration de l'Accorderie vers la plateforme ERPLibre, qu'il y a une base de donnée accessible localement avec les informations suivantes :

```python
host = "localhost"
user = "accorderie"
passwd = "accorderie"
db_name = "accorderie_log_2019"
port = 3306
```

### Restoration d'une base de données

Créer une base de donnée

```bash
# Log into mysql
mysql -u root
```

```sql
-- Create new database user
CREATE USER 'accorderie'@'localhost' IDENTIFIED BY 'accorderie';
GRANT ALL PRIVILEGES ON *.* TO 'accorderie'@'localhost' IDENTIFIED BY 'accorderie';
FLUSH PRIVILEGES;
CREATE DATABASE accorderie_log_2019;
-- Log out
```

Restorer le fichier SQL de la dernière sauvegarde. Assurez-vous que dans le fichier sql, il n'ait pas de commande `USE` d'une base de donnée particulière.

```bash
# Log into mysql
mysql -u accorderie -p accorderie_log_2019 < FICHIER_SQL.sql
```

### Création de modules ERPLibre à partir du générateur de code

À la racine du projet, installer le module de génération de module à partir de base de données :
```bash
./script/db_restore.py --database accorderie
./script/addons/install_addons_dev.sh accorderie code_generator_db_servers
```
