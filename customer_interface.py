import pymysql
import datetime
import mysql.connector as SQLC
import subprocess as sp

def showmy(customer_id, column_name, con):
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

def buyProduct(customer_id, con):
    pname = input("Please enter the name of the product you want to buy: ")
    try:
        cur = con.cursor()
        codes = []
        cur.execute("select code, name from products where name like '%{}%'".format(pname))
        print("Code\tProduct Name")
        for obj in cur:
            print (str(obj["code"]) + "\t" + obj["name"])
            codes.append(obj["code"])
        code = int(input("Please enter the code of the product you want to buy: "))
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
    if(code in codes):
        try:
            cur = con.cursor()
            cur.execute("insert into owns_a (customer_id, product_id) values ({}, {})".format(customer_id, code))
            con.commit()
            print("Product Bought")
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
    else:
        print("Invalid Code")

def createReview(customer_id, con):
    pname = input("Please enter the name of the product you want to review: ")
    try:
        cur = con.cursor()
        codes = []
        cur.execute("select products.code, products.name from customers join owns_a on customers.id = owns_a.customer_id join products on owns_a.product_id=products.code where customers.id = {} and products.name like '%{}%';".format(customer_id, pname))
        print("Code\tProduct Name")
        for obj in cur:
            print (str(obj["code"]) + "\t" + obj["name"])
            codes.append(obj["code"])
        code = int(input("Please enter the code of the product you want to review: "))
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
    if(code in codes):
        stars = int(input("Please enter the number of stars you want to give to the product: "))
        if(stars > 5 or stars < 1):
            print("Invalid Stars")
            return None
        review = input("Please enter your review:\n")
        try:
            cur = con.cursor()
            cur.execute("insert into reviews (stars, review) values ({}, '{}');".format(stars, review))
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
            con.commit()
        review_id = 0
        try:
            cur = con.cursor()
            cur.execute("select MAX(id) as review_id from reviews;".format(stars, review))
            review_id = cur.fetchone()["review_id"]
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
        try:
            cur = con.cursor()
            cur.execute("insert into review values ({}, {}, {});".format(customer_id, code, review_id))
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
            con.commit()
    else:
        print("Invalid Code")

def showReviews(con):
    pname = input("Please enter the name of the product you want to see reviews of: ")
    try:
        cur = con.cursor()
        codes = []
        cur.execute("select products.code, products.name from products where products.name like '%{}%';".format(pname))
        print("Code\tProduct Name")
        for obj in cur:
            print (str(obj["code"]) + "\t" + obj["name"])
            codes.append(obj["code"])
        code = int(input("Please enter the code of the product you want to see reviews of: "))
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
    if(code in codes):
        try:
            cur = con.cursor()
            cur.execute("select reviews.stars, reviews.review from reviews join review on review.review_id = reviews.id join products on review.product_id = {};".format(code))
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
    else:
        print("Invalid Code")

def showDevices(con):
    try:
        cur = con.cursor()
        print("Smartphones:")
        cur.execute("select name, cost, brand from products where type='smartphone';")
        print("Name\tCost\tBrand")
        for obj in cur:
            print (obj["name"] + "\t" + str(obj["cost"]) + "\t" + obj["brand"])
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

    try:
        cur = con.cursor()
        print("Earphones:")
        cur.execute("select name, cost, brand from products where type='earphone';")
        print("Name\tCost\tBrand")
        for obj in cur:
            print (obj["name"] + "\t" + str(obj["cost"]) + "\t" + obj["brand"])
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

    try:
        cur = con.cursor()
        print("Powerbanks:")
        cur.execute("select name, cost, brand from products where type='powerbank';")
        print("Name\tCost\tBrand")
        for obj in cur:
            print (obj["name"] + "\t" + str(obj["cost"]) + "\t" + obj["brand"])
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

    try:
        cur = con.cursor()
        print("Speakers:")
        cur.execute("select name, cost, brand from products where type='speaker';")
        print("Name\tCost\tBrand")
        for obj in cur:
            print (obj["name"] + "\t" + str(obj["cost"]) + "\t" + obj["brand"])
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

    try:
        cur = con.cursor()
        print("TVs:")
        cur.execute("select name, cost, brand from products where type='tv';")
        print("Name\tCost\tBrand")
        for obj in cur:
            print (obj["name"] + "\t" + str(obj["cost"]) + "\t" + obj["brand"])
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



def Customer(customer_id):
    con = pymysql.connect(host='localhost',
        port=30306,
        user="root",
        password="DNA",
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
                if(len(user_query) > 2):
                    if(user_query[2] == "devices" and user_query[1] == "my"):
                        showmy(customer_id, "products", con)
                    elif(user_query[2] == "reviews" and user_query[1] == "my"):
                        showmy(customer_id, "reviews", con)
                    else:
                        print("Invalid Arguments")
                elif(len(user_query) > 1):
                    if(user_query[1] == "reviews"):
                        showReviews(con)
                    elif(user_query[1] == "devices"):
                        showDevices(con)
                    else:
                        print("Invalid Arguments")
                else:
                    print("Insufficient Arguments")
            elif(user_query[0] == "buy"):
                buyProduct(customer_id, con)
            elif(user_query[0] == "review"):
                createReview(customer_id, con)
            else:
                print("Invalid Argument")

Customer(3)