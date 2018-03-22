import balance
import sys
import time
import receive_updates

timestamp = str(int(time.time()))
amount = str(sys.argv[1])
imsi = str(sys.argv[2])
sender_id = "\"" + str(sys.argv[3]) + "\""
bts_id = str(sys.argv[4])
sent = str(0)

transaction = (timestamp, amount, imsi, sender_id, bts_id, sent)

if int(amount) < 0:
    bal = balance.query_db(imsi)
    if (-1)*amount > bal:
        print "Insufficient funds. Please add credit!"
        print bal
    else:
        receive_updates.update_db(transaction)
else:
    receive_updates.update_db(transaction)

print balance.query_db(imsi)
