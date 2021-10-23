import pymysql
import mysql.connector as SQLC
import subprocess as sp

def search(list,n):
    for i in range(len(list)):
        if list[i]==n:
            return True
    return False

def Interface():
    cursor = connect_db()
    query = "Select product_code from Products"

    cursor.execute(query)
    product_code_list = [i[0] for i in cursor.fetchall()]

    Product = input("Product Code of the product/project you wish to generate report about: ")
    tmp = sp.call('clear',shell=True)
    
    if not search(product_code_list,Product):
        print("No Product/Project with such id")
        return
        
    print("Choose the Type of report: ")
    print("Option 1. Stock Analysis")
    print("Sales Purchase Analysis")
    print("Customer Review Analysis")
    
    ch = int(input("Enter Choice> "))
    tmp = sp.call('clear',shell=True)
    
    if ch==1:
        query = ""
    if ch==2:
        query = ""
    if ch==3:
        query = ""
    
    cursor.execute(query)
    
    
        
    