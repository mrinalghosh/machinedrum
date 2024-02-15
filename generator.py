import wave
import struct
from math import *

SAMPLE_RATE = 44100  # .wav sample rate in hz
A_FREQUENCY = 440  # hz - pitch standard

''' Named note utilities '''

notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
equivalent_notes = {'Bb': 'A#',
                    'Db': 'C#',
                    'Eb': 'D#',
                    'Gb': 'F#',
                    'Ab': 'G#'}


def note_to_frequency(note, octave=0):
    try:
        note_idx = notes.index(note)
    except ValueError:
        if note in equivalent_notes.keys():
            note_idx = notes.index(equivalent_notes[note])
        else:
            raise ValueError(f'`{note}` is not a valid note')

    return A_FREQUENCY * pow(2, (12*octave+note_idx)/12)


class Soundwave:
    def __init__(self) -> None:
        pass


class Sine(Soundwave):
    def __init__(self, frequency, duration=1, filename='sound.wav') -> None:
        self.frequency = frequency  # hz
        self.duration = duration  # s
        self.filename = filename

        self._writefile()

    def _writefile(self):
        with wave.open(self.filename, 'w') as wf:
            # boilerplate
            wf.setnchannels(1)  # mono
            wf.setsampwidth(2)
            wf.setframerate(SAMPLE_RATE)

            # write wav
            for i in range(int(self.duration * SAMPLE_RATE)):
                value = int(32767.0 * cos(self.frequency *
                            pi * float(i)/float(SAMPLE_RATE)))
                data = struct.pack('<h', value)
                wf.writeframesraw(data)

            wf.writeframes(b'')

        print(f'Wrote to {self.filename}')


# if __name__ == '__main__':
    # # idea - use a named pipe to keep modifying the sound frequency
    # #   - depends on the wav file being read new each time instead of cached
    # #   - arrow keys (L/R pitch - U/D volume)

    # # idea - other signals
    # #   - square wave, sawtooth, triangle
