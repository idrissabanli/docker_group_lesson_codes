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
            user_id int(11) unsigned NOT NULL,
            image varchar(500),
            created_at datetime NOT NULL,
            is_published tinyint(1) default 1,
            INDEX (id, user_id),
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE
            ); 
            """
        cursor.execute(sql)
    connection.commit()

def create_blog(title, description, user_id, image, is_published=True, **kwargs):
    with connection.cursor() as cursor:
        # Create a new record
        sql = """insert into blog_project.blogs(title, description, user_id, image, created_at, is_published)
            values(%s, %s, %s, %s, %s, %s) 
            """
        now = datetime.now()
        created_ad = now.strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(sql, (title, description, user_id, image, created_ad, is_published))
    connection.commit()

def all_blogs(limit_f_index=None, limit_s_index=None):
    limit_query = ''
    if limit_f_index is not None and limit_s_index is not None:
        limit_query = f'LIMIT {limit_f_index}, {limit_s_index}'

    with connection.cursor() as cursor:
        # Create a new record
        sql = f"""select * from blog_project.blogs {limit_query};"""
        cursor.execute(sql,)
    return cursor.fetchall()

def get_blog_user_details(blog_id):
    with connection.cursor() as cursor:
        # Create a new record
        sql = """select users.first_name, users.surname from blogs 
            INNER JOIN users on users.id = blogs.user_id where blogs.id =  %s
        """
        cursor.execute(sql, blog_id)
    return cursor.fetchone()

def get_blogs_count():
    with connection.cursor() as cursor:
        # Create a new record
        sql = """select count(id) from blogs"""
        cursor.execute(sql)
    return cursor.fetchone()['count(id)']


create_blog_table()