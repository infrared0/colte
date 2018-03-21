import MySQLdb
import sys

######### Get environment variables and args:

print os.environ.get('COLTE_USER')
imsi = sys.argv[1]   # this should be the imsi

########## Set up DB connection:

db = MySQLdb.connect(host="localhost",
                    user="colte",
                    passwd="correcthorsebatterystaple",
		    db="crdt_db")

cursor = db.cursor()

# TODO get the info from Matt's receiver
dummy_update_list = [(1, 10, 'IMSI121234512345', 'infrared', 1, 1), (5, 200, 'IMSI121234512345', 'spencer', 1, 0)]


########### Perform DB Updates:

#for update in dummy_update_list:
#    query = ("SELECT * FROM customers WHERE ip = '" + str(ip_addr) + "'")
#    numrows = cursor.execute(query)

#commit_str = "UPDATE crdt_db SET timestamp = %s, amount = %s, user_imsi = %s, user_id = %s, bts_id = %s FROM `IMSITEST`"
commit_str = "INSERT INTO `" + imsi + "` VALUES (%i, %i, %s, %s, %s, %i, %i)"
cursor.executemany(commit_str, dummy_update_list)

# Try catch version
#try:
#    cursor.executemany(commit_str, dummy_update_list)
#except MySQLdb.Error, e:
#    print e[0], e[1]
#    db.rollback()


########## Close out everything

db.commit()
cursor.close()
db.close()
