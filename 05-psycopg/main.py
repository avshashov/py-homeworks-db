import psycopg2
from psycopg2 import sql


def create_tables(connect):
    try:
        with connect.cursor() as cur:
            cur.execute("""
                        CREATE TABLE IF NOT EXISTS clients (
                        id SERIAL PRIMARY KEY, 
                        client_name VARCHAR(30) NOT NULL,
                        surname VARCHAR(30) NOT NULL,
                        email VARCHAR(30) NOT NULL UNIQUE
                        ); 
            """)

            cur.execute("""
                        CREATE TABLE IF NOT EXISTS phone_numbers (
                        id SERIAL PRIMARY KEY,
                        phone_number VARCHAR(12) DEFAULT NULL,
                        client_id INT REFERENCES clients(id) ON DELETE CASCADE
                        );
            """)

            connect.commit()
            print('[INFO] Таблицы clients и phone_numbers успешно созданы.')


    except Exception as ex:
        print(f'[Error] {ex}')
    finally:
        if connect:
            connect.close()


def add_new_client(connect, name, surname, email, number=None):
    try:
        with connect.cursor() as cur:
            cur.execute("""
                        INSERT INTO clients (client_name, surname, email)
                        VALUES (%s, %s, %s);
            """, (name, surname, email))

            cur.execute("""
                        SELECT id FROM clients
                        WHERE client_name = %s AND surname = %s;
            """, (name, surname))
            client_id = cur.fetchone()[0]

            cur.execute("""
                        INSERT INTO phone_numbers (phone_number, client_id)
                        VALUES (%s, %s);
                        """, (number, client_id))

            connect.commit()
            print('[INFO] В базу добавлен новый клиент.')


    except Exception as ex:
        print(f'[Error] {ex}')
    finally:
        if connect:
            connect.close()


def add_phone_number(connect, name, surname, number):
    try:
        with connect.cursor() as cur:
            cur.execute("""
                        SELECT id FROM clients
                        WHERE client_name = %s AND surname = %s;
                        """, (name, surname))
            client_id = cur.fetchone()[0]

            cur.execute("""
                        INSERT INTO phone_numbers (phone_number, client_id)
                        VALUES (%s, %s);
                        """, (number, client_id))

            connect.commit()
            print(f'[INFO] Клиенту {name} {surname} добавлен новый номер.')


    except Exception as ex:
        print(f'[Error] {ex}')
    finally:
        if connect:
            connect.close()


def change_client_data(connect, name, surname, email, number):
    new_data = input('''Введите через пробел новые данные в следующем порядке: 
    Имя Фамилия email Телефон''').split()

    try:
        with connect.cursor() as cur:
            cur.execute("""
                        UPDATE clients
                        SET client_name = %s,
                            surname = %s,
                            email = %s
                        WHERE email = %s 
            ;""", (*new_data[:3], email))

            cur.execute("""
                        UPDATE phone_numbers
                        SET phone_number = %s
                        WHERE phone_number = %s
                ;""", (new_data[3], number))

            connect.commit()
            print(f'[INFO] Данные изменены.')

    except Exception as ex:
        print(f'[Error] {ex}')
    finally:
        if connect:
            connect.close()


def del_phone_number(connect, number):
    try:
        with connect.cursor() as cur:
            cur.execute("""
                        DELETE FROM phone_numbers
                        WHERE phone_number = %s;
            """, (number,))

            connect.commit()
            print(f'[INFO] Номер удален.')

    except Exception as ex:
        print(f'[Error] {ex}')
    finally:
        if connect:
            connect.close()


def del_client(connect, name, surname, email):
    try:
        with connect.cursor() as cur:
            cur.execute("""
                        DELETE FROM clients
                        WHERE email = %s;
            """, (email,))
            connect.commit()
            print(f'[INFO] Клиент удален из базы.')

    except Exception as ex:
        print(f'[Error] {ex}')
    finally:
        if connect:
            connect.close()


def search_client(connect, data):
    params = {'Имя': 'client_name', 'Фамилия': 'surname',
              'Email': 'email', 'Телефон': 'phone_number'}

    param = input('Выберите параметр поиска: Имя, Фамилия, Email, Телефон: ')

    try:
        with connect.cursor() as cur:
            cur.execute(sql.SQL("""
                        SELECT client_name, surname, email, phone_number 
                        FROM clients c
                            JOIN phone_numbers p ON c.id = p.client_id
                        WHERE {} = %s;
            """).format(sql.Identifier(params[param])), (data,))
            res = cur.fetchall()
            print(f'Результаты поиска:\n{res}' if len(res) != 0 else 'Клиент не найден.')

    except Exception as ex:
        print(f'[Error] {ex}')
    finally:
        if connect:
            connect.close()


conn = psycopg2.connect(database='personal_data', user='postgres', password='1234')

# with conn:
#     with conn.cursor() as cur:
#         cur.execute("DROP TABLE clients CASCADE")
#         cur.execute("DROP TABLE phone_numbers CASCADE")
# create_tables(conn)

# add_new_client(conn, 'Ivan', 'Ivanov', 'ivanov@gmail.com', '89091324321')
# add_new_client(conn, 'Petr', 'Petrov', 'petrov@gmail.com')
# add_phone_number(conn, 'Petr', 'Petrov', '89241724365')
# change_client_data(conn, 'Petr', 'Petrov', 'petrov@gmail.com', '89241724365')
# del_phone_number(conn, '+79146351212')
# del_client(conn, 'Petr', 'Petrov', 'petroff@gmail.com')
# search_client(conn, 'Ivan')
