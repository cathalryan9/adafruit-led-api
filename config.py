import os
# TODO: Change to __name__?
abspath = os.path.abspath('run_command.py')
DIRPATH = os.path.dirname(abspath)


DATABASE_NAME = 'rave.db'

UPLOAD_FOLDER = DIRPATH + '/uploads/'

DEMO_FILE_PATH = DIRPATH + '/rpi-rgb-led-matrix/examples-api-use/'

LED_IMAGE_VIEWER = DIRPATH + '/rpi-rgb-led-matrix/utils/'

GPIO_MAPPING = '--led-gpio-mapping=adafruit-hat'
LARGE_DISPLAY_PARAMETER = '-L'
HOST_IP_ADDRESS = '127.0.0.1'
HOST_PORT = '5000'
