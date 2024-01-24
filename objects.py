"""

Object files for project - should include
# - SoundLoader (file dialog and pull up wav/mp3)
- Beat (single beat)
- Loop (consists of beat, time signature ...)
- Track (runs on timer and consists of all loops simultaneously playing)

"""

import wave  # for meta-information about the file
import time  # sleeps
from playsound import playsound  # to actually play the file
from threading import Thread, Event


class Base:
    '''
    base class implements run '''

    def __init__(self) -> None:
        pass


class Player():
    def __init__(self, file, bpm=100) -> None:
        self.thread = None
        self.file = file
        self.flag = Event()
        self.interval = 60/bpm

    def run(self) -> None:
        self.thread = Thread(target=self._run, args=(), daemon=True)
        self.thread.start()

    def stop(self) -> None:
        self.flag.set()
        self.thread.join(timeout=5)  # arbitrary timeout

    def _run(self) -> None:
        while not self.flag.is_set():
            playsound(self.file)
            # TODO: need to spawn a thread for each beat?
            time.sleep(self.interval)
        print('_run is stopping')


if __name__ == '__main__':
    file = '/Users/ghosh/Downloads/Korg-NS5R-Xylophone-C3.wav'
    player = Player(file, 500)
    player.run()
    print('starting playback')
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print('[ctrl+c] stopping...')
        player.stop()
    # playsound(file)
    # meta = wave.open(file, 'r')
