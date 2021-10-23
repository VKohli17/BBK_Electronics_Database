import pymysql
import mysql.connector as SQLC
import subprocess as sp
import customer_interface


def Customer():
    while(1):
        tmp = sp.call('clear', shell=True)

def InventoryManager():
    while(1):
        tmp = sp.call('clear', shell=True)
        
def Administrator():
    while(1):
        tmp = sp.call('clear', shell=True)
        
def Researcher():
    while(1):
        tmp = sp.call('clear', shell=True)
    


while(1):
    tmp = sp.call('clear',shell=True)
    
    print("1. Login as Customer: ")
    print("2. Login as Inventory Manager")
    print("3. Login as Administrator")
    print("4. Login as Researcher")
    print("5. Exit")
    
    ch = int(input("Enter Choice> "))
    tmp = sp.call('clear', shell=True)
    
    Username = input("Username: ")
    Password = input("Password: ")
    
    if(Username!="admin" or Password!="password"):
        print("Invalid Username or Password")
        exit()
    
    if(ch==1):
        Customer()
        
    if(ch==2):
        InventoryManager()
    
    if(ch==3):
        Administrator()
        
    if(ch==4):
        Researcher()
    
    if(ch==5):
        exit()
    

