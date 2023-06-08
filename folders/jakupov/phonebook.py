import psycopg2
import csv


class CSVManager:
    def getAllEntries(self):
        dataSet = []
        with open("data/sample.csv") as file:
            reader = csv.reader(file)
            for i in reader:
                dataSet.append(i)
        return dataSet[1:]


class DBManager:

    def __init__(self, fileM):
        self.conn = None
        self.fileM = fileM
        self.cursor = None

    def checkIfExists(self, table_name):
        query = f"""
            SELECT *
            FROM INFORMATION_SCHEMA.TABLES
            WHERE TABLE_SCHEMA = 'test'
            AND TABLE_NAME = '{table_name}'
            """

        self.cursor.execute(query)
        return bool(self.cursor.fetchone())

    def createTable(self):
        query = """
            CREATE TABLE lab10.test.PhoneBook11(
                id SERIAL,
                phone VARCHAR(11),
                name VARCHAR(255) UNIQUE
            )
            """

        self.cursor.execute(query)

    def insertData(self, name, phone):
        query = f"""
            INSERT INTO lab10.test.phonebook11 ("phone", "name")
            VALUES ('{phone}', '{name}') ON CONFLICT DO NOTHING
        """
        self.cursor.execute(query)

    def insertListOfData(self, data):
        dataToInsert = []
        for i in data:
            name, phone = i.split(',')
            dataToInsert.append(f"ARRAY['{name.strip()}', '{phone.strip()}']")
        query = f"""SELECT * FROM lab10.test.insertlistofdata(ARRAY[{",".join(dataToInsert)}])"""
        self.cursor.execute(query)
        output = self.cursor.fetchall()
        self.commit()
        return output

    def updateOrInsertProced(self, username, phone):
        query = f"""call lab10.test.insertorupdatephone('{username}', '{phone}')"""
        self.cursor.execute(query)
        self.commit()

    def insertDataFromSet(self, data):
        for i in data:
            self.insertData(name=i[0], phone=i[1])

    def addCSV(self):
        newData = self.fileM.getAllEntries()
        oldData = [[i[2], i[1]] for i in self.getAllPhones()]
        filtered = [i for i in newData if i not in oldData]
        self.insertDataFromSet(filtered)

    def deleteAllPhones(self):
        query = """DELETE FROM lab10.test.phonebook11"""
        self.cursor.execute(query)

    def deleteBy(self, name, phone):
        query = f"""call lab10.test.deleteBy('{name}', '{phone}')"""
        self.cursor.execute(query)
        self.commit()

    def getAllPhones(self):
        query = """
            SELECT * FROM lab10.test.phonebook11
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def getNumberOfPages(self, name='', phone=''):
        query = f"""SELECT * FROM lab10.test.getNumberOfPages('{name}', '{phone}')"""
        self.cursor.execute(query)
        number = self.cursor.fetchone()[0]
        return number

    def getAllPhonesByPage(self, page):
        query = f"""SELECT * FROM lab10.test.getPhonesByPages({page})"""
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def getPhonesBy(self, name, phone, page):
        query = f"""
            SELECT * FROM lab10.test.filterBy('{name}', '{phone}', {page})
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()

    def commit(self):
        self.conn.commit()

    def connect(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="lab10",
            user="postgres",
            port="5432",
            password="Dias2004")
        self.cursor = self.conn.cursor()
        # execute a statement

        if not self.checkIfExists("phonebook11"):
            self.createTable()
            self.commit()


class InteractionManager:
    def __init__(self):
        self.fileM = CSVManager()
        self.db = DBManager(self.fileM)
        self.db.connect()

    def start(self):
        print("""
                1 to get all data
                1.1 to filter data by name
                2 to add CSV file
                3 to write new data from console (or update existing)
                3.1 to insert list of data
                4 to delete by username
                5 to delete everything
            """)
        action = input("""Enter number: """)
        match action:
            case "1":
                userInputPage = 1

                # PAGINATION
                numberOfPages = self.db.getNumberOfPages()
                print("*" * 8)
                print(f"Total number of pages: {numberOfPages}")
                try:
                    userInputPage = int(input("Enter page number or -1(to quit): "))
                except ValueError as e:
                    print("Not a number", type(e))
                while 0 < userInputPage <= numberOfPages:
                    print(f"Current page: {userInputPage}")
                    output = self.db.getAllPhonesByPage(userInputPage)
                    for i in output:
                        print(f"ID: {i[0]}, name: {i[2]}, phone: {i[1]}")
                    try:
                        userInputPage = int(input("Enter page number or -1(to quit): "))
                    except ValueError:
                        print("Not a number")

            case "1.1":
                name = input("Enter filter name: ")
                phone = input("Enter filter phone: ")

                if len(phone) <= 11:
                    # PAGINATION
                    userInputPage = 1
                    numberOfPages = self.db.getNumberOfPages(name, phone)
                    print(f"Total number of pages: {numberOfPages}")
                    try:
                        userInputPage = int(input("Enter page number or -1(to quit): "))
                    except ValueError as e:
                        print("Not a number", type(e))
                    while 0 < userInputPage <= numberOfPages:
                        print(f"Current page: {userInputPage}")
                        output = self.db.getPhonesBy(name, phone, userInputPage)
                        for i in output:
                            print(f"ID: {i[0]}, name: {i[2]}, phone: {i[1]}")
                        try:
                            userInputPage = int(input("Enter page number or -1(to quit): "))
                        except ValueError:
                            print("Not a number")
            case "2":
                self.db.addCSV()
                self.db.commit()
            case "3":
                newName = input("Enter new name or leave blank:")
                newPhone = input("Enter new phone or leave blank:")
                try:
                    if len(newPhone) == 0 or len(newPhone) == 11:
                        self.db.updateOrInsertProced(newName, newPhone)
                        print("Successfully")
                    else:
                        print('Incorrect phone format')
                except Exception as e:
                    print(f"ERROR {e}")
            case "3.1":
                listOfData = input("Enter names and phones in format name1, phone1;name2, phone2: ").split(";")
                if listOfData:
                    incorrect = self.db.insertListOfData(listOfData)
                    for i in incorrect:
                        print(f"Incorrect data: {i}")

            case "4":
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                try:
                    self.db.deleteBy(name, phone)
                except Exception as e:
                    print(f"Something went wrong {e}")
            case "5":
                self.db.deleteAllPhones()
                self.db.commit()
        self.db.close()


mng = InteractionManager()
mng.start()
