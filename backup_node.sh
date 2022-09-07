#!/bin/bash
######################################################    
# Script to switch on backup node at a moments notice
# I don't want to lose uptime, so I am not actually 
# going to run this right now. 

# first, update the software 

cd /home/$USER/nearcore
git fetch
commit=`curl https://raw.githubusercontent.com/near/stakewars-iii/main/commit.md` 
echo "Commit is $commit, building ... "
git checkout $commit
cargo build -p neard --release --features shardnet

# Replace keys
cp ~/.near/altkeys/validator_key.json ~/.near
cp ~/.near/altkeys/node_key.json ~/.near

# Restart
sudo service neard restart

