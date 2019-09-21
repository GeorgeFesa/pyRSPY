import time
from mss import mss
from log import custom_path


def screenshot(times=1, secs=0):
    for i in range(times):
        with mss() as camera:
            # By default mon=0
            # Your build-in camera
            try:
                camera.shot(mon=0, output=str(
                    custom_path.get_path() / '{date:%Y-%m-%d %X}.png'))
            except NotADirectoryError:
                print('Please specify a correct directory!')
        time.sleep(secs)
