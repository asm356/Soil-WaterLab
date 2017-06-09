from socket import *
import os, csv, sys, MySQLdb, glob

serverName = ""
serverPort = 80
fo = open("logger3.csv", "a+")

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
modifiedSentence = clientSocket.recv(1024)
fo.write(modifiedSentence);
fo.write("\n");

print 'From Server:', modifiedSentence
while(modifiedSentence != "END"):
	modifiedSentence = clientSocket.recv(1024)
	if(modifiedSentence != "END"):
		fo.write(modifiedSentence);
		fo.write("\n");
	print 'From Server:', modifiedSentence

	fo.close();
clientSocket.close()

db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="tree1234", db="raindb")
cur = db.cursor()

csv_data = csv.reader(file('logger3.csv'))
for row in csv_data:
	cur.execute("REPLACE INTO station_3(timestamp, count) VALUES(%s, %s)", row)

db.commit()
db.close()