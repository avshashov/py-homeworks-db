import psycopg2
from psycopg2 import sql


def del_tables(connect):
    with connect:
        with connect.cursor() as cur:
            cur.execute("DROP TABLE clients CASCADE")
            cur.execute("DROP TABLE phone_numbers CASCADE")


def create_tables(connect):
    try:
        with connect.cursor() as cur:
            cur.execute("""
                        CREATE TABLE IF NOT EXISTS clients (
                        client_id SERIAL PRIMARY KEY, 
                        client_name VARCHAR(30) NOT NULL,
                        surname VARCHAR(30) NOT NULL,
                        email VARCHAR(30) NOT NULL UNIQUE
                        ); 
            """)

            cur.execute("""
                        CREATE TABLE IF NOT EXISTS phone_numbers (
                        id SERIAL PRIMARY KEY,
                        client_id INT REFERENCES clients(client_id) ON DELETE CASCADE,
                        phone_number VARCHAR(12) DEFAULT NULL
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
                        SELECT client_id FROM clients
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


def add_phone_number(connect, client_id, number):
    try:
        with connect.cursor() as cur:
            cur.execute("""
                        INSERT INTO phone_numbers (client_id, phone_number)
                        VALUES (%s, %s);
                        """, (client_id, number))

            connect.commit()
            print(f'[INFO] Номер телефона добавлен в базу данных.')


    except Exception as ex:
        print(f'[Error] {ex}')
    finally:
        if connect:
            connect.close()


def change_client_data(connect, client_id, client_name=None, surname=None, email=None, number=None):
    # params = [name, surname, email]
    data = {
        'client_name': client_name,
        'surname': surname,
        'email': email
        # 'phone_number': number
    }

    try:
        with connect.cursor() as cur:
            for key, value in data.items():
                if value:
                    cur.execute(sql.SQL("""
                                UPDATE clients
                                SET {} = %s
                                    -- # surname = %s,
                                    -- # email = %s
                                -- WHERE client_id = %s
                                WHERE client_id = 3;
                    """).format(sql.Identifier(key)), (value,))
                    # ;""").format(sql.Identifier(key)), (value, client_id))

            if number:
                cur.execute("""
                            UPDATE phone_numbers
                            SET phone_number = %s
                            WHERE client_id = %s
                    ;""", (number, client_id))

            connect.commit()
            print(f'[INFO] Данные изменены.')

    except Exception as ex:
        print(f'[Error] {ex}')
    finally:
        if connect:
            connect.close()


def del_phone_number(connect, client_id, number):
    try:
        with connect.cursor() as cur:
            cur.execute("""
                        DELETE FROM phone_numbers
                        WHERE client_id = %s AND phone_number = %s;
            """, (client_id, number))

            connect.commit()
            print(f'[INFO] Номер удален.')

    except Exception as ex:
        print(f'[Error] {ex}')
    finally:
        if connect:
            connect.close()


def del_client(connect, client_id):
    try:
        with connect.cursor() as cur:
            cur.execute("""
                        DELETE FROM clients
                        WHERE client_id = %s;
            """, (client_id,))
            connect.commit()
            print(f'[INFO] Клиент удален из базы.')

    except Exception as ex:
        print(f'[Error] {ex}')
    finally:
        if connect:
            connect.close()


def search_client(connect, client_name=None, surname=None, email=None, number=None):
    data = {
        'client_name': client_name,
        'surname': surname,
        'email': email,
        'phone_number': number
    }

    try:
        with connect.cursor() as cur:
            for key, value in data.items():
                if value:
                    cur.execute(sql.SQL("""
                            SELECT client_name, surname, email, phone_number 
                            FROM clients
                                JOIN phone_numbers USING(client_id)
                            WHERE {} = %s;
                """).format(sql.Identifier(key)), (value,))
                    res = cur.fetchall()
                    print(f'Результаты поиска:\n{res}' if len(res) != 0 else 'Клиент не найден.')

    except Exception as ex:
        print(f'[Error] {ex}')
    finally:
        if connect:
            connect.close()


conn = psycopg2.connect(database='personal_data', user='', password='')

# del_tables(conn)
# create_tables(conn)

# add_new_client(conn, 'Ivan', 'Ivanov', 'ivanov@gmail.com', '89091324321')
# add_new_client(conn, 'Vladimir', 'Ivanov', 'vl@gmail.com')
# add_new_client(conn, 'Petr', 'Petrov', 'petrov@gmail.com')
# add_phone_number(conn, 2, '89241724365')
# change_client_data(conn, 2, 'Petya', 'Petrov', 'petrov@gmail.com')
change_client_data(conn, 3, 'Petya', 'Petrov', number='123456')
# change_client_data(conn, 3, 'Petya', 'Petrov')
# del_phone_number(conn, 2, '89241724365')
# del_client(conn, 2)
# search_client(conn, surname='Ivanov')
