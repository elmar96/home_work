import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


# add products(create_table)
def create_table(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
        c.close()
    except Error as e:
        print(e)


def insert_products(conn, products):
    try:
        sql = '''INSERT INTO products (product_title, price, quantity) 
        VALUES (?, ?, ?)'''
        c = conn.cursor()
        c.execute(sql, products)
        conn.commit()
        c.close()
    except Error as e:
        print(e)


def update_products_price(conn, price, id):
    try:
        sql = '''UPDATE products set price=? where id= ?'''
        c = conn.cursor()
        c.execute(sql, (price, id))
        conn.commit()
        c.close()
    except Error as e:
        print(e)


def update_products_quantity(conn, quantity, id):
    try:
        sql = '''UPDATE products set quantity=? where id= ?'''
        c = conn.cursor()
        c.execute(sql, (quantity, id))
        conn.commit()
        c.close()
    except Error as e:
        print(e)


def delete_products(conn, id):
    try:
        sql = '''delete from products where id = ?'''
        c = conn.cursor()
        c.execute(sql, (id,))
        conn.commit()
        c.close()
    except Error as e:
        print(e)


def sellect_all_products(conn):
    try:
        sql = '''select * from products;'''
        c = conn.cursor()
        c.execute(sql)
        rows = c.fetchall()

        for row in rows:
            print(row)

        c.close()
    except Error as e:
        print(e)


def sellect_all_products(conn):
    try:
        sql = '''select * from products;'''
        c = conn.cursor()
        c.execute(sql)
        rows = c.fetchall()

        for row in rows:
            print(row)

        c.close()
    except Error as e:
        print(e)


def select_all_products_cheaper_and_five_more(conn, price, product_title):
    try:
        sql = '''select * from products where price<=? and product_title>=?;'''
        c = conn.cursor()
        c.execute(sql, (price, product_title))
        rows = c.fetchall()

        for row in rows:
            print(row)

        c.close()
    except Error as e:
        print(e)


def product_name_search(conn):
    try:
        sql = '''SELECT * FROM products WHERE product_title like '%масло%';'''
        c = conn.cursor()
        c.execute(sql)
        rows = c.fetchall()

        for row in rows:
            print(row)

        c.close()
    except Error as e:
        print(e)


database = 'home_work.db'
conn = create_connection(database)
sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10,2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0
)
'''

if conn is not None:
    print('Successfully connected')

    # create_table(conn, sql_create_products_table)
    # insert_products(conn, ('сахар песочный', 90.50, 1))
    # insert_products(conn, ('макарон', 45.8, 1))
    # insert_products(conn, ('круппа манная', 120, 2))
    # insert_products(conn, ('чай черный', 160.80, 1))
    # insert_products(conn, ('чай зеленный', 200, 3))
    # insert_products(conn, ('молоко', 80, 6))
    # insert_products(conn, ('масло подсолнечная', 130, 10))
    # insert_products(conn, ('масло сливочное', 400.45, 15))
    # insert_products(conn, ('сливки', 180.30, 15))
    # insert_products(conn, ('мука пшеничная', 1000, 8))
    # insert_products(conn, ('вода газированная', 29.5, 150))
    # insert_products(conn, ('порошок стиральный', 500, 8))
    # insert_products(conn, ('мыло дегтярное', 40.50, 72))
    # insert_products(conn, ('гель для душа', 250.90, 180))
    # insert_products(conn, ('шампунь', 450, 250))
    # insert_products(conn, ('шампунь ', 200, 300))

    # update_products_price(conn, 155, 8)
    # update_products_quantity(conn, 3, 8)
    # delete_products(conn, 16)
    # sellect_all_products(conn)
    # select_all_products_cheaper_and_five_more(conn,100,5)
    product_name_search(conn)
    conn.close()
