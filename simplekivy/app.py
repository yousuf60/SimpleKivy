from kivy.app import App
from kivy.lang import Builder


class MainApp(App):
    widgets = []
    def on_start(self):
        for i in self.widgets:
            try:
                self.root.add_widget(i()) 
            except TypeError:
                self.root.add_widget(i) 

