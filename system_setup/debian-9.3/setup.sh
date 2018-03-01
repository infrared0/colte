#!/bin/bash

SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
COLTE_DIR="$SCRIPTDIR/../.."

# Step 1: Install prereqs (ansible and python)
sudo cp $COLTE_DIR/system_setup/debian-9.3/sources/ansible_sources.list /etc/apt/sources.list
sudo apt-get update
sudo apt-get install -y --allow-unauthenticated ansible python2.7

#sudo add-apt-repository -y ppa:ansible/ansible-2.4
#sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
#sudo apt-get update

# Step 2: Run Ansible script to do all the rest of the setup
sudo cp $COLTE_DIR/system_setup/debian-9.3/sources/sources.list /etc/apt/sources.list
sudo apt-get update

sudo apt-get -y install vim
ansible-playbook -v -i "localhost," -c local $COLTE_DIR/system_setup/debian-9.3/main_playbook.yml 

# Step 3: Any final-final configs?!? Setting IP addresses in config files, etc?!?

# Note 1: Internet interface:
# We want the Internet gateway to be XXXX
# And we want it on interface XXXX

# Note 2: Local network interface:
# We want the eNB to be on 10.0.101.2
# The EPC will be 10.0.101.3

