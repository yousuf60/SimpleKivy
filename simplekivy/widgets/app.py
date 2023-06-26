from kivy.app import App
from kivy.factory import Factory as F
from kivy.lang import Builder

Builder.load_file("widgets/main.kv")

class MainApp(App):
    widgets = []
    def on_start(self):
        for widofmainlist in self.widgets:
            #list for boxlayout
            if type(widofmainlist) is list:
                parent = F.BoxLayout(orientation="horizontal")
                self.row_widget_adder(widofmainlist, parent)

            #list for floatlayout
            elif type(widofmainlist) is tuple:
                parent = F.FloatLayout()
                self.row_widget_adder(widofmainlist, parent) 
                
            else:    
                self.add_to_root(widofmainlist)

    def add_to_root(self, widget):
        self.add_to_widget(widget, self.root)
        

    def add_to_widget(self, widget, parent):
        try:
            parent.add_widget(widget()) 
        except TypeError:
            parent.add_widget(widget) 

    def row_widget_adder(self, widofmainlist, parent):
        for item in widofmainlist:
            self.add_to_widget(item, parent)
        self.add_to_root(parent)        