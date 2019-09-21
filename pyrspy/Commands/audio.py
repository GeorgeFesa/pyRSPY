import sounddevice as sd
from log import custom_path
from scipy.io.wavfile import write


class CapAudio:

    __default_path = custom_path.get_path() / 'test'

    def __init__(self, filename=None, secs=4):
        # Audio duration
        self.__secs = secs
        if filename is not None:
            self.__filename = filename
        else:
            self.__filename = self.__default_path
        # Audio samples per second
        self.__sample_rate = 44100
        # Total samples for 4 secs
        self.__samples = secs * self.__sample_rate

    def start(self):
        __recording = sd.rec(
            self.__samples, samplerate=self.__sample_rate, channels=2)
        # Wait's for the recording to finish
        sd.wait()
        # Saving to disk
        write(self.__filename, self.__sample_rate, __recording)
