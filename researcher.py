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
            cur.execute("select products.name from Researchers join owns_a on Researchers.id = owns_a.Researcher_id join products on owns_a.product_id=products.code where Researchers.id = {}".format(Researcher_id))
            print("Devices Owned")
            for obj in cur:
                print (obj["name"])
        elif(column_name == "employees"):
            cur.execute("select * from employees;")
            # total man-hours, money, employees; order by
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

def createResearcher():
    fname = input("Please enter your ")

def Researcher(Researcher_id):
    con = pymysql.connect(host='localhost',
        port=30306,
        user="root",
        password="fckdna",
        db='bbk',
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