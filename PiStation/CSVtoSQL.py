import os
import csv
import sys
import MySQLdb
import glob

# DB variables
db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="tree1234", db="raindb")
cur = db.cursor()

csv_data = csv.reader(file('logger.csv'))
for row in csv_data:
	cur.execute("REPLACE INTO station_1(timestamp, count) VALUES(%s, %s)", row)

db.commit()
db.close()