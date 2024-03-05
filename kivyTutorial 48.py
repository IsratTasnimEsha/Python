#BISMILLAHIR RAHMANIR RAHIM

from kivy.app import App
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
from kivy.uix.screenmanager import Screen, ScreenManager #to make multiple screen

Window.clearcolor=(0,0,0,0) #changing color of the window
Window.size=(1000, 720) #for fixed size

##........................................................................................................LABEL...............................................................................................................##
'''
class MyLabelApp(App): #NothingApp(App): Nothing is the title and App is used to run the code
    def build(self):
    
        return Label(text="ISRAT TASNIM ESHA", font_size="60sp", bold="True", color=(0,0,0))
        #if it was Label(), nothing would be printed in the middle of the screen

MyLabelApp().run()
'''

##........................................................................................................BUTTON...............................................................................................................##
'''
class MyButtonApp(App): #NothingApp(App): Nothing is the title and App is used to run the code
    def build(self):
    
        self.button=Button(text="Click Me", size_hint=(0.3, 0.3), pos_hint={"center_x": 0.5, "center_y": 0.5}, font_size="50sp", color=(1,1,1), on_press=self.button_click, on_release=self.button_release)
        return self.button

    def button_click(self, submit): #no work of submit argument. button_click function needs 2 arguments that's why it is used
        print("Button clicked")

    def button_release(self, submit):
        print("Button Released")

MyButtonApp().run()
'''

##........................................................................................................IMAGE...............................................................................................................##
'''
class MyImageApp(App):
    def build(self):
        return Image(source="E:\\Photos\\My Photos\\258775307_423336779258770_1870097765813274698_n.jpg", size_hint=(None, None), width=200, height=500, pos_hint={"center_x": 0.5, "center_y": 0.5})

MyImageApp().run()
'''

##........................................................................................................ASYNCIMAGE...............................................................................................................##
'''
class MyAsyncImageApp(App):
    def build(self):
        return AsyncImage(source="https://c4.wallpaperflare.com/wallpaper/770/262/422/himchori-coxs-bazar-bangladesh-wallpaper-preview.jpg")

MyAsyncImageApp().run()
'''

##........................................................................................................BOXLAYOUT...............................................................................................................##
'''
class MyBoxLayoutApp(App): #NothingApp(App): Nothing is the title and App is used to run the code
    def build(self):
    
        self.layout= BoxLayout(orientation="vertical", spacing=30, padding=50) #BoxLayout() places datas horizontally
        
        self.button1=Button(text="Button 1", font_size="80sp", color=(1,1,1))
        self.layout.add_widget(self.button1)
        
        self.button2=Button(text="Button 2", font_size="80sp", color=(1,1,1))
        self.layout.add_widget(self.button2)

        self.button3=Button(text="Button 3", font_size="80sp", color=(1,1,1))
        self.layout.add_widget(self.button3)

        self.button4=Button(text="Button 4", font_size="80sp", color=(1,1,1))
        self.layout.add_widget(self.button4)

        return self.layout

MyBoxLayoutApp().run()
'''

##........................................................................................................GRIDLAYOUT...............................................................................................................##
'''
class MyGirdLayoutApp(App): #NothingApp(App): Nothing is the title and App is used to run the code
    def build(self):

        self.layout= GridLayout(rows=3, row_force_default=True, row_default_height=200) #all buttons will be set in three rows. GridLayout(cols= ) can also be used
        
        self.button1=Button(text="Button 1", font_size="30sp", color=(1,1,1))
        self.layout.add_widget(self.button1)
        
        self.button2=Button(text="Button 2", font_size="30sp", color=(1,1,1))
        self.layout.add_widget(self.button2)

        self.button3=Button(text="Button 3", font_size="30sp", color=(1,1,1))
        self.layout.add_widget(self.button3)

        self.button4=Button(text="Button 4", font_size="30sp", color=(1,1,1))
        self.layout.add_widget(self.button4)

        self.button5=Button(text="Button 5", font_size="30sp", color=(1,1,1))
        self.layout.add_widget(self.button5)

        return self.layout
MyGirdLayoutApp().run()
'''

