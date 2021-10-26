import pymysql
import mysql.connector as SQLC
import subprocess as sp
from customer_interface import *
from administrator import *
from researcher import *
while(1):
    tmp = sp.call('clear',shell=True)
    
    print("1. Login as Customer: ")
    print("2. Login as Inventory Manager")
    print("3. Login as Administrator")
    print("4. Login as Researcher")
    print("5. Create Customer Account")
    print("6. Exit")
    
    ch = int(input("Enter Choice> "))
    if(ch==6):
        exit()
    
    
    tmp = sp.call('clear', shell=True)
    
    
    
    
    
    if(ch==1):
        print()
        Customer(1)
        
    elif(ch==2):
        InventoryManager()
    
    elif(ch==3):
        Username = input("Username: ")
        Password = input("Password: ")
        if(Username!="admin" or Password!="password"):
            Administrator()
        
    elif(ch==4):
        Username = input("Username: ")
        Password = input("Password: ")
        Researcher()

    elif(ch==5):
        CreateCustomer()
    
    

