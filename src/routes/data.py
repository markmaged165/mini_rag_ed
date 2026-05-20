from fastapi import FastAPI ,APIRouter , Depends , UploadFile,status
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings ,settings
from controllers import datacontrolar , projectcontrolar
from model import responsesignal
import aiofiles
import logging

logging.basicConfig(level=logging.INFO)


data_router =APIRouter(
    prefix='/api/v1/data',
    tags=['api_v1','data']
)

##  multi_tenents
@data_router.post("/upload/{project_id}")
async def upload_data(project_id:str,file:UploadFile,
        app_settings: settings = Depends(get_settings)):
    
    
    ## validate the file properties
    is_valid ,resalt_signals= datacontrolar().validate_uploaded_file(file=file)
    if not is_valid:
        return JSONResponse( 
            status_code=status.HTTP_400_BAD_REQUEST ,
            content={
                "signal":resalt_signals
                }
        )
    ## upload the file by chunks 
    project_dir_path = projectcontrolar().git_project_path(project_id=project_id)

    file_path , file_id = datacontrolar().genrate_unique_filenmae(orig_name=file.filename
                            ,project_id=project_id
                        )



    ## save the file in chunks
    try:
        await file.seek(0)
        async with aiofiles.open(file_path,'wb')as f:
            while chunk :=await file.read(app_settings.file_default_chunk_size):
                await f.write(chunk)
    except Exception as e:
        logging.error(f"Error uploading file: {e}")
        return JSONResponse( 
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR ,
            content={
                "signal":responsesignal.FILE_UPLOAD_FAILED.value,
                "error":str('An error occurred while uploading the file.')
                }
        )
    return JSONResponse( 
         {
                "signal":responsesignal.FILE_UPLOAD_SUCCESS.value
                ,'file_id':file_id
                }
            )
