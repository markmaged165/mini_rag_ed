from .base_controlar import basecontrolar
from .project_controlar import projectcontrolar 
import os
from langchain_community.document_loaders import TextLoader, PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from model import processingenum


class processcontrolar (basecontrolar):
    def __init__(self,project_id:str):
        super().__init__()
        self.project_id =project_id
        self.project_path =projectcontrolar().get_project_path(project_id)

    def get_file_extension(self,file_id:str):

        return os.path.splitext(file_id)[-1]


    def get_file_loader(self, file_id: str):
        file_ext = self.get_file_extension(file_id)

        file_path = os.path.join(
            self.project_path, 
            file_id
        )
        
        # ✨ DEBUG CHECK: Print this to your terminal to verify the file is really on your hard drive!
        if not os.path.exists(file_path):
            print(f"🚨 CRITICAL ERROR: The file is missing from the hard drive at: {file_path}")
            return None # This will trigger your get_file_content HTTPException
        
        if file_ext == processingenum.TXT.value or file_ext == '':
            return TextLoader(file_path, autodetect_encoding=True)
        
        if file_ext == processingenum.PDF.value:
            return PyMuPDFLoader(file_path)
        
        return None 
    

    def get_file_content(self,file_id:str):
        loader= self.get_file_loader(file_id)
        return loader.load()


    def process_file_content(self,file_content:list
                             , chunk_size:int=100,overlap_size:int=20):
        
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,
                                                chunk_overlap=overlap_size,
                                                length_function=len)
        file_content_texts=[
            rec.page_content
            for rec in file_content
        ]
        file_content_metadata=[

            rec.metadata
            for rec in file_content
        ]
        chunk=text_splitter.create_documents(file_content_texts,
                            metadatas=file_content_metadata
                            )
        return chunk
    