from kivy.app import App
from kivy.lang import Builder

Builder.load_file("widgets/main.kv")

class MainApp(App):
    widgets = []
    def on_start(self):
        for widofmainlist in self.widgets:
            #list for boxlayout
            if type(widofmainlist) is list:pass
            #list for floatlayout
            elif type(widofmainlist) is tuple:pass
            else:    
                self.add_to_root(widofmainlist)

    def add_to_root(self, widget):
        self.add_to_widget(widget, self.root)
        # try:
        #     self.root.add_widget(widget()) 
        # except TypeError:
        #     self.root.add_widget(widget) 

    def add_to_widget(self, widget, parent):
        try:
            parent.add_widget(widget()) 
        except TypeError:
            parent.add_widget(widget) 