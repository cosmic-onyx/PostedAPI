import os
from dotenv import load_dotenv


load_dotenv()

POSTGRES_USER=os.getenv('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD', 'postgres')
POSTGRES_HOST=os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PORT=os.getenv('POSTGRES_PORT', '5432')
POSTGRES_DB=os.getenv('POSTGRES_DB_NAME', 'postgres')

ADMIN_LOGIN=os.getenv('ADMIN_LOGIN', 'root')
ADMIN_PASSWORD=os.getenv('ADMIN_PASSWORD', 'root')
ADMIN_EMAIL=os.getenv('ADMIN_EMAIL', 'root@gmail.com')