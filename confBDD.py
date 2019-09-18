import pymysql.cursors  
 
# La fonction renvoie une connexion.
def getConnection():
     
    # Vous pouvez changer les arguments de la connexion.
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',                             
                                 db='mysql',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
