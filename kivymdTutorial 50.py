#BISMILLAHIR RAHMANIR RAHIM

from kivymd.app import MDApp
#from kivy.core import text #to write a text
#from kivy.core.window import Window #to change the color of display
from kivymd.uix.label import Label
from kivymd.uix.screen import Screen #to make screen
from kivy.uix.screenmanager import Screen, ScreenManager #to make multiple screen
from kivy.lang import Builder #for screen manager
#from kivymd.uix.mdlabel import MDLabel #to write something
#from kivy.uix.button import Button #to make button
#from kivy.uix.image import Image, AsyncImage #to make Image, AsyncImage for image from internet
#from kivy.uix.boxlayout import BoxLayout #for multiple datas (works as loop)
#from kivy.uix.gridlayout import GridLayout #to make multiple buttons using rows and columns
#from kivy.uix.textinput import TextInput #to take text as input
#from kivy.uix.anchorlayout import AnchorLayout #to set the anchor on x, y axes
#from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.pagelayout import PageLayout #to make multiple pages

#Window.clearcolor=(0,0,0,0) #changing color of the window
#Window.size=(1000, 720) #for fixed size

##........................................................................................................THEME...............................................................................................................##
'''
class MyThemeApp(MDApp): #NothingApp(App): Nothing is the title and App is used to run the code
    def build(self):
        self.theme_cls.theme_style='Dark' #or can be 'Light'

MyThemeApp().run()
'''

##........................................................................................................PROPERTY CHANGE...............................................................................................................##

class MyTextFileApp(MDApp): #NothingApp(App): Nothing is the title and App is used to run the code
    def build(self):
        return MDTextField()

MyTextFileApp().run()