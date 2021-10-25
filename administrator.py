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

        


def show(customer_id, column_name, con):
    cur = con.cursor()
    try:
        if(column_name == "products"):
            cur.execute("select products.name from customers join owns_a on customers.id = owns_a.customer_id join products on owns_a.product_id=products.code")
            print("Devices Owned")
            for obj in cur:
                print (obj["name"])
        elif(column_name == "reviews"):
            cur.execute("select reviews.stars, reviews.review from customers join review on customers.id = review.customer_id join reviews on reviews.id=review.review_id")
            print("Stars\tReview")
            for obj in cur:
                print (str(obj["stars"]) + "\t" + obj["review"])
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
                    
            
            
            else:
                print("Invalid Arguements 2") 
                        