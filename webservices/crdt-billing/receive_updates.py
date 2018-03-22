import MySQLdb
#import sys

######### Get environment variables and args:


########## Set up DB connection:


def update_db(update):
    (timestamp, amount, imsi, sender_id, bts_id, sent) = update

    db = MySQLdb.connect(host="localhost",
                        user="vagrant",
                        passwd="correcthorsebatterystaple",
    		        db="crdt_db")
    
    #db = MySQLdb.connect(host="localhost",
    #                    user="root",
    #                    passwd="correcthorsebatterystaple",
    #		        db="crdt_db")

    #db = MySQLdb.connect(host="localhost",
    #                    user="colte",
    #                    passwd="correcthorsebatterystaple",
    #		    db="crdt_db")

    cursor = db.cursor()
    cursor._defer_warnings = True 
    ########### Perform DB Updates:

    create_table_str = "CREATE TABLE IF NOT EXISTS `" + imsi + "`( \
    `timestamp` int(12) unsigned DEFAULT '0' NOT NULL, \
    `amount` int(11) DEFAULT '0' NOT NULL, \
    `user_imsi` varchar(16) NOT NULL, \
    `sender_id` varchar(16) NOT NULL, \
    `bts_id` varchar(16) NOT NULL, \
    `sent` bit(1) DEFAULT 0 NOT NULL, \
    PRIMARY KEY (`timestamp`, `amount`) \
    ) ENGINE=MyISAM DEFAULT CHARSET=latin1;"
    cursor.execute(create_table_str)
    
    insert_str = "INSERT INTO `" + imsi + "` VALUES ({}, {}, {}, '{}', {}, {})".format(timestamp, amount, imsi, sender_id, bts_id, sent)
    try:
        cursor.execute(insert_str)
    except MySQLdb.Error, e:
        #print e
        pass

    ########## Close out everything
    
    db.commit()
    cursor.close()
    db.close()


############ Main for testing

if __name__ == "__main__":
    #DEBUG get the info from Matt's receiver
    dummy_update_list = [("1", "10", "123451234512345", "infrared", "1", "1"), ("10", "-10", "123451234512345", "infrared", "1", "0"),("5", "200", "123331234512345", "spencer", "1", "0")]
    for up in dummy_update_list:
        update_db(up)
