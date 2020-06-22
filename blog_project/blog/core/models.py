import pymysql.cursors
from datetime import datetime

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
        sql = """create table if not exists blogs(
            id int(11) unsigned AUTO_INCREMENT PRIMARY KEY,
            title varchar(255) NOT NULL,
            description text NOT NULL,
            owner_name varchar(50) NOT NULL,
            image varchar(500),
            created_at datetime NOT NULL,
            is_published tinyint(1) default 1
            ); 
            """
        cursor.execute(sql)
    connection.commit()

def create_blog(title, description, owner_name, image, is_published=True):
    with connection.cursor() as cursor:
        # Create a new record
        sql = """insert into blog_project.blogs(title, description, owner_name, image, created_at, is_published)
            values(%s, %s, %s, %s, %s, %s) 
            """
        now = datetime.now()
        created_ad = now.strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(sql, (title, description, owner_name, image, created_ad, is_published))
    connection.commit()

def all_blogs():
    with connection.cursor() as cursor:
        # Create a new record
        sql = """select * from blog_project.blogs;"""
        cursor.execute(sql,)
    return cursor.fetchall()


create_blog_table()