import pymysql
import mysql.connector as SQLC
import subprocess as sp
from customer_interface import *
from administrator import *
from researcher import *
while(1):
    tmp = sp.call('clear',shell=True)
    
    print("1. Login as Customer: ")
    print("2. Login as Administrator")
    print("3. Login as Researcher")
    print("4. Create Customer Account")
    print("5. Exit")
    
    ch = int(input("Enter Choice> "))

    try:

        if(ch==5):
            exit()
        
        tmp = sp.call('clear', shell=True)
                
        if(ch==1):
            ID = int(input("Customer ID: "))        
            Customer(ID)
        
        elif(ch==2):
            Username = input("Username: ")
            Password = input("Password: ")
            if(Username!="admin" or Password!="password"):
                Administrator()
            
        elif(ch==3):
            Username = input("Username: ")
            Password = input("Password: ")
            Researcher()

        elif(ch==4):
            createCustomer()
            idk = input("Press enter to continue")
    
    except Exception as e:
        print(e)
        randomvariable = input("Press enter to continue")
        continue
