# import os 
# from . common import *


# SECRET_KEY = os.environ['SECRET_KEY']

# DEBUG = False 

# ALLOWED_HOSTS = ['*']



import os
from .common import *

SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-secret-key')

DEBUG = False

ALLOWED_HOSTS = ['*']  # You can replace '*' with your Railway domain later

# # Static files (if not already in common.py)
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# # Whitenoise for static file serving
# MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
