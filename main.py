import time

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests

"""
Kivy app is made from 4 objects: App, ScreenManager, Screen, Widget.
This code is called boilerplate. We will use these 4 classes with every Kivy app.
"""

Builder.load_file('frontend.kv')


class FirstScreen(Screen):

    def search_image(self):

        # Get user query from TextInput
        query = self.manager.current_screen.ids.txt_input.text

        # Get an image matching the query using wikipedia lib
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
        }
        try:
            # Get the image link
            page = wikipedia.page(query)
            link = page.images[0]
            r = requests.get(link, headers=headers)

            # Save the image in the same directory
            with open(f'files/{query}.jpg', 'wb') as f:
                f.write(r.content)

            time.sleep(2)
            # Set the FirstScreen image to the downloaded image
            self.manager.current_screen.ids.img.source = f'files/{query}.jpg'
        except wikipedia.exceptions.DisambiguationError:
            return 'Try being more specific'


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    """
    The main app class inherits from the Kivy App class
    """

    def build(self):
        return RootWidget()


MainApp().run()
