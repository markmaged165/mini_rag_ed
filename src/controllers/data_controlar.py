from .base_controlar import basecontrolar
from fastapi import UploadFile
class datacontrolar (basecontrolar):
    def __init__(self):
        super().__init__()
        self.size_scale=1038576
    def validate_uploaded_file(self,file:UploadFile):
        if file.content_type not in self.app_settings.file_allowed_types:
            return False
        if file.size> self.app_settings.file_max_size:
            return False
        return True
