import pymysql

database = "accorderie_log_2019"
host = "localhost"
port = 3306
user = "accorderie"
password = "accorderie"
schema = "public"

conn = pymysql.connect(
    db=database, host=host, port=port, user=user, password=password
)

cr = conn.cursor()

# Fix date with string "0000-00-00"

# cr.execute("SET sql_mode = 'NO_ZERO_DATE';")
# cr.execute("SET sql_mode = 'NO_ZERO_IN_DATE';")

# query_search = """SELECT *
# FROM tbl_demande_service
# WHERE DateFin = "0000-00-00"
# """
#
# cr.execute(query_search)
# old_v = cr.fetchall()
#
# query = """UPDATE `tbl_demande_service`
# SET DateFin = NULL
# WHERE DateFin = "0000-00-00"
# """
#
# v = cr.execute(query)

# Fix tbl_echange_service NbHeure, transform time to float
query_search = """ALTER TABLE tbl_echange_service modify NbHeure float null;"""
cr.execute(query_search)

# Fix field for foreign key
query_search = """
ALTER TABLE tbl_arrondissement
MODIFY NoVille int unsigned null;
"""
cr.execute(query_search)

# Arrondissement
try:
    query_search = """
    ALTER TABLE tbl_arrondissement
    DROP FOREIGN KEY foreign_key_tbl_ville_noville;
    """
    cr.execute(query_search)
except Exception:
    pass

query_search = """
ALTER TABLE tbl_arrondissement
ADD CONSTRAINT foreign_key_tbl_ville_noville
FOREIGN KEY (NoVille) REFERENCES tbl_ville(NoVille)
on update set null on delete set null;
"""
cr.execute(query_search)

# Cartier
try:
    query_search = """
    ALTER TABLE tbl_cartier
    DROP FOREIGN KEY tbl_cartier_tbl_arrondissement_NoArrondissement_fk;
    """
    cr.execute(query_search)
except Exception:
    pass

query_search = """
ALTER TABLE tbl_cartier
ADD CONSTRAINT foreign_key_tbl_arrondissement_noarrondissement
FOREIGN KEY (NoArrondissement) REFERENCES tbl_arrondissement(NoArrondissement);
"""
cr.execute(query_search)

# Ville
try:
    query_search = """
    ALTER TABLE tbl_ville
    DROP FOREIGN KEY foreign_key_tbl_region_noregion;
    """
    cr.execute(query_search)
except Exception:
    pass

query_search = """
ALTER TABLE tbl_ville
ADD CONSTRAINT foreign_key_tbl_region_noregion
FOREIGN KEY (NoRegion) REFERENCES tbl_region(NoRegion)
on update set null on delete set null;
"""
cr.execute(query_search)

# lst_echange_service = cr.fetchall()
# query_search = """SELECT *
# FROM tbl_echange_service
# """
#
# cr.execute(query_search)
# lst_echange_service = cr.fetchall()

cr.close()
