#!/usr/bin/python3

import mysql.connector


connection = mysql.connector.connect(host='localhost',
					database='foo',
					user='root',
					password='my-secret-pw')

sql_select_Query = "select * from Laptop"
cursor = connection.cursor()
cursor.execute(sql_select_Query)

records = cursor.fetchall()
print("Total number of rows in table : ",cursor.rowcount)
print("\nPrinting each row :")
for row in records:
	print("value = ",row[0])

