from threading import Thread, Event
import curses
import os
import time

from generator import notes, Sine, note_to_frequency

# import keyboard # !!! needs root access

# create audio thread, control thread (main)

# https://stackoverflow.com/questions/24072790/how-to-detect-key-presses

# TODO: last read time so that individual button presses are debounced


# TODO: store files that were created in order to delete them when the player stops
# actually play the generated wav files
# merge files and have background thread playing tones when the key is pressed (can use tempfile)

debounce_delay = 0.08  # seconds


@curses.wrapper
def main(win):
    key = ''
    note_index, note_octave = 0, 0

    win.nodelay(True)  # set true to refresh the key to none when unpressed
    win.clear()
    win.addstr('Detected key:')
    while True:
        try:
            key = win.getkey()
            win.clear()
            win.addstr(
                f'Detected key: {str(key)} {notes[note_index]}{note_octave}')
            if key == os.linesep:  # enter-key
                break

            # change quantized note based on up and down keypresses
            match key:
                case 'KEY_UP':
                    note_index = (note_index + 1) % len(notes)
                case 'KEY_DOWN':
                    note_index = (note_index - 1) % len(notes)
                case 'KEY_LEFT':
                    note_octave -= 1
                case 'KEY_RIGHT':
                    note_octave += 1
                case 'w':  # write note tone to file
                    freq = note_to_frequency(notes[note_index], note_octave)
                    wave = Sine(
                        freq, 0.5, f'\n{notes[note_index]}{note_octave}.wav')
                    win.addstr(f'Wrote {wave.filename}!')
                case _:  # default
                    pass
            curses.flushinp()
        except Exception as e:  # no input
            pass

        # attempt to debounce and clear key for next loop

        # # create note wav file and a thread to play note

        time.sleep(debounce_delay)


# if __name__ == '__main__':
#     window = curses.window
#     window.getch()
#     curses.wrapper(main)
#     # while True:
#     #     try:
#     #         if keyboard.read('')

#     #     except KeyboardInterrupt:
#     #         break
