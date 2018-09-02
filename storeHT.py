import mysql.connector
from mysql.connector import errorcode

class dbtemps:
    print('entering class')
    def __init__(self):
        print('init')
        self.conn = self.create_conn()
        self.cur = self.conn.cursor()

    def create_conn(self):
        print('create_conn')
        config = {
            'user': 'dmontysql',
            'password': 'sun37rIse',
            'host': 'kermit',
            'db': 'temps',
            'raise_on_warnings': True,
        }

        try:
            cnx = mysql.connector.connect(**config)
            print('trying conn')
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
