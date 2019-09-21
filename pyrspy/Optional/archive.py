import shutil
import os
import re
from pathlib import Path


class Archive:

    def __init__(self, source, dest):
        if Path(source).exists():
            self.__base_name = Path(dest) / Path(source).name
            try:
                self.__root_dir = source.split(
                    re.split(r'[\\/]', source)[-1])[0]
            except ValueError:
                self.__root_dir = source.split(
                    re.split(r'[\\/]', source)[-2])[0]
            self.__base_dir = Path(source).name
        self.__format = 'zip' if os.name == 'nt' else 'tar'

    def archive(self):
        shutil.make_archive(self.__base_name, self.__format,
                            self.__root_dir, self.__base_dir)
