import psycopg2
import csv

# 1. searching
conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgress',
    password = 'ayan2004',
    user = 'postgres'
)
cur = conn.cursor()

cur.execute(
    '''CREATE OR REPLACE FUNCTION search_qwer(a VARCHAR)
      RETURNS SETOF qwer 
   AS
   $$
      SELECT * FROM qwer WHERE name = a or number = a;
   $$
   language sql;
   '''
)

cur.execute("SELECT * FROM search_qwer('87777777777')")
res = cur.fetchall()
print(*res, sep='\n')

# 2. add or updating
conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgress',
    password = 'ayan2004',
    user = 'postgres'
)
cur = conn.cursor()

cur.execute(
   '''CREATE OR REPLACE PROCEDURE add_or_update_user(i INTEGER, nm VARCHAR, num VARCHAR)
      LANGUAGE plpgsql
      AS $$
      DECLARE 
         cnt INTEGER;
      BEGIN
         SELECT INTO cnt (SELECT count(*) FROM qwer WHERE name = nm);
         IF cnt > 0 THEN
            UPDATE qwer
               SET number = num
               WHERE name = nm;
         ELSE
            INSERT INTO qwer(id, name, number) VALUES (i, nm, num);
            END IF;
      END;
      $$;''')

cur.execute(
    '''CREATE OR REPLACE PROCEDURE insert_or_update_user(username VARCHAR(100), phone VARCHAR(12))
AS $$
BEGIN
    IF EXISTS (SELECT * FROM qwer WHERE name = username) THEN
        UPDATE qwer SET number = phone WHERE name = username;
    ELSE
        INSERT INTO qwer (name, number) VALUES (username, phone);
    END IF;
END;
$$ LANGUAGE plpgsql;
'''
)

cur.execute("CALL insert_or_update_user( 'Alex', '87773854974')")

# 3. by list
conn = psycopg2.connect(
    host='localhost',
    database='postgress',
    password='ayan2004',
    user='postgres'
)
cur = conn.cursor()

cur.execute(
    '''CREATE OR REPLACE PROCEDURE insert_list_of_users(
  IN users TEXT[][]
)
LANGUAGE plpgsql
AS $$
DECLARE
  i TEXT[];
  invalid_users TEXT[][];
BEGIN 
   FOREACH i SLICE 1 IN ARRAY users
   LOOP
    IF LENGTH(i[3]) != 11 THEN
        invalid_users := array_cat(invalid_users, ARRAY[i]);
    ELSE
        INSERT INTO qwer (id, name, number) VALUES (CAST(i[1] AS INTEGER), i[2], i[3]);
    END IF;
END LOOP;

    IF array_length(invalid_users, 1) > 0 THEN
        RAISE NOTICE 'The following users have invalid phone numbers: %', invalid_users;
    END IF;
END
$$;
''')

cur.execute('''CALL insert_list_of_users(ARRAY[
    ARRAY['22', 'aveke', '8787497949'],
    ARRAY['23', 'aldik', '8707894'],
    ARRAY['24', 'google', '87973688975']
]);
''')

# 4. paginating
conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgress',
    password = 'ayan2004',
    user = 'postgres'
)

cur = conn.cursor()
cur.execute(
    '''CREATE OR REPLACE FUNCTION paginating(a integer, b integer)
RETURNS SETOF qwer
AS $$
   SELECT * FROM qwer
	ORDER BY name
	LIMIT a OFFSET b;
$$
language sql;'''
)
cur.execute("SELECT * FROM paginating(3, 2)")  # ограниченных a записями, начиная с b-й записи.
print(cur.fetchall())

# 5. deleting
config = psycopg2.connect(
    host = 'localhost',
    database = 'postgress',
    password = 'ayan2004',
    user = 'postgres'
)

cur= config.cursor()
cur.execute(
    '''CREATE OR REPLACE PROCEDURE delete_user(del VARCHAR)
AS $$
BEGIN
    DELETE FROM qwer WHERE name = del OR number = del;
END;
$$ LANGUAGE plpgsql;
'''
)
cur.execute("CALL delete_user('rtyuiuytr')")