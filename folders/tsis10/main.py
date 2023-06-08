import psycopg2
import csv

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgress',
    user = 'postgres',
    password = 'ayan2004'
)
cur = conn.cursor()
def inputData():
    user_name = input()
    phone_number = input()
    cur.execute('''
    INSERT INTO postgress.public.phone_book("PersonName", "PhoneNumber") VALUES(%s, %s); ''', (user_name, phone_number))

def importFromCSV():
    with open('info.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            personName, phoneNumber = row
            cur.execute('''
            INSERT INTO postgress.public.phone_book("PersonName", "PhoneNumber") VALUES(%s, %s); ''', (personName, phoneNumber))

def updateData(personName, phoneNumber):
    cur.execute('''
    UPDATE postgress.public.phone_book.SET "PhoneNumber" = %s WHERE "PersonName" = %s''', (phoneNumber, personName))

def queryData():
    cur.execute('''
    SELECT * FROM postgress.public.phone_book''')
    data = cur.fetchall()
    path = r"C:\Users\User\PycharmProjects\pythoncodes\tsis10\queredData.txt"
    f = open(path, 'w')
    for row in data:
        f.write("Name: " +  str(row[1]) + "\n" + "Number: " + str(row[2]) + "\n")
        f.close()

def deleteData():
    print('Which name do you want to delete?\n')
    personName = input()
    cur.execute(f'''
    DELETE FROM postgress.public.phone_book WHERE "PersonName" = '{personName}' ''')

def deleteAllData():
    cur.execute('''
    DELETE FROM postgress.public.phone_book''')

done = False
while not done:
    print("What do you want to do?\n\
              1. Input data from console\n\
              2. Upload form csv file\n\
              3. Update existing contact\n\
              4. Query data from the table\n\
              5. Delete data from table by person name\n\
              6. Delete all data from table\n\
              7. Exit")
    x = int(input('Choose number 1-5\n'))
    if(x == 1):
        inputData()
    elif(x == 2):
        importFromCSV()
    elif(x == 3):
        print('Which number do you want to update? Enter your name and new number: ')
        name = input()
        newNumber = input()

        updateData(name, newNumber)
    elif(x == 4):
        queryData()
    elif(x == 5):
        deleteData()
    elif(x == 6):
        deleteAllData()
    elif(x == 7):
        done = True
    conn.autocommit = True

cur.close()
conn.close()