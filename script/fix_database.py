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
query_search = """alter table tbl_echange_service modify NbHeure float null;
"""

cr.execute(query_search)
# lst_echange_service = cr.fetchall()
# query_search = """SELECT *
# FROM tbl_echange_service
# """
#
# cr.execute(query_search)
# lst_echange_service = cr.fetchall()

print(1)

cr.close()
