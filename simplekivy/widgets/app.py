from kivy.app import App
from kivy.lang import Builder

Builder.load_file("widgets/main.kv")

class MainApp(App):
    widgets = []
    def on_start(self):
        for i in self.widgets:
            if type(i) is list:pass
            else:    
                self.add_to_root(i)

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