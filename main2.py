from pynput import keyboard

def on_press(key):
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    # if k in ['1', '2', 'ctrl', 'cmd']:  # keys of interest
    print('Key pressed: ' + k)
    return False  # stop listener; remove this if want more keys


def on_release(key):
    try:
        k = key.char
    except:
        k = key.name
    print('Key released: ' + k)
    return False

while True:
    listener = keyboard.Listener(on_press=on_press)
    listener = keyboard.Listener(on_release=on_release)
    listener.start()  # start to listen on a separate thread
    listener.join()  # remove if main thread is polling self.keys
