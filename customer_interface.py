import pymysql
import datetime
import mysql.connector as SQLC
import subprocess as sp

def show(customer_id, column_name, con):
    cur = con.cursor()
    try:
        if(column_name == "products"):
            cur.execute("select products.code, products.name from customers join owns_a on customers.id = owns_a.customer_id join products on owns_a.product_id=products.code where customers.id = {}".format(customer_id))
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
    con = pymysql.connect(host='localhost',
        port=30306,
        user="root",
        password="DNA",
        db='bbke',
        cursorclass=pymysql.cursors.DictCursor)
    fname = input("Please enter your First Name: ")
    lname = input("Please enter your Last Name: ")
    prem = input("Are you a Premium Customer(yes/no): ").lower()
    gender = input("Please enter your preferred gender: ")
    city = input("Please enter your City name: ")
    state = input("Please enter your State name: ")
    country = input("Please enter your Country name: ")
    dob = input("Please enter your Date of Birth in the form YYYY-MM-DD: ")
    # dobcopy = dob[:]
    y,m,d = dob.split('-')
    birth_date = datetime.date(int(y), int(m), int(d))
    # get datetime.date for today
    today = datetime.date.today()
    age = int((today - birth_date).days / 365.2425)

    cur = con.cursor()
    retrieve_id = con.cursor()
    try:
        cur.execute("insert into customers (first_name, last_name, premium_customer, gender, city, state, country, dob, age) values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {})".format(fname, lname, prem, gender, city, state, country, dob, age))
        con.commit()
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
            con.close()
    try:
        retrieve_id.execute("select MAX(id) as CID from customers;")
        print("Your Customer ID to be used for login is: {}".format(retrieve_id.fetchone()["CID"]))
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
            con.close()



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

    try:
        cur = con.cursor()
        cur.execute("select id from customers where id={};".format(customer_id))
        if(cur.fetchone() == None):
            print("Customer ID not found")
            return None
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

    while(1):
        user_query = input("Enter a prompt: ").split()
        if(len(user_query) > 0):
            if(user_query[0] == "exit"):
                con.close()
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

Customer(4)