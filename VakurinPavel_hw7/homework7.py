import sqlite3


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_products(connection, products):
    sql = '''INSERT INTO products
    (product_title, price, quantity)
    VALUES (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_products_quantity(connection, products):
    sql = '''UPDATE products SET quantity = ?
    WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_products_price(connection, products):
    sql = '''UPDATE products SET price = ?
    WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def delete_product(connection, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(connection):
    sql = '''SELECT * FROM products'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_by_limit(connection):
    sql = '''SELECT * FROM products 
    WHERE price <= 100 AND quantity > 5'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)


def search_product(connection, name):
    sql = '''SELECT * FROM products 
    WHERE product_title LIKE ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, ('%' + name + '%',))
        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)


sql_to_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
product_title VARCHAR(200) NOT NULL,
price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0
)
'''

connection = create_connection('''hw.db''')
if connection is not None:
    print('Successfully connected!')
    # create_table(connection, sql_to_create_products_table)
    # insert_products(connection, ('Surfskate Carver', 200, 20))
    # insert_products(connection, ('Snowboard Burton', 700, 5))
    # insert_products(connection, ('Surfskate YOW', 250, 50))
    # insert_products(connection, ('Snowboard Salomon', 400, 15))
    # insert_products(connection, ('Action Camera GoPro', 250, 35))
    # insert_products(connection, ('Gloves Dakine', 50, 40))
    # insert_products(connection, ('Vans Slip-on', 60, 13))
    # insert_products(connection, ('Wakeboard Liquid-Force', 499, 19))
    # insert_products(connection, ('Surfboard Maverick', 800, 31))
    # insert_products(connection, ('Bag Dakine', 150, 13))
    # insert_products(connection, ('Snowboard Boots Forum', 200, 20))
    # insert_products(connection, ('Snowboard Bindings Union', 250, 11))
    # insert_products(connection, ('Wakeboard Bindings RipCurl', 130, 17))
    # insert_products(connection, ('Motorcycle BMW CafeRacer', 4000, 1))
    # insert_products(connection, ('Glasses Oakley A-Frame', 190, 14))
    #
    # update_products_quantity(connection, (5, 1))
    # update_products_price(connection, (200, 1))
    # delete_product(connection, 14)
    # select_all_products(connection)
    # select_products_by_limit(connection)
    # search_product(connection, 'Surfboard')
    connection.close()
