#BISMILLAHIR RAHMANIR RAHIM

from kivymd.app import MDApp
from kivy.core import text #to write a text middle of the screen
from kivy.core.window import Window #to change the color of display
from kivy.uix.label import Label #to write something
from kivy.uix.button import Button #to make button
from kivy.uix.image import Image, AsyncImage #to make Image, AsyncImage for image from internet
from kivy.uix.boxlayout import BoxLayout #for multiple datas (works as loop)
from kivy.uix.gridlayout import GridLayout #to make multiple buttons using rows and columns
from kivy.uix.textinput import TextInput #to take text as input
from kivy.uix.anchorlayout import AnchorLayout #to set the anchor on x, y axes
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout #to make multiple pages
from kivy.lang import Builder #for screen manager
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition#to make multiple screen
from kivy.clock import Clock


class MyApp(MDApp):
   
    def build(self):
        layout = BoxLayout(padding = 10, orientation = 'vertical')

        btn1 = Button(text = "OK")
        btn1.bind(on_press = self.buttonClicked)
        layout.add_widget(btn1)

        self.lbl1 = Label(text = "test")
        layout.add_widget(self.lbl1)

        self.txt1 = TextInput(text = '', multiline = False)
        layout.add_widget(self.txt1)
        
        return layout


    def buttonClicked(self, btn):
        self.lbl1.text = "You wrote " + self.txt1.text
        print(self.lbl1.text)

MyApp().run()