from helpers.config import get_settings ,settings
import os
import random
import string

class basecontrolar :
    def __init__(self):
        self.app_settings=get_settings()
        self.base_dir= os.path.dirname(os.path.dirname(__file__))
        self.file_dir= os.path.join(
            self.base_dir,
            'assets/files'
        )
    def generate_random_string(self,length:int=12):
        letters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string