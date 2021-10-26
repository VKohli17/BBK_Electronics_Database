import pymysql
import mysql.connector as SQLC
import subprocess as sp
# from customer_interface import *

def searchList(L, value):
    for i in range(len(L)):
        if value == L[i]:
            return True
    return False

def delete(con):
    print("Option 1: Fire an Employee")
    print("option 2: Delete a product")
    print("option 3: Back Page")
    ch = int(input("Enter the option: "))
    if(ch==3):
        return
    elif(ch==1):
        FireEmployee(con)
    elif(ch==2):
        DeleteProduct(con)
    else:
        print("Invalid Argument")
        delete(con)

def FireEmployee(con):
    cur = con.cursor()
    cur.execute("select * from employees")
    l = []
    for obj in cur:
        l.append(obj["id"])
    ssn = int(input("Enter the id of the employee to be fired: "))
    if not searchList(l,ssn):
        print("No employees found")
        print("The valid ids of employees are: ")
        print(l)
        FireEmployee(con)
    else:
        query = "Delete from employees where id = '%d'" % (ssn)
        try:
            cur.execute(query)
            con.commit()
        except Exception as e:
            print("Failed to delete Employee ")
            print(">>>>>>>>>",e)
    return
        

def DeleteProduct(con):
    cur = con.cursor()
    cur.execute("select * from products")
    l = []
    for obj in cur:
        l.append(obj["id"])
    code = int(input("Enter the id of the Product to be deleted: "))
    if not searchList(l,code):
        print("No products found")
        print("The valid ids of products are: ")
        print(l)
        DeleteProduct(con)
    else:
        query = "Delete from products where code = '%d'" % (code)
        try:
            cur.execute(query)
            con.commit()
        except Exception as e:
            print("Failed to delete Product ")
            print(">>>>>>>>>",e)
    return

def display(column_name, con):
    cur = con.cursor()
    if(column_name == "employees"):
        cur.execute("select * from employees")
        print("Employees list")
        for obj in cur:
            print(obj["name"] + "\t" + obj["role"] + "\t" + str(obj["id"]) + "\t" + obj["team"])
    
    cur = con.cursor()
    if(column_name == "products"):
        cur.execute("select * from products")
        print("Products Info List")
        for obj in cur:
            print(obj["name"] + "\t" + str(obj["code"]) + "\t" + str(obj["cost"]) + "\t" + str(obj["sales"]) + "\t" + str(obj["profit"]))

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
        UpdateProductsInfo(con)
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
            UpdateEmployeeInfo(con)
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
                value1 = input("Enter the new value: ")
                query2 = "update employees set " + parameter + " = '" + value1 + "' where id = " + str(options) + ";"
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
    info["experience"]  = int(input("Experience: "))
    info["salary"] = int(input("Salary: "))
    info["leaves_used"] = 0;
    info["hours_spent"] = 0;
    
    query = "Insert into employees VALUES('%d', '%s', '%s', '%s', '%d', '%d', '%d', '%d')" % (info["id"], info["name"], info["role"], info["team"], info["experience"], info["salary"], info["leaves_used"], info["hours_spent"])
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
    info = {}
    info["name"] = input("Product Name: ")
    info["cost"] = int(input("Cost: "))
    info["making"] - int(input("Manufacturinig_Cost: "))
    info["battery"] = int(input("Battery: "))
    info["camera"] = int(input("Camera Resolution: "))
    info["charger"] = int(input("Charger Wattage: "))
    info["weight"] = int(input("Product Weight: "))
    info["launch_date"] = input("Launch Date: ")
    info["dimensions"] = int(input("Length: "))
    #info["frame"] = input("Frame Material: ")
    info["frame"] = input("Frame Material: ")
    info["glass"] = input("Glass Material: ")
    info["soc"] = input("SOC: ")
    info["IP_rating"] = input("IP Rating: ")
    info["display"] = input("Display: ")
    info["brand"] = input("Brand: ")
    info["sub_brand"] = input("Sub-Brand ")
    profit = info["cost"] - info["making"]
    query2 = "Insert into products (name, cost, sales, profit, launch_date, weekly_production, type, brand, sub_brand) values ('{}', {}, {}, {}, '{}', {}, '{}', '{}', '{}')".format(info["name"], info["cost"], 0,profit,info["launch_date"],10000,"Smartphone",info["brand"], info["sub_brand"])
    try:
        cur = con.cursor()
        cur.execute(query2)
    except pymysql.Error as e:
        try:
            con.rollback()
            print("Failed to Insert into database")
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return None
        except IndexError:
            print("MySQL Error: %s" % str(e))
            return None
        except TypeError as e:
            print(e)
            return None
        except ValueError as e:
            print(e)
            return None
    finally:
        cur.close()
    
    try:
        cur = con.cursor()
        cur.execute("select MAX(code) as new_product from products;")
        pcode = cur.fetchone()["code"]
    except pymysql.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return None
        except IndexError:
            print("MySQL Error: %s" % str(e))
            return None
        except TypeError as e:
            print(e)
            return None
        except ValueError as e:
            print(e)
            return None
    finally:
        cur.close()

    query = "Insert into smartphone values ({}, {}, {}, {}, {}, {}, '{}', '{}', '{}', '{}', '{}')".format(pcode,info["battery"],info["camera"],info["charger"], info["weight"],info["dimensions"],info["frame"],info["glass"],info["soc"],info["IP_rating"],info["display"])

    try:
        cur = con.cursor()
        cur.execute(query)
        print("Inserted into the database")
    except pymysql.Error as e:
        try:
            con.rollback()
            print("Failed to Insert into database")
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            return None
        except IndexError:
            print("MySQL Error: %s" % str(e))
            return None
        except TypeError as e:
            print(e)
            return None
        except ValueError as e:
            print(e)
            return None
    finally:
        cur.close()
        con.commit()
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

def ShowInfo(con):
    print("Option 1: Products")
    print("Option 2: Employees")
    print("Option 3: Back Page")
    ch = int(input("Enter the option"))
    if(ch==3):
        return
    elif(ch==1):
        display("products",con)
    elif(ch==2):
        display("employees",con)
    else:
        print("Invalid Argument")
        ShowInfo(con)

def Administrator():
    con = pymysql.connect(host='localhost',
        port=30306,
        user="root",
        password="dna",
        db='bbke',
        cursorclass=pymysql.cursors.DictCursor)

    if(con.open):
        print("Connected")
    else:
        print("Failed to Connect")
        exit
        
    while(1):
        print("Option 1: Show info")
        print("Option 2: Update Info")
        print("Option 3: Add info")
        print("Option 4: Delete data/Fire Employee")
        print("Option 4: Back Page")
        
        user_query =int(input("Enter the option:  "))
        if(user_query == 1):
            ShowInfo()
        elif(user_query == 2):
            Update(con)
        elif(user_query == 3):
            Add(con)
        elif(user_query == 4):
            delete(con)
        elif(user_query == 5):
            return
        else:
            print("Invalid Argument")