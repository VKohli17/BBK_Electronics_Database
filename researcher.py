import pymysql
import mysql.connector as SQLC
import subprocess as sp
from prettytable import PrettyTable

def show(column_name, con):
    cur = con.cursor()
    try:
        if(column_name == "products"):
            # ask user if they want to filter by type; partial text match available
            filter1 = input("Filter by type: (smartphone/earphone/powerbank/speaker/all) ")
            filter2 = input("Filter by brand: (oppo/vivo/oneplus/all) ")
            # order by
            order = input("Order by: (cost/sales/profit) ")
            x = PrettyTable()
            x.field_names = ["Code", "Name", "Type", "Brand", "Cost", "Sales", "Profit", "Launch date", "Weekly production"]
            if(filter1 == "all"):
                if(filter2 == "all"):
                    # select all from products and select brand from smartphones where smartphones.code = products.code
                    cur.execute("SELECT * FROM products ORDER BY " + order + ";")
                    # print the results in a table with borders and column names
                    for row in cur.fetchall():
                        x.add_row([row["code"], row["name"], row["type"], row["brand"], row["cost"], row["sales"], row["profit"], row["launch_date"], row["weekly_production"]])
                        # print(str(row['code']) + " " + row['name'] + " " + row['type'] + " " + row['brand'] + " " + str(row['cost']) + " " + str(row['sales']) + " " + str(row['profit']))
                    print(x)
                else:
                    if(filter2 == "oppo" or filter2 == "vivo" or filter2 == "oneplus"):
                        cur.execute("SELECT * FROM products WHERE brand = '" + filter2 + "' ORDER BY " + order + ";")
                        # print the results in a table
                        for row in cur.fetchall():
                            x.add_row([row["code"], row["name"], row["type"], row["brand"], row["cost"], row["sales"], row["profit"], row["launch_date"], row["weekly_production"]])
                        print(x)
                    # else if there is partial text match
                    else:
                        cur.execute("SELECT * FROM products WHERE brand LIKE '%" + filter2 + "%' ORDER BY " + order + ";")
                        # print the results in a table
                        for row in cur.fetchall():
                            x.add_row([row["code"], row["name"], row["type"], row["brand"], row["cost"], row["sales"], row["profit"], row["launch_date"], row["weekly_production"]])
                        print(x)
            elif(filter1 == "smartphone" or filter1 == "earphone" or filter1 == "powerbank" or filter1 == "speaker"):
                    if(filter2 == "all"):
                        cur.execute("SELECT * FROM products WHERE type = '" + filter1 + "' ORDER BY " + order + ";")
                        # print the results in a table
                        for row in cur.fetchall():
                            x.add_row([row["code"], row["name"], row["type"], row["brand"], row["cost"], row["sales"], row["profit"], row["launch_date"], row["weekly_production"]])
                        print(x)
                    else:
                        if(filter2 == "oppo" or filter2 == "vivo" or filter2 == "oneplus"):
                            cur.execute("SELECT * FROM products WHERE type = '" + filter1 + "' AND brand = '" + filter2 + "' ORDER BY " + order + ";")
                            # print the results in a table
                            for row in cur.fetchall():
                                x.add_row([row["code"], row["name"], row["type"], row["brand"], row["cost"], row["sales"], row["profit"], row["launch_date"], row["weekly_production"]])
                            print(x)
                        # else if there's partial text match for filter2
                        else:
                            cur.execute("SELECT * FROM products WHERE type = '" + filter1 + "' AND brand LIKE '%" + filter2 + "%' ORDER BY " + order + ";")
                            # print the results in a table
                            for row in cur.fetchall():
                                x.add_row([row["code"], row["name"], row["type"], row["brand"], row["cost"], row["sales"], row["profit"], row["launch_date"], row["weekly_production"]])
                            print(x)
                # else if there is partial text match for filter1
            else:
                if(filter2 == "all"):
                    cur.execute("SELECT * FROM products WHERE type LIKE '%" + filter1 + "%' ORDER BY " + order + ";")
                    # print the results in a table
                    for row in cur.fetchall():
                        x.add_row([row["code"], row["name"], row["type"], row["brand"], row["cost"], row["sales"], row["profit"], row["launch_date"], row["weekly_production"]])
                    print(x)
                else:
                    if(filter2 == "oppo" or filter2 == "vivo" or filter2 == "oneplus"):
                        cur.execute("SELECT * FROM products WHERE type LIKE '%" + filter1 + "%' AND brand = '" + filter2 + "' ORDER BY " + order + ";")
                        # print the results in a table
                        for row in cur.fetchall():
                            x.add_row([row["code"], row["name"], row["type"], row["brand"], row["cost"], row["sales"], row["profit"], row["launch_date"], row["weekly_production"]])
                        print(x)
                    # else if there's partial text match for filter2
                    else:
                        cur.execute("SELECT * FROM products WHERE type LIKE '%" + filter1 + "%' AND brand LIKE '%" + filter2 + "%' ORDER BY " + order + ";")
                        # print the results in a table
                        for row in cur.fetchall():
                            x.add_row([row["code"], row["name"], row["type"], row["brand"], row["cost"], row["sales"], row["profit"], row["launch_date"], row["weekly_production"]])
                        print(x)
        elif(column_name == "employees"):
            # ask user if they want to sort by experience, salary, no_of_leaves_used or hours_spent_a_month
            order = input("Order by: (experience/salary/no_of_leaves_used/hours_spent_a_month) ")
            x = PrettyTable()
            x.field_names = ["ID", "Name", "Experience", "Salary", "Leaves used", "Hours/month"]
            if (order == "experience" or order == "salary" or order == "no_of_leaves_used" or order == "hours_spent_a_month"):
                cur.execute("SELECT * FROM employees ORDER BY " + order)
                # print the results in a table
                for row in cur.fetchall():
                    x.add_row([row["id"], row["name"], row["experience"], row["salary"], row["no_of_leaves_used"], row["hours_spent_a_month"]])
                print(x)
                # print the total and average salary, no_of_leaves_used and hours_spent_a_month
                cur.execute("SELECT SUM(salary), AVG(salary), SUM(no_of_leaves_used), AVG(no_of_leaves_used), SUM(hours_spent_a_month), AVG(hours_spent_a_month) FROM employees;")
                # y = PrettyTable()
                # y.field_names = ["Total salary", "Avg salary", "Total leaves", "Avg leaves", "Total hours/month", "Avg hours/month"]
                # for row in cur.fetchall():
                #     y.add_row([row["SUM(salary)"], row["AVG(salary)"], row["SUM(no_of_leaves_used)"], row["AVG(no_of_leaves_used)"], row["SUM(hours_spent_a_month)"], row["AVG(hours_spent_a_month)"]])
                # print(y)
                for row in cur.fetchall():
                    print("Total salary: " + str(row["SUM(salary)"]))
                    print("Avg salary: " + str(row["AVG(salary)"]))
                    print("Total leaves: " + str(row["SUM(no_of_leaves_used)"]))
                    print("Avg leaves: " + str(row["AVG(no_of_leaves_used)"]))
                    print("Total hours/month: " + str(row["SUM(hours_spent_a_month)"]))
                    print("Avg hours/month: " + str(row["AVG(hours_spent_a_month)"]))                    
            # else incorrect input
            else:
                print("Invalid Argument")
        elif(column_name == "finances"):
            x = PrettyTable()
            x.field_names = ["Brand", "YoY growth", "QoQ growth", "Stock price"]
            # ask user if they want to sort by stock_price, yoy_growth or qoq_growth
            order = input("Order by: (stock_price/yoy_growth/qoq_growth) ")
            if (order == "stock_price" or order == "yoy_growth" or order == "qoq_growth"):
                cur.execute("SELECT * FROM stock_of ORDER BY " + order + ";")
                # print the results in a table
                for row in cur.fetchall():
                    x.add_row([row["brand"], row["yoy_growth"], row["qoq_growth"], row["stock_price"]])
                print(x)
            # else incorrect input
            else:
                print("Invalid Argument")
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

def Researcher():
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

    while(1):
        user_query = input("Enter query: ").split()
        if(len(user_query) > 0):
            if(user_query[0] == "exit"):
                return
            elif(user_query[0] == "show"):
                if(len(user_query) > 1):
                    if(user_query[1] == "products"):
                        show("products", con)
                    elif(user_query[1] == "employees"):
                        show("employees", con)
                    elif(user_query[1] == "finances"):
                        show("finances", con)
                    else:
                        print("Invalid Arguments")
                else:
                    print("Insufficient Arguments")
            else:
                print("Invalid Argument")

    Researcher(1)