import pymysql
import mysql.connector as SQLC
import subprocess as sp

def show(Researcher_id, column_name, con):
    cur = con.cursor()
    try:
        if(column_name == "products"):
            # ask user if they want to filter by type; partial text match available
            filter1 = input("Filter by type: (smartphone/earphone/powerbank/speaker/all)")
            filter2 = input("Filter by brand: (Oppo/Vivo/OnePlus/all)")
            # order by
            order = input("Order by: (cost/sales/profit) ")
            if(filter1 == "all"):
                if(filter2 == "all"):
                    # select all from products and select brand from smartphones where smartphones.code = products.code
                    cur.execute("SELECT * FROM products ORDER BY " + order)
                else:
                    if(filter2 == "Oppo" or filter2 == "vivo" or filter2 == "OnePlus"):
                        cur.execute("SELECT * FROM products WHERE brand = '" + filter2 + "' ORDER BY " + order)
                    # else if there is partial text match
                    else:
                        cur.execute("SELECT * FROM products WHERE brand LIKE '%" + filter2 + "%' ORDER BY " + order)
            elif(filter1 == "smartphone" or filter1 == "earphone" or filter1 == "powerbank" or filter1 == "speaker"):
                    if(filter2 == "all"):
                        cur.execute("SELECT * FROM products WHERE type = '" + filter1 + "' ORDER BY " + order)
                    else:
                        if(filter2 == "Oppo" or filter2 == "vivo" or filter2 == "OnePlus"):
                            cur.execute("SELECT * FROM products WHERE type = '" + filter1 + "' AND brand = '" + filter2 + "' ORDER BY " + order)
                        # else if there's partial text match for filter2
                        else:
                            cur.execute("SELECT * FROM products WHERE type = '" + filter1 + "' AND brand LIKE '%" + filter2 + "%' ORDER BY " + order)
                # else if there is partial text match for filter1
            else:
                if(filter2 == "all"):
                    cur.execute("SELECT * FROM products WHERE type LIKE '%" + filter1 + "%' ORDER BY " + order)
                else:
                    if(filter2 == "Oppo" or filter2 == "vivo" or filter2 == "OnePlus"):
                        cur.execute("SELECT * FROM products WHERE type LIKE '%" + filter1 + "%' AND brand = '" + filter2 + "' ORDER BY " + order)
                    # else if there's partial text match for filter2
                    else:
                        cur.execute("SELECT * FROM products WHERE type LIKE '%" + filter1 + "%' AND brand LIKE '%" + filter2 + "%' ORDER BY " + order)
        # elif(column_name == "employees"):
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

def createResearcher():
    fname = input("Please enter your ")

def Researcher(Researcher_id):
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
        user_query = input("Enter query: ").split()
        if(len(user_query) > 0):
            if(user_query[0] == "exit"):
                return
            elif(user_query[0] == "show"):
                if(len(user_query) > 1):
                    if(user_query[1] == "devices"):
                        show(Researcher_id, "products", con)
                    elif(user_query[1] == "reviews"):
                        show(Researcher_id, "reviews", con)
                    else:
                        print("Invalid Arguments")
                else:
                    print("Insufficient Arguments")
            else:
                print("Invalid Argument")

    Researcher(1)