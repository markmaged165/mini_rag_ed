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
    

    def genrate_unique_filenmae(self, orig_name: str, project_id: str):
        random_key = self.generate_random_string()
        project_path = projectcontrolar().get_project_path(project_id)
        
        # 1. Safely split the name and the extension
        base_name, file_extension = os.path.splitext(orig_name)
        
        # 2. Clean ONLY the base name (send just the name part to your function)
        clean_base = self.get_clean_filename(base_name)
        
        # 3. Create the new name AND attach the extension back!
        new_file_name = f"{clean_base}_{random_key}{file_extension}"
        new_file_path = os.path.join(project_path, new_file_name)
        
        # 4. Check if it exists (and keep the extension if you have to regenerate)
        while os.path.exists(new_file_path):
            random_key = self.generate_random_string()
            new_file_name = f"{random_key}_{clean_base}{file_extension}"
            new_file_path = os.path.join(project_path, new_file_name)
            
        return new_file_path, new_file_name
    
    def get_clean_filename(self,file_name:str):
        clean_filename = re.sub(r'[^\w\.-]', '_', file_name)
        clean_filename=clean_filename.replace(' ','_')
        return clean_filename 