from kivy.app import App
from kivy.factory import Factory as F
from kivy.lang import Builder

import os.path

file_path = os.path.abspath(os.path.dirname(__file__))
print(file_path)
Builder.load_file(os.path.join(file_path, "main.kv"))

class MainApp(App):
    widgets = []
    def on_start(self):
        
        for widofmainlist in self.widgets:
            if type(widofmainlist) in (list, tuple, str):
                self.freeze(widofmainlist)
            else:
                self.add_to_root(widofmainlist)


    def freeze(self, wid):
        #list for boxlayout
        if type(wid) is list:
            parent = F.BoxLayout(orientation="horizontal")
            self.row_widget_adder(wid, parent)

        #tuple for floatlayout
        elif type(wid) is tuple:
            parent = F.FloatLayout()
            self.row_widget_adder(wid, parent) 

        elif type(wid) is str:
            widget = Builder.load_string(wid)
            self.add_to_root(widget)

            

    def add_to_root(self, widget):
        self.add_to_widget(widget, self.root)
        

    def add_to_widget(self, widget, parent):
        try:
            parent.add_widget(widget()) 
        except TypeError:
            parent.add_widget(widget) 

    def row_widget_adder(self, widofmainlist, parent):
        
        for item in widofmainlist:
            print(item)
            #put new boxlayout or floatlayout kwargs
            if type(item) is dict:
                parent.__init__(**item)
                print("dict")
            elif type(item) in (list, tuple, str):
                self.freeze(item)
            else:self.add_to_widget(item, parent)
        self.add_to_root(parent)        
