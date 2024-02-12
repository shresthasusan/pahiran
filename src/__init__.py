from flask import Flask
import secrets

app = Flask(__name__,template_folder='Templates')

from . import routes