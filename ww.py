from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config


Config.set("graphics", "resizble", 0)
Config.set("graphics", "width", 600)
Config.set("graphics", "height", 600)

class Application(App):

    def clic(self, instance):
        self.label.text = "текс655т"

    
    def click(self, instance):
        self.label.text = "текст"



        
    def build(self):


        but_together = BoxLayout()
        grid = GridLayout(cols=1)

        
        my_but = Button(text="1", font_size=30, background_color="blue", on_press=self.click)

        my2_but = Button(text="2", font_size=30, background_color="blue", on_press=self.clic)
        self.label = Label(text="3", font_size=30)


        but_together.add_widget(my_but)
        but_together.add_widget(my2_but)

        grid.add_widget(but_together)
        grid.add_widget(self.label)

        
        return grid





if __name__ == "__main__":
    Application().run()
