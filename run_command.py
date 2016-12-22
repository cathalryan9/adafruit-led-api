import os
import config

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
    if os.path.exists(file_path):
        os.system(command)
        print('Command run')

    else:
        print('File not found')


def run_command_gif(request):
    print('run gif')
    os.chdir(config.LED_IMAGE_VIEWER)
    file = request.json['file']
    play_duration = request.json['duration']
    file_path = config.UPLOAD_FOLDER + file
    print(play_duration)
    print('%d %s %s %s' % (play_duration, config.LARGE_DISPLAY_PARAMETER, config.GPIO_MAPPING, file_path))
    command = 'sudo ./led-image-viewer -t%d %s %s %s' % (play_duration, config.LARGE_DISPLAY_PARAMETER, config.GPIO_MAPPING, file_path)
    print(command)
    if os.path.exists(file_path):
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
    command = 'sudo ./demo -t %d %s %s -D 12' % (play_duration, config.LARGE_DISPLAY_PARAMETER, config.GPIO_MAPPING)
    print(command)
    print('Clock run')