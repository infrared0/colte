import MySQLdb

import sys
sys.path.insert(0, '/home/vagrant/epc-fork-colte/webservices/crdt-billing/webserver')
import sender
import os

######### Get environment variables and args:

neighbors_file = '/home/vagrant/epc-fork-colte/webservices/crdt-billing/neighbor_epc.json'
#neighbors_file = '/home/vagrant/epc-fork-colte/webservices/crdt-billing/test/test_neighbor.json'

########## Set up DB connection:

db = MySQLdb.connect(host="localhost",
                    user="vagrant",
                    passwd="correcthorsebatterystaple",
		    db="crdt_db")

#db = MySQLdb.connect(host="localhost",
#                    user="root",
#                    passwd="correcthorsebatterystaple",
#		    db="crdt_db")

#db = MySQLdb.connect(host="localhost",
#                    user="colte",
#                    passwd="correcthorsebatterystaple",
#		    db="crdt_db")

cursor = db.cursor()

########### init Sender:

s = sender.Sender(neighbors_file)

########### Query DB for updates:

query_tables = ("show tables") 
cursor.execute(query_tables) 
result = cursor.fetchall()
customers = [tup[0] for tup in result] # weird formatting

for imsi in customers:
    query_new = ("SELECT * FROM `" + imsi + "` WHERE sent = 0")
    cursor.execute(query_new) 
    new_entries = cursor.fetchall()

    for entry in new_entries:
        timestamp = entry[0]
        amount = entry[1]
        user_imsi = entry[2]
        sender_id = entry[3]
        bts_id = entry[4]
        sent = entry[5]
        to_send = sender.formatUpdate(timestamp, amount, user_imsi, sender_id, bts_id, sent) 
        s.broadcast(to_send)

    update_sent = ("UPDATE `" + imsi + "` SET sent = 1 WHERE sent = 0")
    cursor.execute(update_sent)
    

########## Close out everything

db.commit()
cursor.close()
db.close()
