import sys, os
from flask import Flask

WIN = sys.platform.startswith('win')
if WIN: 
    # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:
    # 否则使用四个斜线
    prefix = 'sqlite:////'

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev')

from app import views