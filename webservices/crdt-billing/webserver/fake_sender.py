import json
import requests


class Sender(object):
    def __init__(self, destination_list):
        self.destination_list = destination_list

    def broadcast(self, data):
        for dest in self.destination_list:
            print(requests.post(dest, data).text)


def formatUpdate(timestamp, bts_id, imsi, user_id, amount):
    transport_collection = {"timestamp": timestamp, "bts_id": bts_id, "imsi": imsi, "user_id": user_id, "amount": amount}
    return json.dumps(transport_collection)


if __name__ == "__main__":
    update = formatUpdate(100, "betty", "jen", "francis", -44)
    sender = Sender(["http://localhost:5000/fake_crdt/"])

    sender.broadcast(update)
