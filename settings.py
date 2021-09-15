import os
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

MY_CONTENT = os.environ.get('MY_CONTENT')
