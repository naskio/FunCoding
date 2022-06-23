from environs import Env
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

env = Env()
env.read_env(path=str(BASE_DIR / '.env'))

DATA_DIR = BASE_DIR / 'data'

DEBUG = env.bool('DEBUG', False)

HTTP_BASIC_USERNAME = env.str('HTTP_BASIC_USERNAME', None)
HTTP_BASIC_PASSWORD = env.str('HTTP_BASIC_PASSWORD', None)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', [])
