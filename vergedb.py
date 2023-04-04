import sqlite3
from sqlite3 import Error

db_name = 'vergeinfo.db'
def create_db_conn():
    connection = None
    try:
        connection = sqlite3.connect(db_name)
        print('databse connected..')
    except Error as e:
        print('Error: ',e)

    return connection

conn = create_db_conn()

def create_table():
    # create a table if not exists
    
    query = '''
        create table if not exists articles (
        id integer primary key autoincrement not null,
        header text not null,
        url varchar(255) not null,
        author varchar(255) not null,
        date varchar(255) not null
        ); 
    '''
    conn.execute(query)
    conn.commit()
    print('created table..')

def insert_article(headline,link,author,date):
    insert_query = """insert into articles(header,url,author,date) values(?,?,?,?)"""
    conn.execute(insert_query,(headline,link,author,date))
    conn.commit()

def display_articles():
    cursor = conn.cursor()
    cursor.execute('select * from articles')
    result = cursor.fetchall()
    print(result)
    conn.close()