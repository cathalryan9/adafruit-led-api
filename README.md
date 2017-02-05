# adafruit-led-api
Web API for LED panels powered by Raspberry Pi and Adafruit hat.

The following commands need to be run after repo is cloned (and submodule pulled)

###Run the setup.py script:
* python setup.py

###Install dependecies
* sudo apt-get install python-virtualenv
* virtualenv flask
* . flask/bin/activate
* sudo pip install Flask
* sudo pip install Pillow
* sudo npm install -g bower

###In the python dir of rpi-rgb-led-api:
* sudo apt-get update && sudo apt-get install python2.7-dev python-pillow -y
* make build-python
* sudo make install-python

###And in the examples-api-use dir:
* make

###And in utils:
* sudo apt-get install libgraphicsmagick++-dev libwebp-dev -y
* make led-image-viewer
