from kivy.app import App
from kivy.factory import Factory as F
from kivy.lang import Builder

import os.path

from .app_methods import AppMethods

file_path = os.path.abspath(os.path.dirname(__file__))

Builder.load_file(os.path.join(file_path, "main.kv"))

class MainApp(App, AppMethods):
    on_start = AppMethods.on_start
    
    

