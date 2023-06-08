import psycopg2

def create_table():
    conn = psycopg2.connect(database = 'postgress', user = 'postgres', password = 'ayan2004')
    # database connection
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE phonebook (
    USER_NAME TEXT PRIMARY KEY NOT NULL,
    PHONENUMBER TEXT NOT NULL);""")
    print("[INFO] Table created successfully!")
    conn.commit()
    cursor.close()
    conn.close()
def add_user():
    add = input().split()
    postgre_query = """INSERT INTO phonebook( user_name, phonenumber) VALUES (%s, %s) """
    data_toinsert = (add[0], add[1])
    cursor.execute(postgre_query, data_toinsert)

    conn.commit()
    print("Data added!")


def fetch_users():
    cursor.execute("SELECT * FROM phonebook ")
    table = cursor.fetchall()
    for row in table:
        c = row[0] + " " + row[1]
        print(c)


def update():
    print("Type who's number you want to change")
    name = input()
    print("New number")
    number = input()
    postgre_query = """UPDATE phonebook SET phonenumber = %s WHERE user_name = %s """
    cursor.execute(postgre_query, (number, name))

    conn.commit()
    print("Data updated!")


def find():
    print("Insert name who's number you want to see")
    name = input()
    cursor.execute("SELECT * FROM phonebook ")
    table = cursor.fetchall()
    for row in table:
        if name == row[0]:
            c = row[0] + " " + row[1]
            print(c)


def delete_user():
    print("Insert name you want to delete")
    name = input()
    postgre_query = """DELETE FROM phonebook WHERE user_name = %s """
    cursor.execute(postgre_query, (name,))

    conn.commit()
    print("Data deleted!")


try:
    cond = False
    conn = psycopg2.connect("dbname=postgress user=postgres password=ayan2004")
    cursor = conn.cursor()

    while not cond:
        print(
            "\nChoose action:\n0.Create table\n1.Add user and number\n2.Change number of existing user\n3.Delete user\n4.Find number by name\n5.Show all names and numbers\n6.Exit")
        action = input()
        if action == '1':
            print("Insert data")
            add_user()
        elif action == '0':
            create_table()
        elif action == '2':
            update()
        elif action == '3':
            delete_user()
        elif action == '4':
            find()
        elif action == '5':
            fetch_users()
        elif action == '6':
            cond = True


except psycopg2.Error as e:
    print("Failed!")

finally:
    cursor.close()
    conn.close()
    print("Connection closed!")