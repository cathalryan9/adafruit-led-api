import os
import config
import sqlite3
import time

def run_command_ppm(request):
    #TODO Implement request validation
    # Run command on RPi
    # Test command
    # TODO Fix file paths
    os.chdir(config.DEMO_FILE_PATH)
    file = request.json['file']
    play_duration = request.json['duration']
    file_path = config.DEMO_FILE_PATH + file
    command = 'sudo ./demo -t %d %s %s -D 1 %s' % (play_duration, config.LARGE_DISPLAY_PARAMETER, config.GPIO_MAPPING, file_path)
    print(command)

    try:
        db_change_state()
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
        db_change_state()
        os.system(command)
        print('Command run')

    else:
        print('File not found')

def run_command_clock(request):
    #TODO Implement request validation
    # Run command on RPi
    # Test command
    # TODO Fix file paths
    os.chdir(config.DEMO_FILE_PATH)
    #file = request.json['file']
    play_duration = request.json['duration']

    command = 'sudo ./demo  %s %s -D 12 -R180' % ( config.LARGE_DISPLAY_PARAMETER, config.GPIO_MAPPING)
    print(command)
    db_change_state()
    os.system(command)

    print('Clock run')

def run_command_countdown(request):
    #TODO Implement countdown timer for New Years
    print('countdown')

def db_change_state():
    conn = sqlite3.connect(config.DATABASE_NAME)
    with conn:
        conn.execute('UPDATE STATE SET value="stopping" WHERE name="led_panel_state");')
        t = 'led_panel_state'
        conn.execute('SELECT value FROM STATE WHERE name=?', t)
        print conn.fetchone()
        led_panel_state = conn.fetchone()
        while led_panel_state is not 'stopped':
            #sleep(1)
            print("sleeping")
            time.sleep(1)