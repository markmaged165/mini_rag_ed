from pydantic_settings import BaseSettings , SettingsConfigDict

class settings (BaseSettings):
    app_name: str
    app_version:str
    openai_api_key:str
    file_allowed_types:list
    file_max_size:int

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding='utf-8',
        extra='ignore' # This prevents crashes if you have extra stuff in your .env
    )
    # class config :
    #     env_file ='.env'
def get_settings():
    return settings()
# print('done')
