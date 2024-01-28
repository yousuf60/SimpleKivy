
import kivy
from kivy.factory import Factory as F

from time import sleep


class SimpleKivy:
    def __init__(self, make_app=True, md_mode= False, *args, **kwargs):
        self.md_mode = md_mode
        if make_app:
            if not md_mode:
                from .widgets.app import MainApp
            else:
                from .widgets.mdapp import MainApp

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

        elif self.md_mode:
            import kivymd
            if hasattr(kivymd, attr):
                return getattr(kivymd, attr)
        raise Exception(attr + " doasn't exists")
            
    def get_running_app(self):
        return kivy.app.App.get_running_app()

    def build(self, widgets):
        from .widgets.app_methods import AppMethods, MDAppMethods
        
        if not self.md_mode:
            app = AppMethods()
        else:
            app = MDAppMethods()
        widget = app.freeze(widgets)
        return widget