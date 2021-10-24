import pymysql
import mysql.connector as SQLC
import subprocess as sp
from customer_interface import *
from administrator import *
while(1):
    tmp = sp.call('clear',shell=True)
    
    print("1. Login as Customer: ")
    print("2. Login as Inventory Manager")
    print("3. Login as Administrator")
    print("4. Login as Researcher")
    print("5. Exit")
    
    ch = int(input("Enter Choice> "))
    if(ch==5):
        exit()
    
    
    tmp = sp.call('clear', shell=True)
    
    Username = input("Username: ")
    Password = input("Password: ")
    
    if(Username!="admin" or Password!="password"):
        print("Invalid Username or Password")
        exit()
    
    if(ch==1):
        print()
        Customer(1)
        
    if(ch==2):
        InventoryManager()
    
    if(ch==3):
        Administrator()
        
    if(ch==4):
        Researcher()
    
    

