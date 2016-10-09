#!/usr/bin/env bash

ln -s /vagrant work

# python
sudo apt-get update
sudo apt-get install -y python-pip python-dev build-essential 
sudo pip install pydub
sudo apt-get install -y aubio-tools libaubio-dev libaubio-doc
sudo pip install telepot
sudo pip install feedparser
#sudo pip install requests
#sudo pip install complexjson
sudo pip install beautifulsoup4
sudo apt-get install -y libav-tools
sudo apt-get install -y git

sudo locale-gen UTF-8
sudo hostname snake
