
import kivy
from kivy.factory import Factory as F
from kivy.clock import mainthread

from threading import Thread
from time import sleep

from .widgets import MainApp, AppMethods


class SimpleKivy:
    def __init__(self, make_app=True, *args, **kwargs):
        if make_app:
            self.myapp = MainApp(*args, **kwargs)
        
    #use + to add widgets
    def __add__(self, widgets):
        self.myapp.widgets = widgets
        self.myapp.run()        
         
   
    def __getattr__(self, attr):
        if hasattr(kivy, attr):
            return getattr(kivy, attr)

        elif hasattr(F, attr):
            return getattr(F, attr)

        else:
            raise Exception(attr + " doasn't exists")
    def get_running_app(self):
        return kivy.app.App.get_running_app()

    def build(self, widgets):
        app = AppMethods()
        widget = app.freeze(widgets)
        return widget