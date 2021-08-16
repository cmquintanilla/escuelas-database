import mongoDB as MongoDB


def welcome():
    print(120 * '*')
    print("* Welcome to Evaluacion01, this program was created for learning purposes and it's a CRUD for School Center Management *")
    print("* For this scenario we are using MongoDB and ATLAS for the persistence of the Data", 35 * ' ', '*')
    print(120 * '*')
    print("\n")


def menu():
    print("Choose an option please:")
    print("MENU")
    print("1- Insert a new School Center")
    print("2- Visualize a School Center")
    print("3- Update a School Center")
    print("4- Delete a School Center")
    print("5- Exit")


def optionValidation(op):
    try:
        option = int(op)
        return option
    except ValueError:
        print("This is not a correct option!!!!")
        return -1


def insertSchool(DB: MongoDB):
    name = input("Type School Identification Name: ")
    department = input("Type the Department's Name where is located: ")
    municipality = input("Type the Municipalitie's Name where is located: ")
    school = {"_id": "", "Nombre": name,
              "Departamento": department, "Municipio": municipality}
    DB.insert(school)
    print("Successfully inserted!")
    print("\n")


def visualizeSchools(DB: MongoDB):
    print("What do you whant to do?")
    print("1-Visualize all the Schools")
    print("2-Search School by Name")
    print("3-Search School by ID Number")
    op = input("Please type your option: ")
    if op == "1":
        print("Here all the Schools registered...")
        print("\n")
        myquery = {}
        DB.find(myquery)
        for x in DB.document:
            print("ID: ",  x["_id"])
            print("Name: ",  x["Nombre"])
            print("Department: ",  x["Departamento"])
            print("Municipality: ",  x["Municipio"])
            print(30 * '*')
    elif op == "2":
        name = input("Type the name of the School: ")
        myquery = {"Nombre": {"$regex": name}}
        DB.find(myquery)
        # if DB.document
        print("Here what it was found...")
        print("\n")
        for x in DB.document:
            print("ID: ",  x["_id"])
            print("Name: ",  x["Nombre"])
            print("Department: ",  x["Departamento"])
            print("Municipality: ",  x["Municipio"])
            print(30 * '*')
    elif op == "3":
        ID = input("Type the ID number of the School: ")
        myquery = {"_id": ID}
        DB.find(myquery)
        # if DB.document
        print("Here what it was found...")
        print("\n")
        for x in DB.document:
            print("ID: ",  x["_id"])
            print("Name: ",  x["Nombre"])
            print("Department: ",  x["Departamento"])
            print("Municipality: ",  x["Municipio"])
    else:
        print("You typed a non existent option")
    print("\n")


def updateSchool(DB: MongoDB):
    school = {}
    # Asking for the ID
    ID = input("Type School ID Number you want to update: ")
    if optionValidation(ID) != -1:
        myquery = {"_id": ID}
        DB.find(myquery)
        if DB.document.count() == 0:
            print("Sorry there is no School with that ID number!!!")
            return
    else:
        return
    # Asking for the Name
    name = input("Type New School Identification Name: ")
    if name != None:
        school["Nombre"] = name
    # Asking for the Department
    department = input("Type the New Department's Name where is located: ")
    if department != None:
        school["Departamento"] = department
    # Asking for the Municipality
    municipality = input(
        "Type the New Municipalitie's Name where is located: ")
    if municipality != None:
        school["Municipio"] = municipality
    school = {"$set": school}
    DB.update(myquery, school)
    print("Successfully updated!")
    print("\n")


def deleteSchool(DB: MongoDB):
    school = {}
    # Asking for the ID
    ID = input("Type School ID Number you want to delete: ")
    if optionValidation(ID) != -1:
        myquery = {"_id": ID}
        DB.find(myquery)
        if DB.document.count() == 0:
            print("Sorry there is no School with that ID number!!!")
            return
    else:
        return
    school["_id"] = ID
    DB.delete(school)
    print("Successfully deleted!")
    print("\n")
