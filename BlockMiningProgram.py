#Using Python 3.6.4

import json
import cryptography
import datetime
import time
import hashlib

transactions = []

def checkForNewTransactions (transactionList, checkAgainst):
    transactionListLength = len(transactionList)
    if transactionListLength > checkAgainst:
        return True
    else:
        return False

def buildBlockChain (prevBlock, transactionData):
    newBlock = prevBlock + str(transactionData)
    successfulHash = calculateNonce(newBlock)
    return successfulHash

def calculateNonce(workBlock):
    nonce = 0
    loopNum = 0
    while loopNum < 50000:
        updatedBlock = workBlock + str(nonce)
        bytesBlock = bytes(updatedBlock, 'utf-8')
        hashedUpdatedBlock = hashlib.sha256(bytesBlock).hexdigest()
        if hashedUpdatedBlock.count('0') == 14:
            successfulHash = hashedUpdatedBlock
            return successfulHash

        nonce += 1
        loopNum += 1

    if loopNum == 50000:
        print ("No successful hash could be obtained within 50,000 attempts. Using last produced hash.")
        return (hashedUpdatedBlock) #Return the 50,000th attempt at finding 14 0's
    
    

#########################################################################################


print ("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-(*)-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print ("\n\t\tWelcome to the Block Miner")
print ("\n\t      A Program by Brandon Gordon")
print ("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-(*)-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

try: #Try to open the file in read mode (it needs to exist for this to work)
    f = open ('BlockChain.txt', 'r') 
    workingBlock = f.read()
    f.close()
    
except: #If the BlockChain file doesnt already exist, create a new block based on arbitrary data
    block = [0, "first block", ('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())), hashlib.sha256(bytes('first block', 'utf-8')).hexdigest()]
    bytesBlock = bytes(str(block), 'utf-8')
    hashedBlock = hashlib.sha256(bytesBlock)
    workingBlock = hashedBlock.hexdigest()

    f = open ("BlockChain.txt", 'w')
    f.write(workingBlock)
    f.close()

print ("Operating on current block:", workingBlock) #Print the hash that will be used at the start of the operation

recordedTransactions = len(transactions)

foundTransactions = False
while foundTransactions == False: #If the program doesnt find any transactions, keep looping until it does
    try:
        f = open('Transactions.txt', 'r')
        transactions = json.load(f)
        f.close()
        print ("Transactions file loaded.")
        foundTransactions = True #Indicate you have found a new transaction
    except:
        print ("No transactions found. Try recording some.")
        time.sleep(3)

while foundTransactions == True: #When you do find a first transaction,
    f = open('Transactions.txt', 'r')
    transactions = json.load(f)
    f.close()
    if checkForNewTransactions (transactions, recordedTransactions) == True: #check if you have already operated on it before
        recordedTransactions = len(transactions)    #If it returns true (you havent already operated on it), update the record so we dont operate on it again
        successfulHash = buildBlockChain(workingBlock, transactions[(recordedTransactions - 1)]) #Send the new transaction data through the buildBlockChain function and save the successful block chain to "successfulHash"
        print ("Successful Hash: ", successfulHash)

        f = open ("BlockChain.txt", 'w')
        f.write(successfulHash) #Write Successful Hash to file
        f.close

        workingBlock = successfulHash #Update the hash that we are now working with for the next set of transactions

    time.sleep(3)


    
