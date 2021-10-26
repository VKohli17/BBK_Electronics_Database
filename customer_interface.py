import pymysql
import datetime
import mysql.connector as SQLC
import subprocess as sp
from prettytable import PrettyTable

def editmyReview(customer_id, con):
    codes = []
    try:
        cur = con.cursor()
        cur.execute("select reviews.id, reviews.stars, products.name, reviews.review from customers join review on customers.id = review.customer_id join reviews on reviews.id=review.review_id join products on products.code = review.product_id where customers.id = {}".format(customer_id))
        table = PrettyTable()
        table.field_names = ["Review ID", "Stars", "Product Name", "Review"]
        rows = cur.fetchall()
        for row in rows:
            table.add_row([row["id"], row["stars"], row["name"], row["review"]])
            codes.append(row["id"])
        print(table)
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
    code = int(input("Please enter the ID of the review you wish to edit: "))
    if(code in codes):
        try:
            cur = con.cursor()
            stars = int(input("Please enter the new number of stars: "))
            review = input("Please enter the new review: ")
            cur.execute("update reviews set stars = {}, review = '{}' where id = {}".format(stars, review, code))
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
        print("Invalid ID")

def editMe(customer_id, con):
    row = {}
    try:
        cur = con.cursor()
        cur.execute("select * from customers where id = {}".format(customer_id))
        row = cur.fetchone().copy()
        table = PrettyTable()
        temp = []
        for key in row.keys():
            temp.append(key)
        table.field_names = temp
        table.add_row(list(row.values()))
        print(table)
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

    changedCol = input("Please enter the column name you wish to change: ")
    newValue = input("Please enter the new value: ")

    if(changedCol in row.keys() and changedCol != "dob" and changedCol != "id" and changedCol != "age"):
        try:
            cur = con.cursor()
            cur.execute("update customers set {} = '{}' where id = {}".format(changedCol, newValue, customer_id))
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
    elif(changedCol == "dob"):
        try:
            cur = con.cursor()
            y,m,d = str(newValue).split('-')
            birth_date = datetime.date(int(y), int(m), int(d))
            # get datetime.date for today
            today = datetime.date.today()
            age = int((today - birth_date).days / 365.2425)
            cur.execute("update customers set {} = '{}', age = '{}' where id = {}".format(changedCol, newValue, age, customer_id))
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
        print("Invalid column name")

def showmy(customer_id, column_name, con):
    cur = con.cursor()
    try:
        if(column_name == "products"):
            cur.execute("select products.name, products.brand, products.type from customers join owns_a on customers.id = owns_a.customer_id join products on owns_a.product_id=products.code where customers.id = {}".format(customer_id))
            print("Devices Owned")
            table = PrettyTable()
            table.field_names = ["Device Name", "Brand", "Type"]
            rows = cur.fetchall()
            for row in rows:
                table.add_row([row["name"], row["brand"], row["type"]])
            print(table)
        elif(column_name == "reviews"):
            cur.execute("select reviews.stars, reviews.review, products.name from customers join review on customers.id = review.customer_id join reviews on reviews.id=review.review_id join products on products.code = review.product_id where customers.id = {}".format(customer_id))
            table = PrettyTable()
            table.field_names = ["Stars", "Review", "Product Name"]
            rows = cur.fetchall()
            for row in rows:
                table.add_row([row["stars"], row["review"], row["name"]])
            print(table)
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
    pw = input("Please enter your password: ")
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
        cur.execute("insert into customers (password, first_name, last_name, premium_customer, gender, city, state, country, dob, age) values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {})".format(pw, fname, lname, prem, gender, city, state, country, dob, age))
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
        retrieve_id.close()
        con.close()

def buyProduct(customer_id, con):
    pname = input("Please enter the name of the product you want to buy: ")
    try:
        cur = con.cursor()
        codes = []
        cur.execute("select code, name, brand from products where name like '%{}%'".format(pname))
        table = PrettyTable()
        table.field_names = ["Code", "Product Name", "Brand"]
        rows = cur.fetchall()
        for row in rows:
            table.add_row([row["code"], row["name"], row["brand"]])
            codes.append(row["code"])
        print(table)
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
            con.commit()
        
        try:
            cur = con.cursor()
            cur.execute("update products set sales = sales + 1 where code = {}".format(code))
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
            con.commit()
    else:
        print("Invalid Code")

