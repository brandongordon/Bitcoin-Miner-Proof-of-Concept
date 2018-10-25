#Using Python 3.6.4

import datetime
import json
import cryptography


def recordTransaction():
    transaction["from"] = input("Enter username of person sending the cryptocurrency amount: ")
    transaction["to"] = input("Enter username of person receiving the cryptocurrency amount: ")
    transaction["amount"] = inputInt("Amount: ")
    transaction["timestamp"] = ('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
    transactions.append(transaction.copy())

def saveChanges(dataList): #This function opens "data.txt" in write mode and writes dataList to it in JSON format.
    f = open('Transactions.txt', 'w')
    json.dump(transactions, f)
    f.close()

def inputInt(prompt): #This function repeatedly prompts for input until an integer is entered.
    keepGoing = True
    while keepGoing:
        something = input(prompt)
        if something.isdigit() == True:  #Prompts the user to enter value, and confirms that it is a digit.
            keepGoing = False
    return int(something)

################################################################################################

print ("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-(*)-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print ("\n\t\tWelcome to Crypto-Transation Recorder")
print ("\n\t\t      A Program by Brandon Gordon")
print ("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-(*)-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

transactions = []
transaction = {}

try:
    f = open('Transactions.txt', 'r')
    transactions = json.load(f) #Read the json data from 'f' into the 'transaction' varaible(list).
    f.close()
    print ("Data loaded from file")

except:
    print ("Failed to load transactions. Writing to new file.")

while True:
    print ("Choose from the following options: ")
    menuChoice = input ("\t[R]ecord Transaction \n\t[Q]uit \n >").upper() #Stores as capital letter

    if menuChoice == "R":
        recordTransaction()
        saveChanges(transactions)

    elif menuChoice == "Q":
        print ("Goodbye!")
        break

    else:
        print ("Please enter valid input.\n")
