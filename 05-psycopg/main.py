import psycopg2


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
                        client_id INT REFERENCES clients(id)
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


conn = psycopg2.connect(database='personal_data', user='postgres', password='1234')
# add_new_client(conn, 'Ivan', 'Ivanov', 'ivanov@gmail.com', '89091324321')
# add_new_client(conn, 'Petr', 'Petrov', 'petrov@gmail.com')
# add_phone_number(conn, 'Petr', 'Petrov', '89241724365')
# change_client_data(conn, 'Petr', 'Petrov', 'petrov@gmail.com', '89241724365')

# with conn:
#     with conn.cursor() as cur:
#         cur.execute("DROP TABLE clients CASCADE")
#         cur.execute("DROP TABLE phone_numbers CASCADE")
# create_tables(conn)

# Petya Petrov 228@gmail.com 2281488

# print('Petya Petrov 228@gmail.com 2281488'.split())