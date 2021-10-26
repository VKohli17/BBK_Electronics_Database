import pymysql
import mysql.connector as SQLC
import subprocess as sp

def show(customer_id, column_name, con):
    cur = con.cursor()
    try:
        if(column_name == "products"):
            cur.execute("select products.name from customers join owns_a on customers.id = owns_a.customer_id join products on owns_a.product_id=products.code where customers.id = {}".format(customer_id))
            print("Devices Owned")
            for obj in cur:
                print (obj["name"])
        elif(column_name == "reviews"):
            cur.execute("select reviews.stars, reviews.review from customers join review on customers.id = review.customer_id join reviews on reviews.id=review.review_id where customers.id = {}".format(customer_id))
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

def createCustomer():
    fname = input("Please enter your ")

def Customer(customer_id):
    con = pymysql.connect(host='localhost',
        port=30306,
        user="root",
        password="dna",
        db='bbke',
        cursorclass=pymysql.cursors.DictCursor)

    if (con.open):
        print("Connected")
    else:
        print("Failed to Connect")
        exit

    while(1):
        user_query = input("Enter a prompt: ").split()
        if(len(user_query) > 0):
            if(user_query[0] == "exit"):
                return
            elif(user_query[0] == "show"):
                if(len(user_query) > 1):
                    if(user_query[1] == "devices"):
                        show(customer_id, "products", con)
                    elif(user_query[1] == "reviews"):
                        show(customer_id, "reviews", con)
                    else:
                        print("Invalid Arguments")
                else:
                    print("Insufficient Arguments")
            else:
                print("Invalid Argument")

Customer(1)