import credentials as key
import mongoDB as mongo
import functionsCE as fnc
import os

mongoDB = mongo.MongoDB(key.CONNECTION_STRING)
mongoDB.setDatabase("Evaluacion01")
mongoDB.setCollection("CE")

os.system("cls")
fnc.welcome()

while True:
    fnc.menu()
    option = input(" Please type your option: ")
    if fnc.optionValidation(option) == -1:
        fnc.menu()
        continue
    if option == "1":
        fnc.insertSchool(mongoDB)
    if option == "2":
        fnc.visualizeSchools(mongoDB)
    if option == "3":
        fnc.updateSchool(mongoDB)
    if option == "4":
        fnc.deleteSchool(mongoDB)
    if option == "5":
        break