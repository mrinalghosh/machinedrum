from threading import Thread, Event
import curses
import os

# import keyboard # !!! needs root access

# create audio thread, control thread (main)

# https://stackoverflow.com/questions/24072790/how-to-detect-key-presses


def main(win):
    win.nodelay(True)
    key = ""
    win.clear()
    win.addstr("Detected key:")
    while True:
        try:
            key = win.getkey()
            win.clear()
            win.addstr("Detected key:")
            win.addstr(str(key))
            if key == os.linesep:  # Enter
                break
        except Exception as e:
            # No input
            pass


if __name__ == '__main__':
    curses.window.getch()
    curses.wrapper(main)
    # while True:
    #     try:
    #         if keyboard.read('')

    #     except KeyboardInterrupt:
    #         break
