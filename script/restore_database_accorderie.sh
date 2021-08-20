#!/usr/bin/env bash

echo "Create database and user"
sudo mysql -u root << EOF
DROP DATABASE IF EXISTS accorderie_log_2019;
CREATE USER IF NOT EXISTS 'accorderie'@'localhost' IDENTIFIED BY 'accorderie';
GRANT ALL PRIVILEGES ON *.* TO 'accorderie'@'localhost' IDENTIFIED BY 'accorderie';
FLUSH PRIVILEGES;
CREATE DATABASE accorderie_log_2019;
EOF

echo "Fix SQL file"
sed -i "s/'0000-00-00'/NULL/g" /accorderie_canada/Intranet/accorder_AccorderieIntranet_20200826.sql

echo "Import SQL file"
mysql -u accorderie -paccorderie accorderie_log_2019 < /accorderie_canada/Intranet/accorder_AccorderieIntranet_20200826.sql

echo "Fix SQL in database"
./.venv/bin/python ./addons/TechnoLibre_odoo_accorderie/script/fix_database.py
