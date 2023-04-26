from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
"""
Kivy app is made from 4 objects: App, ScreenManager, Screen, Widget.
This code is called boilerplate. We will use these 4 classes with every Kivy app.
"""

Builder.load_file('frontend.kv')
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
