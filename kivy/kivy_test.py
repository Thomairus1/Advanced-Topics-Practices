from kivy.app import App
from kivy.lang import Builder

class HelloWorldApp(App):
    def build(self):
        return Builder.load_file('ButtonLayout.kv')
    

HelloWorldApp().run()