def createReview(customer_id, con):
    pname = input("Please enter the name of the product you want to review: ")
    try:
        cur = con.cursor()
        codes = []
        cur.execute("select products.code, products.name, products.brand from customers join owns_a on customers.id = owns_a.customer_id join products on owns_a.product_id=products.code where customers.id = {} and products.name like '%{}%';".format(customer_id, pname))

        table = PrettyTable()
        table.field_names = ["Code", "Product Name", "Brand"]
        rows = cur.fetchall()
        for row in rows:
            table.add_row([row["code"], row["name"], row["brand"]])
            codes.append(row["code"])
        print(table)
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
        cur.execute("select products.code, products.name, products.brand from products where products.name like '%{}%';".format(pname))
        table = PrettyTable()
        table.field_names = ["Code", "Product Name", "Brand"]
        rows = cur.fetchall()
        for row in rows:
            table.add_row([row["code"], row["name"], row["brand"]])
            codes.append(row["code"])
        print(table)
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
            cur.execute("select reviews.stars, reviews.review from reviews join review on review.review_id = reviews.id join products on review.product_id = products.code where products.code = {};".format(code))
            table = PrettyTable()
            table.field_names = ["Stars", "Review"]
            rows = cur.fetchall()
            for row in rows:
                table.add_row([row["stars"], row["review"]])
            print(table)
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
        table = PrettyTable()
        table.field_names = ["Name", "Cost", "Brand"]
        rows = cur.fetchall()
        for row in rows:
            table.add_row([row["name"], row["cost"], row["brand"]])
        print(table)
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
        table = PrettyTable()
        table.field_names = ["Name", "Cost", "Brand"]
        rows = cur.fetchall()
        for row in rows:
            table.add_row([row["name"], row["cost"], row["brand"]])
        print(table)
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
        table = PrettyTable()
        table.field_names = ["Name", "Cost", "Brand"]
        rows = cur.fetchall()
        for row in rows:
            table.add_row([row["name"], row["cost"], row["brand"]])
        print(table)
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
        table = PrettyTable()
        table.field_names = ["Name", "Cost", "Brand"]
        rows = cur.fetchall()
        for row in rows:
            table.add_row([row["name"], row["cost"], row["brand"]])
        print(table)
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
        table = PrettyTable()
        table.field_names = ["Name", "Cost", "Brand"]
        rows = cur.fetchall()
        for row in rows:
            table.add_row([row["name"], row["cost"], row["brand"]])
        print(table)
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

def deletemyReview(customer_id, con):
    codes = []
    try:
        cur = con.cursor()
        cur.execute("select reviews.id, reviews.stars, products.name, reviews.review from customers join review on customers.id = review.customer_id join reviews on reviews.id=review.review_id join products on products.code = review.product_id where customers.id = {}".format(customer_id))
        table = PrettyTable()
        table.field_names = ["Review ID", "Stars", "Product Name", "Review"]
        rows = cur.fetchall()
        for row in rows:
            table.add_row([row["id"], row["stars"], row["name"], row["review"]])
            codes.append(row["id"])
        print(table)
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
    code = int(input("Please enter the ID of the review you wish to delete: "))
    if(code in codes):
        check = input("Are you sure you want to delete this review? (type 'Delete' to confirm)\n")
        if(check == "Delete"):
            try:
                cur = con.cursor()
                cur.execute("delete from review where review.review_id = {}".format(code))
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
            try:
                cur = con.cursor()
                cur.execute("delete from reviews where reviews.id = {}".format(code))
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
        print("Invalid ID")

def deletemyDevice(customer_id, con):
    codes = []
    try:
        cur = con.cursor()
        cur.execute("select products.code, products.name from customers join owns_a on customers.id = owns_a.customer_id join products on owns_a.product_id = products.code where customers.id = {}".format(customer_id))
        table = PrettyTable()
        table.field_names = ["Code", "Name"]
        rows = cur.fetchall()
        for row in rows:
            codes.append(row["code"])
            table.add_row([row["code"], row["name"]])
        print(table)
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
    code = int(input("Please enter the ID of the device you wish to return: "))
    if(code in codes):
        check = input("Are you sure you want to return this device? (type 'Return' to confirm)\n")
        if(check == "Return"):
            try:
                cur = con.cursor()
                cur.execute("delete from owns_a where product_id = {}".format(code))
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
        print("Invalid ID")

def deleteMe(customer_id, con):
    check = input("Are you sure you want to delete this customer? (type 'Delete' to confirm)\n")
    if(check == "Delete"):
        try:
            cur = con.cursor()
            cur.execute("delete from owns_a where customer_id = {}".format(customer_id))
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

        review_id = []

        try:
            cur = con.cursor()
            cur.execute("select review_id from review where customer_id = {}".format(customer_id))
            rows = cur.fetchall()
            for row in rows:
                review_id.append(row["review_id"])
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

        for i in review_id:
            try:
                cur = con.cursor()
                cur.execute("delete from reviews where id = {}".format(i))
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
        
        try:
            cur = con.cursor()
            cur.execute("delete from review where customer_id = {}".format(customer_id))
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

        try:
            cur = con.cursor()
            cur.execute("delete from customers where id = {}".format(customer_id))
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
    
