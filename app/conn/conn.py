import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='sebangsa',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)