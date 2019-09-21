import subprocess
import sys
import time
from log import custom_path


def check_for_fswebcam():
    if sys.platform == 'linux':
        try:
            subprocess.run(
                ['sudo', 'apt', 'install', 'fswebcam'])
            print('Completed successfully!')
        except OSError:
            print('Could not install fswebcam.')
        except KeyboardInterrupt:
            sys.exit()
    else:
        print('This functionality has not been'
              'implemented yet in your current OS.')


def cap_webcam_footage(times=1, secs=0):
    for i in range(times):
        try:
            subprocess.run(['fswebcam',
                            custom_path.get_path() /
                            '%Y-%m-%d %X.png'])
        except OSError:
            pass
    time.sleep(secs)
