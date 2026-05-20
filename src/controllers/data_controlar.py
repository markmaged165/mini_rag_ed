import os
import re
from .base_controlar import basecontrolar
from fastapi import UploadFile
from model import responsesignal
from .project_controlar import projectcontrolar
class datacontrolar (basecontrolar):
    def __init__(self):
        super().__init__()
        self.size_scale=1038576
    def validate_uploaded_file(self,file:UploadFile):
        if file.content_type not in self.app_settings.file_allowed_types:
            return False , responsesignal.FILE_TYPE_NOTSUPPORTED.value
        if file.size< self.app_settings.file_max_size:
            return False ,responsesignal.FILE_SIZE_NOT_EXCEDED.value
        return True ,responsesignal.FILE_UPLOAD_SUCCESS.value
    

    def genrate_unique_filenmae(self,orig_name:str,project_id:str):
        raddom_key=self.generate_random_string()
        project_path= projectcontrolar().git_project_path(project_id)
        clean_filename =self.get_clean_filename(orig_name)
        new_file_path=os.path.join(project_path,f"{clean_filename}_{raddom_key}")
        while os.path.exists(new_file_path):
            raddom_key=self.generate_random_string()
            new_file_path=os.path.join(project_path,f"{raddom_key}_{clean_filename}")
        return new_file_path , raddom_key + '_'+ clean_filename
    
    def get_clean_filename(self,filename:str):
        clean_filename = re.sub(r'[^\w\.-]', '_', filename.split('.')[0])
        clean_filename=clean_filename.replace(' ','_')
        return clean_filename