import psycopg2



# with psycopg2.connect(database="clients_db", user="postgres", password="159357874") as conn:
# with conn.cursor() as cur:

        #cur.execute("""
        #CREATE TABLE IF NOT EXISTS client(
        #    id SERIAL NOT NULL UNIQUE,
        #    name VARCHAR(60) NOT NULL,
        #    surname VARCHAR(60) NOT NULL,
        #    email VARCHAR(100)
        #);
        #""")

        #cur.execute("""
        #CREATE TABLE IF NOT EXISTS phones(
        #    id SERIAL UNIQUE,
        #    client_id INTEGER REFERENCES client(id),
        #    numbers INTEGER 
        #);
        #""")

        #cur.execute("""
        #INSERT INTO client(name,surname,email) 
        #VALUES('Ivan','Ivanov','ivanov335@gmail.com') RETURNING id;
        #""")
        #print(cur.fetchone())

        #cur.execute(f"""
        #INSERT INTO phones(client_id,numbers) 
        #VALUES('1','53535353') RETURNING id;
        #""")

        





#######################################################################
# conn = psycopg2.connect(database="clients_db", user="postgres", password="159357874")



# def create_table(conn):
#     with conn.cursor() as cur:
#         cur.execute("""
#             CREATE TABLE IF NOT EXISTS test3 (
#             id SERIAL NOT NULL UNIQUE,
#             client_id INTEGER REFERENCES client(id),
#             numbers INTEGER
#             );
#             """)
#
# create_table(conn)
# Функция № 1 Создание таблицы
#
#
# def insert_info(name,surname,email):
#     with conn.cursor() as cur:
#         cur.execute("""
#             INSERT INTO client(name,surname,email)
#             VALUES(%s,%s,%s) RETURNING id;
#             """,(name,surname,email))
#         conn.commit()
#
# insert_info('Petr','Ivanov','8989@mail.ru')
# Функция № 2 Добавление пользователя
#
#
# def insert_phone(client_id,phone):
#     with conn.cursor() as cur:
#         cur.execute("""
#             INSERT INTO phones(client_id,numbers)
#             VALUES(%s,%s) RETURNING id;
#             """,(client_id,phone))
#         conn.commit()
#
# insert_phone('1','53538553')
# Функция № 3 Добавление номера телефона
#
#
# def change_client(client_id, name=None, surname=None, email=None, phone=None):
#     if name == None:
#         pass
#     else:
#         with conn.cursor() as cur:
#             cur.execute("""
#                 UPDATE  client
#                     SET name = %s
#                 WHERE id = %s;
#                 """, (name, client_id))
#             conn.commit()
#         print("Name has changed")
#
#     if surname == None:
#         pass
#     else:
#         with conn.cursor() as cur:
#             cur.execute("""
#                 UPDATE  client
#                     SET surname = %s
#                 WHERE id = $s;
#                 """, (surname, client_id))
#             conn.commit()
#         print("Surname has changed")
#
#     if email == None:
#         pass
#     else:
#         with conn.cursor() as cur:
#             cur.execute("""
#                 UPDATE  client
#                     SET email = %s
#                 WHERE id = %s;
#                 """, (email, client_id))
#             conn.commit()
#         print("Email has changed")
#
#     if phone == None:
#         pass
#     else:
#         with conn.cursor() as cur:
#             cur.execute("""
#                 UPDATE  phones
#                     SET numbers = %s
#                 WHERE client_id = %s;
#                 """, (phone, client_id))
#             conn.commit()
#         print("Phone has changed")
#
#
# change_client('10',name = "Vlad", email = "stepanko@mail.ru",phone = "87899859")
# Функция № 4 Изменение данных существующего клиента

# def delete_phone(client_id, phone):
#     with conn.cursor() as cur:
#         cur.execute("""
#             DELETE FROM phones
#             WHERE client_id = %s and
#             numbers = %s;
#             """,(client_id,phone))
#         conn.commit()
#
# delete_phone('1', phone = 535353)
# Функция № 5 Удаление номера телефона существующего клиента

# def delete_client(client_id):
#     with conn.cursor() as cur:
#         cur.execute("""
#             DELETE FROM phones
#             WHERE client_id = %s;
#             """,(client_id))
#         conn.commit()
#
#     with conn.cursor() as cur:
#         cur.execute("""
#             DELETE FROM client
#             WHERE id = %s;
#             """,(client_id))
#         conn.commit()
#
# delete_client('9')
# Функция № 6 Удаление существующего клиента


# def find_client(name=None, surname=None, email=None, phone=0):
#     with conn.cursor() as cur:
#         cur.execute("""
#             SELECT * FROM client WHERE name =%s or surname = %s or
#             email = %s or id = (SELECT client_id FROM phones p WHERE p.numbers = %s);
#             """,(name,surname,email,phone))
#
#         print(cur.fetchall())
#
#
# find_client(name = 'Ivan',phone = 53535353 )
# Функция № 7 Получить данные существующего клиента по информации
