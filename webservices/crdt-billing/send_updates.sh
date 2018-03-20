#!/bin/bash

# this script should run as a cron job when the db has updates to send.
python $COLTE_DIR/webservices/crdt-billing/send_updates.py
