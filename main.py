from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from backend import hello_world

# Load the KV file
Builder.load_file("UI.kv")

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        return sm
    
    def backend_hello_world(self):
        message = hello_world()
        self.root.ids.my_label.text = message

class LoginScreen(Screen):
    def login(self, email, password):
        # Here you would typically make a request to your backend server
        # to authenticate the user with the provided email and password.
        # For this example, let's just print the credentials.
        print("Login credentials:")
        print("Email:", email)
        print("Password:", password)

        # After authentication, you can handle the response from the server
        # and navigate to the dashboard screen if login is successful.

        # Example:
        # if login_successful:
        #     self.manager.current = "dashboard_screen"
        # else:
        #     display_error_message()

if __name__ == "__main__":
    MyApp().run()