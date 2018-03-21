import json

from flask import Flask
from flask import request
app = Flask(__name__)


# Need to get a callback function passed in, or use this to call esther's code.
def fakeCallback(timestamp, bts_id, imsi, user_id, amount):
    print("Got a request with", timestamp, bts_id, imsi, user_id, amount)


@app.route("/fake_crdt/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        try:
            crdt_data = json.loads(request.data.decode("utf8"))
            fakeCallback(crdt_data["timestamp"], crdt_data["bts_id"], crdt_data["imsi"], crdt_data["user_id"],
                         crdt_data["amount"])
        except TypeError as e:
            print("Failed to decode json string")
            raise e
    else:
        print("got a get")

    return "ok"
