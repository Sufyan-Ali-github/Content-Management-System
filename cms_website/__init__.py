from flask import Flask




app=Flask(__name__)
app.config['SECRET_KEY']="abcdsgyged"

from .index import *
from .authorization import *
from .home import *
from .action import *


