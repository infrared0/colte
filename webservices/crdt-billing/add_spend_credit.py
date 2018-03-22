import balance
import sys
import time
import receive_updates

timestamp = int(time.time())
amount = sys.argv[1]
imsi = sys.argv[2]
sender_id = sys.argv[3] 
bts_id = sys.argv[4]
sent = 0

transaction = (str(timestamp), str(amount), str(imsi), "\"" + str(sys.argv[3]) + "\"", str(bts_id), str(sent))

if (int(amount) < 0): 
    bal = balance.query_db(imsi)
    if ((-1)*int(amount) > bal):
        print "Insufficient funds. Please add credit!"
        print "Balance for user with IMSI '" + imsi + "' is {}.".format(bal)
    else:
        receive_updates.update_db(transaction)
        bal = balance.query_db(imsi)
        print "New balance for user with IMSI '" + imsi + "' is {}.".format(bal)
else:
    receive_updates.update_db(transaction)
    bal = balance.query_db(imsi)
    print "New balance for user with IMSI '" + imsi + "' is {}.".format(bal)

