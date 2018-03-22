import json
import requests


class Sender(object):
    def __init__(self, destination_filename):
        with open(destination_filename, 'r+') as neighbor_file:
            destination_list = json.load(neighbor_file) 
        self.destination_list = destination_list
        print "Destinations", destination_list

    def broadcast(self, data):
        for dest in self.destination_list:
            print requests.post(dest, data).text


def formatUpdate(timestamp, bts_id, imsi, sender_id, amount, sent):
    transport_collection = {"timestamp": timestamp, "bts_id": bts_id, "imsi": imsi, "sender_id": sender_id, "amount": amount, "sent": sent}
    return json.dumps(transport_collection)


#if __name__ == "__main__":

    # import the list of updates

#    update = formatUpdate(100, "betty", "jen", "francis", -44)
#    sender = Sender(["http://localhost:5000/fake_crdt/"])
#
#    sender.broadcast(update)