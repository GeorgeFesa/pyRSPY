from pathlib import Path

"""Class for setting the default path for the logs,
   depending on the operating system"""


class Logs:

    __path = Path('Data')

    def get_path(self):
        return self.__path

    def set_path(self, new_path):
        self.__path = Path(new_path)


custom_path = Logs()
