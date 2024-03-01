import psycopg2 as sql

db = sql.connect(
    database='autosalon',
    host='localhost',
    user='postgres',
    password='18181609'
)

cursor = db.cursor()

# ------------------------------------------------------------------------------------------------

# cursor.execute('''
#     SELECT model_name, model_price, brand_name, color_name, models.car_count FROM models
#     JOIN colors USING(color_id)
#     JOIN brands USING(brand_id);
# ''')
#
# models = cursor.fetchall()
#
# print("+", "-".center(30, '-'), "+", "".center(11, '-'),
#       "+", "".center(15, '-'), "+", "".center(10, '-'),
#       "+", "".center(9, '-'), "+")
#
# print("|", "model_name".center(30, ' '), "|", "model_price".center(9, ' '),
#       "|", "brand_name".center(15, ' '), "|", "color_name".center(10, ' '),
#       "|", "car_count".center(7, ' '), "|")
#
# print("+", "".center(30, '-'), "+", "".center(11, '-'),
#       "+", "".center(15, '-'), "+", "".center(10, '-'),
#       "+", "".center(9, '-'), "+")
#
# for model in models:
#     model_name, model_price, brand_name, color_name, car_count = model
#     print("|", model_name.center(30, ' '), "|", str(model_price).center(11, ' '),
#           "|", brand_name.center(15, ' '), "|", color_name.center(10, ' '), "|", str(car_count).center(9, ' '), "|")
#
# print("+", "-".center(30, '-'), "+", "".center(11, '-'),
#       "+", "".center(15, '-'), "+", "".center(10, '-'),
#       "+", "".center(9, '-'), "+")

# ------------------------------------------------------------------------------------------------

# cursor.execute('''
#     SELECT customer_id ,email FROM customers
#     UNION
#     SELECT employee_id, email FROM employees;
# ''')
#
# emails = cursor.fetchall()
# print("+", "--".center(6, '-'), "+", "------".center(30, '-'), "+")
# print("|", "ID".center(6, ' '), "|", "EMAILS".center(30, ' '), "|")
# print("+", "--".center(6, '-'), "+", "------".center(30, '-'), "+")
# for email in emails:
#     h_id, uemail = email
#     print("|", str(h_id).center(6, ' '), "|", uemail.center(30, ' '), "|")
#
# print("+", "--".center(6, '-'), "+", "------".center(30, '-'), "+")

# ------------------------------------------------------------------------------------------------

# cursor.execute('''
#     SELECT country, count(customers.*) FROM customers GROUP BY country ORDER BY count(customers.*) DESC;
# ''')
#
# customers = cursor.fetchall()
# print("+", "-------".center(15, '-'), "+", "---------------".center(15, '-'), "+")
# print("|", "Country".center(15, ' '), "|", "Customers count".center(15, ' '), "|")
# print("+", "-------".center(15, '-'), "+", "---------------".center(15, '-'), "+")
# for customer in customers:
#     country, cust_count = customer
#     print("|", country.center(15, ' '), "|", str(cust_count).center(15, ' '), "|")
#
# print("+", "-------".center(15, '-'), "+", "---------------".center(15, '-'), "+")

# ------------------------------------------------------------------------------------------------

# cursor.execute('''
#     SELECT country, count(employees.*) FROM employees GROUP BY country ORDER BY count(employees.*) DESC;
# ''')
#
# employees = cursor.fetchall()
# print("+", "-------".center(15, '-'), "+", "---------------".center(16, '-'), "+")
# print("|", "Country".center(15, ' '), "|", "Employees count".center(16, ' '), "|")
# print("+", "-------".center(15, '-'), "+", "---------------".center(16, '-'), "+")
# for employee in employees:
#     country, emp_count = employee
#     print("|", country.center(15, ' '), "|", str(emp_count).center(16, ' '), "|")
#
# print("+", "-------".center(15, '-'), "+", "---------------".center(16, '-'), "+")

# ------------------------------------------------------------------------------------------------

# cursor.execute('''
#     SELECT brand_name, count(models.*) FROM brands JOIN models USING(brand_id) GROUP BY brand_name;
# ''')
#
# brands = cursor.fetchall()
# print("+", "-----".center(15, "-"), "+", "-----------".center(12, '-'), "+")
# print("|", "Brand".center(15, " "), "|", "Model count".center(12, ' '), "|")
# print("+", "-----".center(15, "-"), "+", "-----------".center(12, '-'), "+")
# for brand in brands:
#     brand, model_count = brand
#     print("|", brand.center(15, " "), "|", str(model_count).center(12, ' '), "|")
# print("+", "-----".center(15, "-"), "+", "-----------".center(12, '-'), "+")

# ------------------------------------------------------------------------------------------------

# cursor.execute('''
#     SELECT brand_name, count(models.*) FROM brands JOIN models USING(brand_id) GROUP BY brand_name HAVING count(models.*) > 5 ;
# ''')
#
# brands = cursor.fetchall()
# print("+", "-----".center(15, "-"), "+", "-----------".center(12, '-'), "+")
# print("|", "Brand".center(15, " "), "|", "Model count".center(12, ' '), "|")
# print("+", "-----".center(15, "-"), "+", "-----------".center(12, '-'), "+")
# for brand in brands:
#     brand, model_count = brand
#     print("|", brand.center(15, " "), "|", str(model_count).center(12, ' '), "|")
# print("+", "-----".center(15, "-"), "+", "-----------".center(12, '-'), "+")

# ------------------------------------------------------------------------------------------------

# cursor.execute('''
#     SELECT customers.first_name ||' '|| customers.last_name AS customer,
#            employees.first_name ||' '|| employees.last_name AS employee,
#            models.model_name, orders.car_count, order_date FROM orders
#            JOIN customers USING(customer_id)
#            JOIN employees USING(employee_id)
#            JOIN models USING(model_id);
# ''')
#
# orders = cursor.fetchall()
# print("+", "-".center(22, '-'), "+", "-".center(22, '-'),
#       "+", "-".center(28, '-'), "+", "-".center(9, '-'),
#       "+", "-".center(10, '-'), "+")
#
# print("|", "Customer".center(22, ' '), "|", "Employee".center(22, ' '),
#       "|", "Model name".center(28, ' '), "|", "Car count".center(9, ' '),
#       "|", "Order date".center(10, ' '), "|")
#
# print("+", "-".center(22, '-'), "+", "-".center(22, '-'),
#       "+", "-".center(28, '-'), "+", "-".center(9, '-'),
#       "+", "-".center(10, '-'), "+")
#
# for order in orders:
#     customer, employee, model_name, car_count, order_date = order
#     print("|", customer.center(22, ' '), "|", employee.center(22, ' '), "|", model_name.center(28, ' '),
#           "|", str(car_count).center(9, ' '), "|", str(order_date).center(10, ' '), "|")
#
# print("+", "-".center(22, '-'), "+", "-".center(22, '-'),
#       "+", "-".center(28, '-'), "+", "-".center(9, '-'),
#       "+", "-".center(10, '-'), "+")

# ------------------------------------------------------------------------------------------------

# cursor.execute('''
#     SELECT sum(model_price) FROM models;
# ''')
#
# models = cursor.fetchall()
# print("Models jadvalidagi modellarning umumiy narxi:", models[0][0])

# ------------------------------------------------------------------------------------------------

# cursor.execute('''
#     SELECT count(brands.*) FROM brands;
# ''')
# brands = cursor.fetchall()
# print("Autosalondagi jami brandlar soni:", brands[0][0], "ta.")

db.commit()
db.close()
