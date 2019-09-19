import pymysql.cursors  
 
# La fonction renvoie une connexion.
def getConnection():

    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',                             
                                 db='roc',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    print ("connected")
    return connection
