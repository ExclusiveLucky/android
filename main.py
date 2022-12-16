from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from random import randint
from kivy.core.window import Window
import requests


def get_rofl(type):
    data = requests.get(f"http://rzhunemogu.ru/RandJSON.aspx?CType={type}")
    text = data.text[12:][:-2]
    print(text)
    return text
    

def random_colour():
    return (randint(0, 255)/255,
                              randint(0, 255)/255,
                              randint(0, 255)/255,
                              1)

def colorized():
    Window.clearcolor = 'gray'

class Container(GridLayout):
    def real_time(self):
        self.obj_mid_label.text = get_rofl(1)
        # self.obj_top_label_1.color = random_colour()
        # self.obj_mid_label.color = random_colour()
        colorized()
        
    def real_date(self):
        self.obj_mid_label.text = get_rofl(2)
        # self.obj_top_label_1.color = random_colour()
        # self.obj_mid_label.color = random_colour()
        colorized()
        

    def real_rofl(self):
        self.obj_mid_label.text = get_rofl(3)
        # self.obj_mid_label.text = qwest["question"]
        # self.obj_top_label_1.color = random_colour()
        # self.obj_mid_label.color = random_colour()
        colorized()

class MyApp(App):

    def build(self):
        return Container()





if __name__ == "__main__":
    colorized()
    MyApp().run()
