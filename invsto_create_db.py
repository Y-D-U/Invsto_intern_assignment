import mysql.connector
import pandas as pd
import numpy



with open("det.txt") as f:
	paswd=[i.strip() for i in f.readlines()][0]

db=mysql.connector.connect(host="localhost",
	user="root",
	passwd=paswd,
	database="invsto",
	auth_plugin="mysql_native_password")

cur=db.cursor(buffered=True)

data=pd.read_excel(r"C:\Users\HP\Downloads\HINDALCO_1D.xlsx")

cur.execute("CREATE TABLE HINDALCO(Date datetime,close FLOAT,high FLOAT ,low FLOAT,open FLOAT,volume INT, instrument varchar(20));")

for i,rows in data.iterrows():
	cur.execute("INSERT INTO HINDALCO(Date,close,high,low,open,volume,instrument) VALUES ({date},{close},{high},{low},{open},{vol},{instrum})".format(date="\'"+str(rows[0])+"\'",close=rows[1],high=rows[2],low=rows[3],open=rows[4],vol=rows[5],instrum="\'"+rows[6]+"\'"))
	db.commit()

	
print("finished updating the database..")