def Customer(customer_id, password):
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
        cur.execute("select password, first_name from customers where id={};".format(customer_id))
        acc = cur.fetchone()
        if(acc == None):
            tmp = sp.call('clear',shell=True)
            print("Customer ID not found")
            temp = input("Press Enter to Continue...")
            return None
        elif(acc["password"] == password):
            tmp = sp.call('clear',shell=True)
            print("Welcome back, {}".format(acc["first_name"]))
        elif(acc["password"] != password):
            tmp = sp.call('clear',shell=True)
            print("Incorrect Password")
            temp = input("Press Enter to Continue...")
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
        tmp = sp.call('clear',shell=True)
    
        print("1. Show all Devices")
        print("2. Show my Devices")
        print("3. Show all Reviews for a Product")
        print("4. Show my Reviews")
        print("5. Add a Review")
        print("6. Edit a Review")
        print("7. Delete a Review")
        print("8. Buy a Device")
        print("9. Return a Device")
        print("10. Edit my Account")
        print("11. Delete my Account")
        print("12. Logout")
        
        ch = int(input("Enter Choice> "))

        if(ch == 1):
            tmp = sp.call('clear',shell=True)
            showDevices(con)
            input("Press Enter to Continue...")
        if(ch == 2):
            tmp = sp.call('clear',shell=True)
            showmy(customer_id, "products", con)
            input("Press Enter to Continue...")
        if(ch == 3):
            tmp = sp.call('clear',shell=True)
            showReviews(con)
            input("Press Enter to Continue...")
        if(ch == 4):
            tmp = sp.call('clear',shell=True)
            showmy(customer_id, "reviews", con)
            input("Press Enter to Continue...")
        if(ch == 5):
            tmp = sp.call('clear',shell=True)
            createReview(customer_id, con)
        if(ch == 6):
            tmp = sp.call('clear',shell=True)
            editmyReview(customer_id, con)
        if(ch == 7):
            tmp = sp.call('clear',shell=True)
            deletemyReview(customer_id, con)
        if(ch == 8):
            tmp = sp.call('clear',shell=True)
            buyProduct(customer_id, con)
        if(ch == 9):
            tmp = sp.call('clear',shell=True)
            deletemyDevice(customer_id, con)
        if(ch == 10):
            tmp = sp.call('clear',shell=True)
            editMe(customer_id, con)

        if(ch == 11):
            tmp = sp.call('clear',shell=True)
            deleteMe(customer_id, con)
            break
        if(ch == 12):
            tmp = sp.call('clear',shell=True)
            break
        # user_query = input("Enter a prompt: ").split()
        # if(len(user_query) > 0):
        #     if(user_query[0] == "exit"):
        #         con.close()
        #         return
        #     elif(user_query[0] == "show"):
        #         if(len(user_query) > 2):
        #             if(user_query[2] == "devices" and user_query[1] == "my"):
        #                 showmy(customer_id, "products", con)
        #             elif(user_query[2] == "reviews" and user_query[1] == "my"):
        #                 showmy(customer_id, "reviews", con)
        #             else:
        #                 print("Invalid Arguments")
        #         elif(len(user_query) > 1):
        #             if(user_query[1] == "reviews"):
        #                 showReviews(con)
        #             elif(user_query[1] == "devices"):
        #                 showDevices(con)
        #             else:
        #                 print("Invalid Arguments")
        #         else:
        #             print("Insufficient Arguments")
        #     elif(user_query[0] == "edit"):
        #         if(len(user_query) > 1):
        #             if(user_query[1] == "review"):
        #                 editmyReview(customer_id, con)
        #             elif(user_query[1] == "me"):
        #                 editMe(customer_id, con)
        #             else:
        #                 print("Invalid Arguments")
        #     elif(user_query[0] == "delete"):
        #         if(len(user_query) > 1):
        #             if(user_query[1] == "review"):
        #                 deletemyReview(customer_id, con)
        #             elif(user_query[1] == "device"):
        #                 deletemyDevice(customer_id, con)
        #             elif(user_query[1] == "me"):
        #                 deleteMe(customer_id, con)
        #                 break
        #             else:
        #                 print("Invalid Arguments")
        #     elif(user_query[0] == "buy"):
        #         buyProduct(customer_id, con)
        #     elif(user_query[0] == "review"):
        #         createReview(customer_id, con)
        #     else:
        #         print("Invalid Argument")

# Customer(3)