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
            if type(widofmainlist) in (list, tuple,  str):
                wid = self.freeze(widofmainlist)
                self.add_to_root(wid)
            else:
                self.add_to_root(widofmainlist)


    def freeze(self, wid):
        #list for boxlayout
        if type(wid) is list:
            parent = F.BoxLayout(orientation="horizontal")
            self.row_widget_adder(wid, parent)
            return parent
        #tuple for floatlayout
        elif type(wid) is tuple:
            parent = F.FloatLayout()
            self.row_widget_adder(wid, parent) 
            return parent

        elif type(wid) is str:
            widget = Builder.load_string(wid)
            return widget
        
            

    def add_to_root(self, widget):
        self.add_to_widget(widget, self.root)
        

    def add_to_widget(self, widget, parent):
        try:
            parent.add_widget(widget()) 
        except TypeError:
            parent.add_widget(widget) 

    def row_widget_adder(self, widofmainlist, parent):
        
                
        for item in widofmainlist:
            #put new boxlayout or floatlayout kwargs
            if type(item) is dict:
                parent.__init__(**item)
            elif type(item) in (list, tuple, str):
                wid = self.freeze(item)
                self.add_to_widget(wid, parent)
            else:self.add_to_widget(item, parent)
