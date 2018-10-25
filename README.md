# Bitcoin Miner - Proof of Concept

### Instructions for running your program to complete the required objectives:

Ensure that there are no previously generated text files in the running directory. If they are present, please delete them.

 - **Open and run the Block Mining program**
 
    - Upon first launch of this program, it will generate a genesis file, containing arbitrary data that is used to generate the first block in the chain.
  
    - It will then prompt the user to begin recording transactions. They should do this via the Transaction Recording program
  
    - The block mining program must remain running while recording transactions. This is not the default behaviour for IDLE on Mac OS however you can run two instances of Python from the Terminal
  
 - **Open and run the Transaction Recording program** 
  
    - Record a transaction by choosing “Record Transaction”
  
    - Enter the appropriate fields. The amount value must be of type integer for the program to accept it

- **Quickly check the Block Mining program and observe that it has found a hash value that contains exactly 14 0’s as per the requirements.**

- **You are now free to record another transaction following the same procedures as before, via the Transaction Recording program. The Block Mining program will continue to check for new transactions and provide the appropriate hash containing exactly 14 zeros as a result of the new transaction data**

