from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


# Kivy app is made from 4 objects: App, ScreenManager, Screen, Widget
class FirstScreen(Screen):

    def search_image(self):
        pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    """
    The main app class inherits from the Kivy App class
    """

    def build(self):
        return RootWidget()


MainApp().run()
