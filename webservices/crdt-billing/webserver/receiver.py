import json
import sys
sys.path.insert(0, '../')
import receive_updates as receive

from flask import Flask
from flask import request
app = Flask(__name__)


# Need to get a callback function passed in, or use this to call esther's code.
def callback(update):
    receive.update_db(update)

@app.route("/crdt/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        try:
            crdt_data = json.loads(request.data.decode("utf8"))
            callback((crdt_data["timestamp"], crdt_data["amount"], crdt_data["imsi"], crdt_data["sender_id"],
                         crdt_data["bts_id"], "1")) # always set "sent" to 1 when receiving from another bts
            print("Got a request with", crdt_data["timestamp"], crdt_data["amount"], crdt_data["imsi"], crdt_data["sender_id"],
                         crdt_data["bts_id"], "1")
        except TypeError as e:
            print("Failed to decode json string")
            raise e
    else:
        print("got a get")

    return "Received DB Update"

app.run(host="0.0.0.0", port=int("5000"), debug=True)
