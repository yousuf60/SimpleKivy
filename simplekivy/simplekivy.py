import kivy
from kivy.factory import Factory as F
from kivy.clock import mainthread

from threading import Thread
from time import sleep

from widgets import MainApp


class SimpleKivy:
    def __init__(self, *args, **kwargs):
        self.app = MainApp(*args, **kwargs)
        
    #use + to add widgets
    def __add__(self, widgets):
        self.app.widgets = widgets
        self.app.run()        
         

    def __getattr__(self, attr):
        if hasattr(kivy, attr):
            return getattr(kivy, attr)

        elif hasattr(F, attr):
            return getattr(F, attr)

        else:
            raise Exception(attr + " doasn't exists")




if __name__ == "__main__":
    s = SimpleKivy(title = "gsg")
    s + [[
        s.Button(text="gdddg"),
        s.Button(text="gdgdd")],
        (
        s.Label(text="ffljwfe", pos_hint={"center_x":.1, "center_y":.5}),
        s.Label(text="ffljwfe", pos_hint={ "center_y":.5}),),
        [s.Button(text="third button"), s.Button(text="third button")],
        [s.Button(text="third button"), s.Button(text="third button")],
    ]