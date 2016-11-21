import os
import config

def run_command_ppm(file):
    #TODO Implement request validation
    # Run command on RPi
    # Test command
    # TODO Fix file paths
    os.chdir(config.DEMO_FILE_PATH)
    os.system('sudo pkill ')

    file = config.DEMO_FILE_PATH + file
    command = 'sudo ./demo -t 20 %s %s -D 1 %s' % config.LARGE_DISPLAY_PARAMETER, config.GPIO_MAPPING, file
    print(command)
    if os.path.exists(file):
        os.system(command)
        print('Command run')
        os.system('sudo pkill sudo')

    else:
        print('File not found')


def run_command_gif(file):
    print('run gif')
    os.chdir(config.LED_IMAGE_VIEWER)

    file = config.UPLOAD_FOLDER + file
    command = 'sudo ./led-image-viewer -t20 %s %s %s' % config.LARGE_DISPLAY_PARAMETER,config.GPIO_MAPPING, file
    print(command)
    if os.path.exists(file):
        os.system(command)
        print('Command run')
        os.system('sudo pkill sudo')

    else:
        print('File not found')