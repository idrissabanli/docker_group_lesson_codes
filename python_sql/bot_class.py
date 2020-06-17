import pymysql.cursors
from datetime import datetime

class Bot():
    ids = []
    connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='123',
                                    db='test_db',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

    def __init__(self):        
        with self.connection.cursor() as cursor:
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
        self.connection.commit()

    def create(self, question, answer):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO test_db.bot (question, answer, created_at, updated_at) VALUES (%s, %s, %s, %s);"
            cursor.execute(sql, (question, answer, current_time, current_time))

        self.connection.commit()
        print('melumatlar elave edildi! ')

    def get(self, **kwargs):
        result = None
        with self.connection.cursor() as cursor:
            query = 'where'
            for key, value in kwargs.items():
                query += ' {key}=%s'.format(key=key)
            sql = f"SELECT * FROM test_db.bot {query}"
            cursor.execute(sql, tuple(kwargs.values()))
            result = cursor.fetchone()
        return result

    def all(self):
        with self.connection.cursor() as cursor:
            sql = f"SELECT * FROM test_db.bot;"
            cursor.execute(sql)
            return cursor.fetchall()

    @classmethod
    def filter(cls, **kwargs):
        result = None
        with cls.connection.cursor() as cursor:
            query = 'where'
            for key, value in kwargs.items():
                query += ' {key}=%s'.format(key=key)
            sql = f"SELECT * FROM test_db.bot {query}"
            cursor.execute(sql, tuple(kwargs.values()))
            result= cursor.fetchall()
            cls.ids = [item['id'] for item in result]
        return result

    @classmethod
    def update(cls, **kwargs):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = ''
        for key, value in kwargs.items():
            query += ' {key}=%s,'.format(key=key)

        for data_id in cls.ids:
            with cls.connection.cursor() as cursor:
                sql = f"UPDATE test_db.bot SET {query}"[:-1]
                sql += f'where id={data_id}'
                # "update test.bot set question='salam', answer='sagol'"
                cursor.execute(sql, tuple(kwargs.values()))

        cls.connection.commit()
        print('melumatlar deyisdirildi ')
            

if __name__ == '__main__':
    Bot.filter(id=2)
    Bot.update(question='salam')
    