from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from backend import hello_world

# Load the KV file
Builder.load_file("UI.kv")

class MyApp(App):
    def build(self):
        return MyLayout()
    
    def backend_hello_world(self):
        message = hello_world()
        self.root.ids.my_label.text = message

class MyLayout(BoxLayout):
    pass

if __name__ == "__main__":
    MyApp().run()