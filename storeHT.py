import mysql.connector
from mysql.connector import errorcode
import datetime

class dbtemps:
    print('entering class')
    def __init__(self):
#        print('init')
        self.conn = self.create_conn()
        self.cur = self.conn.cursor()

    def create_conn(self):
#        print('create_conn')
        config = {
            'user': 'pi0a',
            'password': '37Sunset',
            'host': 'kermit',
            'db': 'temps',
            'raise_on_warnings': True,
        }

        try:
            cnx = mysql.connector.connect(**config)
#            print('trying conn')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            return
        else:
            print('CONNECTED!!!')
            return cnx

    def write_temp(self, h, t):
        try:
            sql= """INSERT INTO temps (idloc, temp, humidity, time, idunit, iddev) VALUES('{}', '{}', '{}', '{}', '7', '2');""".format(13, t, h, datetime.datetime.now())
            print(sql)
            self.cur.execute(sql)
            self.conn.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err.errno)
