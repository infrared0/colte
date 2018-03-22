import MySQLdb
import sys

def query_db(imsi):

    ########## Set up DB connection:
    #db = MySQLdb.connect(host="localhost",
    #                    user="vagrant",
    #                    passwd="correcthorsebatterystaple",
    #		        db="crdt_db")
    
    db = MySQLdb.connect(host="localhost",
                        user="root",
                        passwd="correcthorsebatterystaple",
    		        db="crdt_db")
    
    #db = MySQLdb.connect(host="localhost",
    #                    user="colte",
    #                    passwd="correcthorsebatterystaple",
    #		    db="crdt_db")

    cursor = db.cursor()
    
    ########### Perform DB Query:

    query_str = "SELECT sum(amount) from `" + imsi + "`"
    try:
        cursor.execute(query_str)
        result = cursor.fetchone()
        balance = float(result[0])
        #print "Balance for user with IMSI '" + imsi + "' is {}.".format(balance)
    except MySQLdb.Error, e:
        #print e
        print "Error: User not found."
        balance = 0


    ########## Close out everything
    
    db.commit()
    cursor.close()
    db.close()

    return balance

############ Main for testing

if __name__ == "__main__":

    imsi = sys.argv[1]
    print query_db(imsi)
