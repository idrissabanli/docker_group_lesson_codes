import pymysql.cursors
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash 

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123',
                             db='blog_project',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def create_blog_table():
    with connection.cursor() as cursor:
        # Create a new record
        sql = """create table if not exists users(
            id int(11) unsigned AUTO_INCREMENT PRIMARY KEY,
            username varchar(50) NOT NULL UNIQUE,
            email varchar(40) NOT NULL UNIQUE,
            first_name varchar(40) NOT NULL,
            surname varchar(40) NOT NULL,
            password varchar(255) NOT NULL,
            date_joined datetime NOT NULL,
            is_active tinyint(1) default 0
            );
            """
        cursor.execute(sql)
    connection.commit()


def create_user(username, email, first_name, surname, password, is_active=1, **kwargs):
    hashed_pass = generate_password_hash(password)
    with connection.cursor() as cursor:
        # Create a new record
        sql = """INSERT INTO users(username, email, first_name, surname, password, date_joined, is_active)
            VALUES(%s, %s, %s, %s, %s, %s, %s);
        """
        now = datetime.now()
        date_joined = now.strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(sql, (username, email, first_name, surname, hashed_pass, date_joined, is_active))
    connection.commit()

def check_user_username(username):
    finded_user = None
    with connection.cursor() as cursor:
        sql = 'select * from users where users.username=%s'
        cursor.execute(sql, username)
        finded_user = cursor.fetchone()
    return finded_user

def check_user_email(email):
    finded_user = None
    with connection.cursor() as cursor:
        sql = 'select * from users where users.email=%s'
        cursor.execute(sql, email)
        finded_user = cursor.fetchone()
    return finded_user

def get_user(user_id):
    finded_user = None
    with connection.cursor() as cursor:
        sql = 'select * from users where users.id=%s'
        cursor.execute(sql, user_id)
        finded_user = cursor.fetchone()
    return finded_user

def check_user(username, password):
    finded_user = None
    user = check_user_username(username)
    if user:
        pwhash = user['password'] 
        if check_password_hash(pwhash, password):
            finded_user = user
    return finded_user

create_blog_table()
