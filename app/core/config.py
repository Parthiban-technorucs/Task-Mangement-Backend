from dotenv import load_dotenv
import os

load_dotenv()
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_server = os.getenv('DB_SERVER')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
secret_key = os.getenv('SECRET_KEY')
jwt_token_name = os.getenv('TOKEN_NAME')

DB_URL = f'mysql+pymysql://{db_user}:{db_pass}@{db_server}:{db_port}/{db_name}'