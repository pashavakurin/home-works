import sqlite3


def create_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()  # Не забываем подтвердить изменения в базе данных
    except sqlite3.Error as e:
        print(e)


def insert_countries(connection, title):
    sql = '''INSERT INTO countries
    (title)
    VALUES (?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (title,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def insert_cities(connection, title, area, country_id):
    sql = '''INSERT INTO cities
    (title, area, country_id)
    VALUES (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (title, area, country_id))
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def insert_employees(connection, first_name, last_name, city_id):
    sql = '''INSERT INTO employees 
    (first_name, last_name, city_id)
    VALUES(?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (first_name, last_name, city_id))
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def display_cities(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    for city in cities:
        print(f"{city[0]}. {city[1]}")


def display_employees(connection, city_id):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT employees.first_name, employees.last_name, countries.title, cities.title, cities.area
        FROM employees
        JOIN cities ON employees.city_id = cities.id
        JOIN countries ON cities.country_id = countries.id
        WHERE employees.city_id = ?
    """, (city_id,))
    employees = cursor.fetchall()
    for employee in employees:
        print(
            f"Имя: {employee[0]}, Фамилия: {employee[1]}, Страна: {employee[2]}, Город: {employee[3]}, Площадь города: {employee[4]}")


sql_to_create_countries_table = '''
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
)
'''

sql_to_create_cities_table = '''
CREATE TABLE IF NOT EXISTS cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    area FLOAT(8.2) DEFAULT 0,
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES countries(id)
)
'''

sql_to_create_employees_table = '''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    city_id INTEGER,
    FOREIGN KEY (city_id) REFERENCES cities(id)
)
'''

connection = create_connection('countries.db')

if connection is not None:
    print('Successfully connected!')

    create_table(connection, sql_to_create_countries_table)
    create_table(connection, sql_to_create_cities_table)
    create_table(connection, sql_to_create_employees_table)

    insert_countries(connection, 'Austria')
    insert_countries(connection, 'Switzerland')
    insert_countries(connection, 'U.S.A.')

    insert_cities(connection, 'Vienna', 2345.01, 1)
    insert_cities(connection, 'Montafon', 65456.88, 1)
    insert_cities(connection, 'Zurich', 125.6, 2)
    insert_cities(connection, 'Geneva', 4567.11, 2)
    insert_cities(connection, 'LA', 458.22, 3)
    insert_cities(connection, 'NY', 55, 3)
    insert_cities(connection, 'Miami', 789.5, 3)

    insert_employees(connection, 'Pavel', 'Vakurin', 1)
    insert_employees(connection, 'Julia', 'Vakurina', 2)
    insert_employees(connection, 'Stepan', 'Borodich', 3)
    insert_employees(connection, 'Stanislav', 'Bazeev', 4)
    insert_employees(connection, 'Alexandra', 'Nesterova', 5)
    insert_employees(connection, 'Piter', 'Parker', 6)
    insert_employees(connection, 'Miles', 'Morales', 6)
    insert_employees(connection, 'Aleksey', 'Verkeev', 7)
    insert_employees(connection, 'Suhrab', 'Nazarov', 1)
    insert_employees(connection, 'Vasiliy', 'Pupkin', 2)
    insert_employees(connection, 'Ivan', 'Ivanov', 3)
    insert_employees(connection, 'Anna', 'Vakurina', 4)
    insert_employees(connection, 'Tony', 'Stark', 5)
    insert_employees(connection, 'Wanda', 'Maksimoff', 6)
    insert_employees(connection, 'Im', 'Groot', 7)

    while True:
        print(
            "Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
        display_cities(connection)
        user_input = input("Введите id города: ")

        if user_input == '0':
            break

        try:
            city_id = int(user_input)
            display_employees(connection, city_id)
        except ValueError:
            print("Введите корректный id города.")

    connection.close()
