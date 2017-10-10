import os
import config
import sqlite3
import time
#import subprocess

def run_command_ppm(request):
    #TODO Implement request validation
    #TODO Fix file paths
    os.chdir(config.DEMO_FILE_PATH)
    file = request.json['file']
    play_duration = request.json['duration']
    file_path = config.DEMO_FILE_PATH + file
    command = 'sudo ./demo -t %d %s %s -D 1 %s' % (play_duration, config.LARGE_DISPLAY_PARAMETER, config.GPIO_MAPPING, file_path)
    print(command)

    try:
        os.system(command)
        print('Command run')
    except:
        if not os.path.exists(file_path):
            print('File not found')

def run_command_gif(request):
    print('run gif')
    os.chdir(config.LED_IMAGE_VIEWER)
    file = request.json['file']
    play_duration = request.json['duration']
    file_path = config.DIRPATH + '/' + file
    print('%d %s %s %s' % (play_duration, config.LARGE_DISPLAY_PARAMETER, config.GPIO_MAPPING, file_path))
    command = 'sudo ./led-image-viewer -t%d %s %s %s' % (play_duration, config.LARGE_DISPLAY_PARAMETER, config.GPIO_MAPPING, file_path)
    print(command)
    if os.path.exists(file_path):
        os.system(command)
        #subprocess.call(command)

        print('Command run')

    else:
        print('File not found')

def run_command_clock(request):
    #TODO Implement request validation
    #TODO Fix file paths
    os.chdir(config.DEMO_FILE_PATH)
    #play_duration = request.json['duration']
    print("About to play the clock")

    command = 'sudo .%sdemo  %s %s -D 12 -R180' % (config.DEMO_FILE_PATH, config.LARGE_DISPLAY_PARAMETER, config.GPIO_MAPPING)
    print(command)
    #subprocess.call(command)
    os.system(command)

    print('Clock run')

def run_command_countdown(request):
    #TODO Implement countdown timer for New Years
    print('countdown')


def db_change_state(changed_value):
    print("Change state to " + changed_value)
    conn = sqlite3.connect(config.DATABASE_NAME)

    with conn:
        conn.execute('UPDATE STATE SET value="' + changed_value + '" WHERE name="led_panel_state";')

