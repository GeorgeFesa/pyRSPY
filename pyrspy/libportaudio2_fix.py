import sys
import time
import subprocess


def check_for_libportaudio2():
    if sys.platform == 'linux':
        try:
            output = subprocess.run(['apt', 'list', '--installed',
                                     'libportaudio2'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.DEVNULL)
            output = output.stdout.decode('utf-8')
            if 'libportaudio2' not in output:
                print('\nLibrary "libportaudio2" is missing,\nInstalling...\n')
                time.sleep(2)
                subprocess.run(['sudo', 'apt', 'install', 'libportaudio2'])
        except OSError:
            print('Could not install libportaudio2.')
        except KeyboardInterrupt:
            sys.exit()


check_for_libportaudio2()
