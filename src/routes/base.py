from fastapi import FastAPI ,APIRouter , Depends
import os
from helpers.config import get_settings ,settings
base_router =APIRouter(
    prefix='/api/v1',
    tags=['api_v1']
)
## dependss use it more effeciant and organize 
@base_router.get('/')
async def welcome (app_settings: settings =Depends(get_settings)):

    # app_settings=get_settings()

    app_name =app_settings.app_name
    app_ver=app_settings.app_version
    return{
        'app_name':app_name ,
        'app_version':app_ver,
        }
