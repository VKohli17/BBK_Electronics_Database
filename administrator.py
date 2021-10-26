import pymysql
import mysql.connector as SQLC
import subprocess as sp
# from customer_interface import *

def searchList(L, value):
    for i in range(len(L)):
        if value == L[i]:
            return True
    return False

def display(column_name, con):
    cur = con.cursor()
    if(column_name == "employees"):
        cur.execute("select * from employees")
        print("Employees list")
        for obj in cur:
            print(obj["name"] + "\t" + obj["role"])
    
    cur = con.cursor()
    if(column_name == "products"):
        cur.execute("select * from products")
        print("Products Info List")
        for obj in cur:
            print(obj["name"] + "\t" + obj["code"] + "\t" + obj["cost"] + "\t" + obj["sales"] + "\t" + obj["profit"])

def Update(con):
    print("Option 1: Employee Data")
    print("Option 2: Product Info")
    
    option_selected = int(input("Enter selection: "))
    if(option_selected == 1):
        UpdateEmployeeInfo(con)
    if(option_selected == 2):
        UpdateProductsInfo(con)

def UpdateProductsInfo(con):
    cur = con.cursor()
    options = int(input("Enter id of Product"))
    
    query1 = "select * from products"
    cur.execute(query1)
    l = []
    for obj in cur:
        l.append(obj["id"])
        print(obj)    
    print(l)
    if not searchList(l,options):
        print("No Product with entered id")
        print("Find id(s) of product(s) here:")
        print(l)
    else:
        parameter = input("Enter the parameter to be updated: ")
        cur.execute(query1)
        l = []
        for obj in cur:
           l = list(obj.keys())
        print(l)

        if not searchList(l,parameter):
            print("Invalid parameter")
            print("Valid parameters: ")
            print(l)
        else:
            value = input("Enter the new value: ")
            query2 = "update products set " + parameter + " = " + value + " where id = " + str(options)
            print(query2)
            cur.execute(query2)
            con.commit()

def UpdateEmployeeInfo(con):
    try:
        cur = con.cursor()
        options = int(input("Enter id of Employee"))
        query1 = "select * from employees"
        cur.execute(query1)
        l = []
        for obj in cur:
            l.append(obj["id"])
            print(obj)    
        print(l)
        if not searchList(l,options):
            print("No Employee with entered id")
            print("Find id(s) of employee(s) here:")
            print(l)
        else:
            parameter = input("Enter the parameter to be updated: ")
            cur.execute(query1)
            l = []
            for obj in cur:
                l = list(obj.keys())
            print(l)

            if not searchList(l,parameter):
                print("Invalid parameter")
                print("Valid parameters: ")
                print(l)
            else:
                value = input("Enter the new value: ")
                query2 = "update employees set " + parameter + " = " + value + " where id = " + str(options)
                print(query2)
                cur.execute(query2)
                con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return



def Add(con):
    print("Option 1: Employee")
    print("Option 2: Product")
    option_selected = int(input("Enter selection: "))
    if(option_selected == 1):
        AddEmployee(con)
    if(option_selected == 2):
        AddProduct(con)

def AddEmployee(con):
    cur = con.cursor()
    info = {}
    info["id"] = int(input("SSN: "))
    info["name"] = input("Name: ")
    info["role"] = input("Role: ")
    info["team"] = input("Team: ")
    info["experince"]  = int(input("Experince: "))
    info["salary"] = int(input("Salary: "))
    info["leaves_used"] = 0;
    info["hours_spent"] = 0;
    
    query = "Insert into employees VALUES('%d', '%s', '%s', '%s', '%d', '%d', '%d', %d)" % (info["id"], info["name"], info["role"], info["team"], info["experience"], info["salary"], info["leaves_used"], info["hours_spent"])
    print(query)
    cur.execute(query)
    con.commit()
    
def AddProduct(con):
    print("Option 1: Add Smartphone")
    print("Option 2: Add Speaker")
    print("Option 3: Add TV")
    print("Option 4: Add Earphones")
    print("Option 5: Exit")
    ch = int(input("Enter Choice: "))
    if(ch==5):
        return
    elif(ch==1):
        AddSmartPhone(con)
    elif(ch==2):
        AddSpeaker(con)
    elif(ch==3):
        AddTV(con)
    elif(ch==4):
        AddEarphones(con)
    else:
        print("Invalid Input: Try Again")
        AddProduct(con)
    
def AddSmartPhone(con):
    try:
        cur = con.cursor()
        info = {}
        info["code"] = int(input("Product Code: "))
        info["battery"] = int(input("Battery: "))
        info["camera"] = int(input("Camera Resolution: "))
        info["charger"] = int(input("Charger Wattage: "))
        info["weight"] = int(input("Product Weight: "))
        info["dimensions"] = int(input("Length: "))
        #info["frame"] = input("Frame Material: ")
        info["frame"] = input("Frame Material: ")
        info["glass"] = input("Glass Material: ")
        info["soc"] = input("SOC: ")
        info["IP_rating"] = input("IP Rating: ")
        info["display"] = input("Display: ")
        info["brand"] = input("Brand: ")
        info["sub_brand"] = input("Sub-Brand ")
        query = "Insert into smartphone VALUES ('%d', '%d','%d','%d','%d','%d','%s','%s','%s','%s','%s','%s','%s')" %(info["code"],info["battery"],info["camera"],info["charger"], info["weight"],info["dimensions"],info["frame"],info["glass"],info["soc"],info["IP_rating"],info["display"],info["brand"],info["sub_brand"])
        cur.execute(query)
        con.commit()
        print("Inserted into the database")
    
    except Exception as e:
        con.rollback()
        print("Failed to Insert into database")
        print(">>>>>>>",e)
    return

def AddSpeaker(con):
    print("Didn't implement this functionality: Try Adding Smartphone")
    return

def AddTV(con):
    print("Didn't implement this functionality: Try Adding Smartphone")
    return

def AddEarphones(con):
    print("Didn't implement this functionality: Try Adding Smartphone")
    return        

def Administrator():
    con = pymysql.connect(host='localhost',
        port=30306,
        user="root",
        password="fckdna",
        db='bbk',
        cursorclass=pymysql.cursors.DictCursor)

    if(con.open):
        print("Connected")
    else:
        print("Failed to Connect")
        exit
        
    while(1):
        user_query =input("Enter a prompt:  ").split()
        if(len(user_query)>0):
            if(user_query[0] == "exit"):
                break
            elif(user_query[0] == "show"):
                if(len(user_query) > 1):
                    if(user_query[1] == "employees"):
                        print("executing")
                        display("employees",con)
                    elif(user_query[1] == "products"):
                        #show(1,"products",con)
                        display("products",con)
                    else:
                        print("Invalid Arguements 1")
                else:
                    print("Insufficient Arguements")
            
            elif(user_query[0] == "Update"):
                Update(con)
            elif(user_query[0] == "Add"):
                Add(con)    
                    
            
            
            else:
                print("Invalid Arguements 2") 
                        