##........................................................................................................TEXTINPUT...............................................................................................................##
'''
class MyTextInputApp(App): #NothingApp(App): Nothing is the title and App is used to run the code
    def build(self):

        self.layout= BoxLayout(orientation="vertical", padding=200, spacing=50) #all buttons will be set in three rows. GridLayout(cols= ) can also be used

        self.email=TextInput(text="Enter Your E-mail", font_size="30sp")
        self.layout.add_widget(self.email)

        self.password=TextInput(text="Enter Your Password", font_size="30sp")
        self.layout.add_widget(self.password)

        self.button=Button(text="Log In", font_size="30sp", color=(1,1,1), on_press=self.submit_button)
        self.layout.add_widget(self.button)

        return self.layout

    def submit_button(self, submit): #no work of submit argument. button_click function needs 2 arguments that's why it is used
        print(f"Your E-mail is: {self.email.text}")
        print(f"Your Password is: {self.password.text}")

MyTextInputApp().run()
'''

##........................................................................................................ANCHOR LAYOUT...............................................................................................................##
'''
class MyAnchorLayoutApp(App): #NothingApp(App): Nothing is the title and App is used to run the code
    def build(self):

        self.layout= AnchorLayout(anchor_x="right", anchor_y="top")#anchor is set on top right, so data will be placed on top right

        self.button=Button(text="Click Me", font_size="80sp", color=(1,1,1), size_hint=(None, None), width=500)
        self.layout.add_widget(self.button)

        return self.layout

MyAnchorLayoutApp().run()
'''

##........................................................................................................FLOAT LAYOUT...............................................................................................................##
'''
class MyFloatLayoutApp(App): #NothingApp(App): Nothing is the title and App is used to run the code
    def build(self):
        
        self.layout=FloatLayout()
        
        self.button=Button(text="Click Me", font_size="80sp", size_hint=(None, None), width=500, pos_hint={"center_x": 0.7, "center_y": 0.3})
        self.layout.add_widget(self.button)
        
        return self.layout

MyFloatLayoutApp().run()
'''

##........................................................................................................PAGE LAYOUT...............................................................................................................##
'''
class MyPageLayoutApp(App): #NothingApp(App): Nothing is the title and App is used to run the code
    def build(self):

        self.layout= PageLayout() #making individual pages for each data

        self.button1=Button(text="Button 1", font_size="80sp", color=(1,1,1), size_hint=(None, None), width=500)
        self.layout.add_widget(self.button1)

        self.button2=Button(text="Button 2", font_size="80sp", color=(1,1,1), size_hint=(None, None), width=500)
        self.layout.add_widget(self.button2)

        return self.layout

MyPageLayoutApp().run()
'''

##........................................................................................................SCREEN MANAGER...............................................................................................................##

Builder.load_string("""

<ScreenOne>:
    name: "screen_one"    
    Button:
    
        text: "Home Page"
        font_size: "100sp"
        background_color : 0,0,1,1 

        on_press: 
            root.manager.transition.direction = 'left' #direction of the slide
            root.manager.transition.duration = 2 #duration of the change in second
            root.manager.current = 'screen_two' #next page where i wanna go

   
<ScreenTwo>:
    name: "screen_two"    
    Button:
    
        text: "1st Sub Page"
        font_size: "100sp"
        background_color : 1,0,1,1 

        on_press: 
            root.manager.transition.direction = 'left' #direction of the slide
            root.manager.transition.duration = 2 #duration of the change in second
            root.manager.current = 'screen_three' #next page where i wanna go

<ScreenThree>: 
    name: "screen_three"    
    Button:
    
        text: "2nd Sub Page"
        font_size: "100sp"
        background_color : 1,0,0,1 
    
        on_press: 
            root.manager.transition.direction = 'right' #direction of the slide
            root.manager.transition.duration = 2 #duration of the change in second
            root.manager.current = 'screen_one' #next page where i wanna go
""")

screen_manager = ScreenManager() #ScreenManager controls moving between screens

class ScreenOne(Screen): 
    pass
screen_manager.add_widget(ScreenOne())

class ScreenTwo(Screen): 
    pass
screen_manager.add_widget(ScreenTwo())

class ScreenThree(Screen): 
    pass 
screen_manager.add_widget(ScreenThree()) 

class MyScreenManagerApp(App):
    def build(self): 
        return screen_manager  

MyScreenManagerApp().run()