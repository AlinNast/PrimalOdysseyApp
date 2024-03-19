from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.dropdown import DropDown
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
        sm.add_widget(LessonScreen(name='lesson'))
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(ProfileScreen(name='profile'))

        
        return sm
        
    def get_user(self, user_id):
        return service.get_user(user_id)
    
    
    def open_menu(self):
        app = App.get_running_app()
        app.root.current = 'menu'
    
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

    
    def get_lesson(self, lesson_id):
        """
        Function that retrieves the lesson from the service given the lesson id
        
        Args:
            lesson_id (int): The id of the lesson
        
        Returns:
            Lesson: The lesson associated with the lesson id
        """
        lesson = service.get_lesson_by_id(lesson_id)
        return lesson


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
        if lessons:
            # If lessons are available, create buttons for each lesson
            for lesson in lessons:
                lesson_button = Button(text=lesson.title, size_hint_y=None, height=dp(40))
                lesson_button.bind(on_press=self.on_lesson_pressed)  # Bind the on_press event
                lesson_button.lesson_id = lesson.id  # Assign lesson ID to button
                self.ids.lessons_layout.add_widget(lesson_button)
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
        
    
    def on_lesson_pressed(self, instance):
        """
        Callback function to handle lesson button press.
        """
        app = App.get_running_app()
        app.selected_lesson_id = instance.lesson_id
        app.root.current = 'lesson'
        


class LessonScreen(Screen):
    def on_enter(self):
        """
        Called when the screen is displayed.
        """
        # Clear the existing widgets from the layout
        self.ids.lesson_layout.clear_widgets()

        # Get the selected lesson id from the app
        app = App.get_running_app()
        selected_lesson_id = app.selected_lesson_id

        # Get the details of the selected lesson
        selected_lesson = app.get_lesson(selected_lesson_id)

        # Create and add Label widgets for the title and description
        title_label = Label(text=selected_lesson.title, font_size="24sp", bold=True)
        description_label = Label(text=selected_lesson.description)

        # Add the Label widgets to the lesson_layout
        self.ids.lesson_layout.add_widget(title_label)
        self.ids.lesson_layout.add_widget(description_label)


class MenuScreen(Screen):
    def on_enter(self):
        """
        Called when the screen is displayed.
        """
        self.ids.menu_layout.transition = 'slide_right'
        self.ids.menu_layout.transition_duration = 0.2
        
        app = App.get_running_app()
        
        self.ids.menu_layout.clear_widgets()
        
        # Create user profile button and bind it to switch to user profile on press
        user_profile_button = Button(text='User Profile', size_hint_y=None, height=dp(40))
        user_profile_button.bind(on_press=self.on_profile_button_pressed)
        self.ids.menu_layout.add_widget(user_profile_button)
        
        
        # Create dashboard button and bind it to switch to dashboard screen on press
        dashboard_button = Button(text='Dashboard', size_hint_y=None, height=dp(40))
        dashboard_button.bind(on_press=self.on_dashdoard_button_pressed)
        self.ids.menu_layout.add_widget(dashboard_button)
        
        

    def on_menu_button_pressed(self, instance):
        """
        Callback function to handle menu button press.
        """
        app = App.get_running_app()
        app.root.switch_screen(instance.text.lower())
    
    def on_profile_button_pressed(self, instance):
        """
        Callback function to handle profile button press.
        """
        app = App.get_running_app()
        app.root.current = 'profile'
    
    def on_dashdoard_button_pressed(self, instance):
        """
        Callback function to handle dashboard button press.
        """
        app = App.get_running_app()
        app.root.current = 'dashboard'


class ProfileScreen(Screen):
    def on_enter(self):
        """
        Called when the screen is displayed.
        """
        app = App.get_running_app()

        # Clear the existing widgets from the layout
        self.ids.profile_layout.clear_widgets()

        # Get the user information from the controller
        user_id = app.user_data.get_user_id()
        user_info = app.get_user(user_id)

        # Create and add Label widgets for the username and email
        username_label = Label(text=f"Username: {user_info.username}")
        email_label = Label(text=f"Email: {user_info.email}")

        # Add the Label widgets to the profile_layout
        self.ids.profile_layout.add_widget(username_label)
        self.ids.profile_layout.add_widget(email_label)


class UserData():
    def __init__(self):
        self.user_id = None

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_user_id(self):
        return self.user_id
    
    

if __name__ == "__main__":
    MyApp().run()