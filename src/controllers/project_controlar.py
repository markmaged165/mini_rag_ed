from .base_controlar import basecontrolar
from fastapi import UploadFile
from model import responsesignal
import os
class projectcontrolar(basecontrolar):
    def __init__(self):
        super().__init__()
    def get_project_path(self,project_id:str):
        project_dir= self.file_dir= os.path.join(
            self.file_dir,
            project_id
        )
        if not os.path.exists(project_dir):
            os.makedirs(project_dir)
        
        return project_dir