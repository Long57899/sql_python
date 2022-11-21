import psycopg2



with psycopg2.connect(database="clients_db", user="postgres", password="159357874") as conn:
    with conn.cursor() as cur:
        
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

        def create_table(cursor, name):
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {name}(
                id SERIAL NOT NULL UNIQUE,
                client_id INTEGER REFERENCES client(id),
                numbers INTEGER 
                );
                """)
        
       # create_table(cur,'test')
       # Функция № 1 Создание таблицы

        

        def insert_info(cursor, name,surname,email):
            cursor.execute(f"""
            INSERT INTO client(name,surname,email) 
            VALUES('{name}','{surname}','{email}') RETURNING id;
            """)
          
        # insert_info(cur,'name','surname','email')
        # Функция № 2 Добавление пользователя


        def insert_phone(cursor, client_id,phone):
            cursor.execute(f"""
            INSERT INTO phones(client_id,numbers) 
            VALUES('{client_id}','{phone}') RETURNING id;
            """)

        # insert_phone(cur,'1','535353')
        # Функция № 3 Добавление номера телефона


        def change_client(cursor, client_id, name=None, surname=None, email=None, phone=None):
            cursor.execute(f"""
            UPDATE  client 
                SET name = '{name}'
            WHERE id = '{client_id}';
            """)
            
            cursor.execute(f"""
            UPDATE  client 
                SET surname = '{surname}'
            WHERE id = '{client_id}';
            """)

            cursor.execute(f"""
            UPDATE  client 
                SET email = '{email}'
            WHERE id = '{client_id}';
            """)

            cursor.execute(f"""
            UPDATE  phones 
                SET numbers = '{phone}'
            WHERE client_id = '{client_id}';
            """)

        # change_client(cur,'2','Egor',phones = 898989)
        # Функция № 4 Изменение данных существующего клиента

        def delete_phone(cursor, client_id, phone):
            cursor.execute(f"""
            DELETE FROM phones 
            WHERE client_id = '{client_id}' and 
            numbers = '{phone}';
            """)

        # delete_phone(cur,'2', phone = 898989)
        # Функция № 5 Удаление номера телефона существующего клиента

        def delete_client(cursor, client_id):
            cursor.execute(f"""
            DELETE FROM phones 
            WHERE client_id = '{client_id}';
            """)

            cursor.execute(f"""
            DELETE FROM client 
            WHERE id = '{client_id}';
            """)

        # delete_client(cur,'1')
        # Функция № 6 Удаление существующего клиента

        def find_client(cursor, name=None, surname=None, email=None, phone=0):
            cur.execute(f"""
            SELECT * FROM client WHERE name ='{name}' or surname = '{surname}' or 
            email = '{email}' or id = (SELECT client_id FROM phones p WHERE p.numbers = '{phone}');
            """) 

            print(cur.fetchall())


        # find_client(cur,name = 'Ivan',phone = 53535353 )
        # Функция № 7 Получить данные существующего клиента по информации

        

conn.close()

