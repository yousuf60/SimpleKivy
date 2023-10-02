from kivymd.app import MDApp
from kivy.factory import Factory as F
from kivy.lang import Builder

import os.path

from .app_methods import MDAppMethods

file_path = os.path.abspath(os.path.dirname(__file__))
Builder.load_file(os.path.join(file_path, "main.kv"))

class MainApp(MDApp, MDAppMethods):
    on_start = MDAppMethods.on_start

    

