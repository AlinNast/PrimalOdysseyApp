from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from backend import login_user

# Load the KV file
Builder.load_file("UI.kv")

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegistrationScreen(name='registration'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        return sm
    
    def backend_login(self, email, password):
        return login_user(email, password)

class LoginScreen(Screen):
    def login(self, email, password):
        app = App.get_running_app()
        authenticated = app.backend_login(email, password)
        print("Login successful:", authenticated)
        print("Login credentials:")
        print("Email:", email)
        print("Password:", password)

        if authenticated:
            app = App.get_running_app().root
            app.current = 'dashboard'


class RegistrationScreen(Screen):
    def register(self,username, email, password, confirm_password):
        # Basic validation
        if password != confirm_password:
            print("Passwords do not match")
            return

        # Add your registration logic here
        print("Registration successful")
        print("Registration credentials:")
        print("Username:", username)
        print("Email:", email)
        print("Password:", password)
        
        # Navigate to login screen
        app = App.get_running_app().root
        app.current = 'login'


class DashboardScreen(Screen):
    def on_enter(self):
        """
        Called when the screen is displayed.
        """
        # Build a label with some text.
        label = Label(text="Welcome to the Dashboard!")

        # Add the label to the screen's layout.
        self.add_widget(label)

    def on_leave(self):
        """
        Called when the screen is no longer displayed.
        """
        # Remove all the widgets from the screen.
        self.clear_widgets()



if __name__ == "__main__":
    MyApp().run()