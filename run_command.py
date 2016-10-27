import os
import config

def run_command(request):
    #TODO Implement request validation
    print(request.data)
    file = request.json['file']
    # Run command on RPi
    # Test command
    # TODO Fix file paths
    os.chdir(config.DEMO_FILE_PATH)

    file = config.DEMO_FILE_PATH + file
    command = 'sudo ./demo -t 10 -D 1 %s' % file
    print(command)
    if os.path.exists(file):
        os.system(command)
        print('Command run')
    else:
        print('File not found')
