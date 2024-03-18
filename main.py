from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
import service


# Load the KV file
Builder.load_file("UI.kv")

class MyApp(App):
    def __init__(self):
        super(MyApp, self).__init__()
        self.user_data = UserData()
    
    
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegistrationScreen(name='registration'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.add_widget(LessonTreeScreen(name='lesson_tree'))
        return sm
    
    # Controller functions
    def login_with_email(self, email, password):
        response = service.login_with_email(email, password)
        self.user_data.set_user_id(response.id)
        return response
    
    def login_with_username(self, username, password):
        response = service.login_with_username(username, password)
        self.user_data.set_user_id(response.id)
        return response
    
    
    def get_user_learning_trees(self, user_id):
        """
        Function that retrieves the learning trees a user is assigned to based on their user id
        
        Args:
            user_id (int): The id of the user
        
        Returns:
            list: A list of learning trees the user is assigned to
        """
        user_learning_trees = service.get_user_learning_trees(user_id)
        return user_learning_trees
    
    
    def get_lessons_for_learning_tree(self, learning_tree_id):
        """
        Function that retrieves the list of lessons from the service given the learning tree id
        
        Args:
            learning_tree_id (int): The id of the learning tree
        
        Returns:
            list: A list of lessons associated with the learning tree id
        """
        lessons = service.get_lessons_by_learning_tree_id(learning_tree_id)
        return lessons



class LoginScreen(Screen):
    def login(self, email, password):
        app = App.get_running_app()
        if '@' in email:  # Check if '@' character exists in the input_text
            response = app.login_with_email(email, password)
            print(response)
            authenticated = response
        else:
            response = app.login_with_username(email, password)
            print(response)
            authenticated = response
        print("Login successful:", authenticated)
        print("Login credentials:")
        print("Email/Username:", email)
        print("Password:", password)

        if authenticated:
            app = App.get_running_app().root
            app.current = 'dashboard'


# Crud operations not implemented for registration
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
        # Clear the existing widgets from the layout
        self.ids.learning_trees_layout.clear_widgets()

        # Get the user's learning trees
        app = App.get_running_app()
        user_learning_trees = app.get_user_learning_trees(app.user_data.get_user_id())

        if user_learning_trees:
            # If user is associated with learning trees, create boxes for each learning tree
            for learning_tree in user_learning_trees:
                box = Button(text=learning_tree.name, size_hint_y=None, height=dp(40))
                box.bind(on_press=self.on_learning_tree_pressed)  # Bind the on_press event
                box.learning_tree_id = learning_tree.id  # Assign learning tree ID to button
                
                self.ids.learning_trees_layout.add_widget(box)
        else:
            # If user is not associated with any learning trees, display a message
            label = Label(text="No learning trees associated with the user", size_hint_y=None, height=dp(40))
            self.ids.learning_trees_layout.add_widget(label)

    def on_leave(self):
        """
        Called when the screen is no longer displayed.
        """
        # Remove all the widgets from the layout
        self.ids.learning_trees_layout.clear_widgets()
        
    def on_learning_tree_pressed(self, instance):
        """
        Callback function to handle learning tree button press.
        """
        app = App.get_running_app()
        app.selected_learning_tree_id = instance.learning_tree_id
        app.root.current = 'lesson_tree'
        print(app.selected_learning_tree_id)


class LessonTreeScreen(Screen):
    def on_enter(self):
        """
        Called when the screen is displayed.
        """
        # Clear the existing widgets from the layout
        self.ids.lessons_layout.clear_widgets()

        # Get the lessons associated with the selected learning tree
        app = App.get_running_app()
        selected_learning_tree_id = app.selected_learning_tree_id  # Assuming you have a way to get the selected learning tree ID
        lessons = app.get_lessons_for_learning_tree(selected_learning_tree_id)
        print("lessons", lessons)
        if lessons:
            # If lessons are available, create buttons for each lesson
            for lesson in lessons:
                button = Button(text=lesson.title, size_hint_y=None, height=dp(40))
                self.ids.lessons_layout.add_widget(button)
        else:
            # If no lessons are available, display a message
            label = Label(text="No lessons available for this learning tree", size_hint_y=None, height=dp(40))
            self.ids.lessons_layout.add_widget(label)

    def on_leave(self):
        """
        Called when the screen is no longer displayed.
        """
        # Remove all the widgets from the layout
        self.ids.lessons_layout.clear_widgets()

class UserData():
    def __init__(self):
        self.user_id = None

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_user_id(self):
        return self.user_id
    
    

if __name__ == "__main__":
    MyApp().run()