import mysql.connector as sql


class DBPropertyUt:
    @staticmethod
    def getParameter():
        host = 'localhost'
        database = 'ecommercewebservice'
        user = 'root'
        password = '9392951228'
        return host, database, user, password


class DBConnectivity:
    @staticmethod
    def makeConnection():
        l = DBPropertyUt.getParameter()
        conn = sql.connect(host=l[0], database=l[1], user=l[2], password=l[3])
        if conn.is_connected:
            print('DB is connected: ')


DBConnectivity.makeConnection()
