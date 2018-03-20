import MySQLdb

print os.environ.get('COLTE_USER')

db = MySQLdb.connect(host="localhost",
                    user="colte",
                    passwd="correcthorsebatterystaple",
		    db="crdt")
cursor = db.cursor()

# TODO get the info from Matt's receiver
dummy_update_list = []

#for update in dummy_update_list:
#    query = ("SELECT * FROM customers WHERE ip = '" + str(ip_addr) + "'")
#    numrows = cursor.execute(query)

# (commit all updates at once to save DB operations)
commit_str = "UPDATE crdt SET timestamp = %s, amount = %s, balance = %s WHERE idcustomers = %s"
cursor.executemany(commit_str, record_list)
db.close()
