#!/bin/bash


cd /home/$USER/nearcore
git fetch
#commit=`curl https://raw.githubusercontent.com/near/stakewars-iii/main/commit.md`
commit='24cbb11ce1e14aa267f787f011935a4465d3537d'
echo "Commit is $commit, building ... "
git checkout $commit
cargo build -p neard --release --features shardnet
echo "Finished, restarting ..."
sudo service neard restart
