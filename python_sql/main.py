import pymysql.cursors
from datetime import datetime


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123',
                             db='test_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = '''create table if not exists test_db.bot (
            id int unsigned AUTO_INCREMENT PRIMARY KEY,
            question varchar(255) NOT NULL,
            answer varchar(255) NOT NULL,
            created_at datetime NOT NULL,
            updated_at datetime NOT NULL,
            INDEX (id, question)
            ) CHARACTER SET utf8 COLLATE utf8_general_ci;
        '''
        cursor.execute(sql)

    connection.commit()
    print('table yaradildi! ')
    question = input('Daxil etmek istediyiniz suali yazin: ')
    answer = input('Daxil etmek istediyiniz cavabi yazin: ')
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with connection.cursor() as cursor:
        sql = "INSERT INTO test_db.bot (question, answer, created_at, updated_at) VALUES (%s, %s, %s, %s);"
        cursor.execute(sql, (question, answer, current_time, current_time))

    connection.commit()
    print('melumatlar elave edildi! ')

    with connection.cursor() as cursor:
        sql = f"SELECT * FROM test_db.bot WHERE id=1"
        cursor.execute(sql)
        result = cursor.fetchone()
        print('elave edilen melumat:', result)

    with connection.cursor() as cursor:
        sql = f"SELECT * FROM test_db.bot;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print('butun melumatlar', result)
        for data in result:
            print(data['question'], data['created_at'])

finally:
    connection.close()
