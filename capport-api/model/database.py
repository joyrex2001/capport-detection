import mysql.connector
import os

TABLES = {}
TABLES['session'] = (
    "CREATE TABLE IF NOT EXISTS `session` ("
    "  `uuid` varchar(64),"
    "  `identity` varchar(64),"
    "  `expire` int(11),"
    "  `datalimit` int(11),"
    "  PRIMARY KEY (`uuid`)"
    ") ENGINE=InnoDB")

TABLES['requirement'] = (
    "CREATE TABLE IF NOT EXISTS `requirement` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `uuid` varchar(64),"
    "  `type` varchar(64),"
    "  `url` text,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")


def getCnx():
    cnx = mysql.connector.connect(
        user=os.getenv("MYSQL_USER","capport"),
        password=os.getenv("MYSQL_PASSWORD","capport"),
        host=os.getenv("MYSQL_HOST","127.0.0.1"),
        database=os.getenv("MYSQL_DATABASE","capport") )
    return cnx

def initDatabase():
    cnx = getCnx()
    cursor = cnx.cursor()
    for name, ddl in TABLES.iteritems():
        cursor.execute(ddl)
    cursor.close()
    cnx.close()
    return
