from kivy.app import App
from kivy.factory import Factory as F
from kivy.lang import Builder

import os.path

file_path = os.path.abspath(os.path.dirname(__file__))
print(file_path)
Builder.load_file(os.path.join(file_path, "main.kv"))


class AppMethods:
    def freeze(self, wid, parent = None):
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

        elif type(wid) is dict:
            if parent:
                self.row_widget_adder([wid], parent)

            else:
                widgets = self.row_widget_adder([wid])
                return widgets
            
    
        elif type(wid) is str:
            widget = Builder.load_string(wid)
            return widget

        else:
            return wid
            
        
    def add_to_root(self, widget):
        self.add_to_widget(widget, self.root)
        

    def add_to_widget(self, widget, parent):
        try:
            parent.add_widget(widget()) 
        except TypeError:
            parent.add_widget(widget) 

    def row_widget_adder(self, widofmainlist, parent=None):
        if not parent:
            dict_keys = []
        for item in widofmainlist:
        
            if type(item) is dict:
                items = item.copy().items()
                for key, value in items:
                    if type(key) is not str :
                        try:keyI = key()  #keyI => keyInstance
                        except: keyI = key
                        wid = self.freeze(value, parent = keyI)
                        if wid:
                            self.add_to_widget(wid, keyI)

                        if parent:
                            self.add_to_widget(keyI, parent)
                        else:
                            dict_keys.append(keyI)

                        del item[key]

                parent.__init__(**item)
                if not parent:
                    return dict_keys
            elif type(item) in (list, tuple, str):
                wid = self.freeze(item)
                self.add_to_widget(wid, parent)
            else:self.add_to_widget(item, parent)


class MainApp(App, AppMethods):
    widgets = []
    def on_start(self):
        for widofmainlist in self.widgets:
            if type(widofmainlist) in (list, tuple,  str):
                wid = self.freeze(widofmainlist)
                self.add_to_root(wid)

            elif type(widofmainlist) is dict:
                self.freeze(widofmainlist, parent=self.root)
            else:
                self.add_to_root(widofmainlist)


