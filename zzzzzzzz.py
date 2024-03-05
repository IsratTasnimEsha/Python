#BISMILLAHIR RAHMANIR RAHIM

from kivymd.app import MDApp
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition

subjs=[]


class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)

class FirstPage(Screen):
    def __init__(self, **kwargs):
        super(FirstPage, self).__init__(**kwargs)

        self.box=BoxLayout(orientation='vertical')

        #.........................................................................................1: Part 1.........................................................................................#

        self.input=Label(text='SHIBPUR PILOT MODEL HIGH SCHOOL', color=(0/255, 128/255, 128/255), size_hint=(1, .13), font_size='80sp')
        self.box.add_widget(self.input)

        #.........................................................................................1: Part 2.........................................................................................#

        self.b_grid=GridLayout(rows=1,  size_hint=(1, .08), padding=10, spacing=380)

        #.........................................................................................1: Part 2.1.........................................................................................#

        self.grid=GridLayout(cols=2)

        self.input=Button(text='Class: ')
        self.grid.add_widget(self.input)

        self.input=TextInput()
        self.grid.add_widget(self.input)

        self.b_grid.add_widget(self.grid)

        #.........................................................................................1: Part 2.2.........................................................................................#

        self.grid=GridLayout(cols=2)

        self.input=Button(text='Section: ')
        self.grid.add_widget(self.input)

        self.input=TextInput()
        self.grid.add_widget(self.input)

        self.b_grid.add_widget(self.grid)

        #.........................................................................................1: Part 2.3.........................................................................................#

        self.grid=GridLayout(cols=2)

        self.input=Button(text='Total Subjects: ')
        self.grid.add_widget(self.input)

        self.sub_input=TextInput()
        self.grid.add_widget(self.sub_input)

        self.b_grid.add_widget(self.grid)

        self.box.add_widget(self.b_grid)

        #.........................................................................................1: Part 3.........................................................................................#

        self.s_box=BoxLayout()

        #.........................................................................................1: Part 3.1.........................................................................................#

        self.s_grid1=GridLayout(cols=1, size_hint_x=.07)

        self.input=Label()
        self.s_grid1.add_widget(self.input)

        self.input=Button(text='Roll', color=(1, 1, 1), bold=True,  background_color=(0, 128/255, 0, .5))
        self.s_grid1.add_widget(self.input)

        for i in range(15):
            
            self.input=Button(text=str(i+1), background_color=(0, 128/255, 0, .7))
            self.s_grid1.add_widget(self.input)

        self.s_box.add_widget(self.s_grid1)

        #.........................................................................................1: Part 3.2........................................................................................#

        self.s_grid2=GridLayout(cols=1, size_hint_x=.25)

        self.input=Label()
        self.s_grid2.add_widget(self.input)
            
        self.input=Button(text='Name', color=(1, 1, 1), bold=True,  background_color=(0, 128/255, 0, 1))
        self.s_grid2.add_widget(self.input)

        for i in range(15):

            self.input=TextInput(background_color=(0, 128/255, 0, .6))
            self.s_grid2.add_widget(self.input)

        self.s_box.add_widget(self.s_grid2)

        #.........................................................................................1: Part 3.3.........................................................................................#

        self.s_grid3=GridLayout(cols=14)

        for i in range(14):

            if i%14==13:
                self.input=TextInput(hint_text="Optional", foreground_color=(1, 1, 1), background_color=(192/255, 192/255, 192/255, .1))

            else:
                if i%2==0:
                    self.input=TextInput(hint_text="Subj"+str(i+1), foreground_color=(1, 1, 1), background_color=(0, 128/255, 128/255, .2))
                    
                else:
                    self.input=TextInput(hint_text="Subj"+str(i+1), foreground_color=(1, 1, 1), background_color=(128/255, 128/255, 128/255, .4))

            self.s_grid3.add_widget(self.input)

        self .total_input=[]

        for i in range(14):

            if i%14==13:
                self.total_input.append(TextInput(hint_text='Total', foreground_color=(1, 1, 1), background_color=(192/255, 192/255, 192/255, .3)))
            
            else:

                if i%2==0:
                    self.total_input.append(TextInput(hint_text='Total', foreground_color=(1, 1, 1), background_color=(0, 128/255, 128/255, .4)))

                else:
                    self.total_input.append(TextInput(hint_text='Total', foreground_color=(1, 1, 1), background_color=(128/255, 128/255, 128/255, 1)))

            self.s_grid3.add_widget(self.total_input[i])

        self.t_input=[]

        for i in range(15*14):

            if i%14==13:
                self.t_input.append(TextInput(hint_text= 'Roll:'+str(int(i/14+1)), background_color=(192/255, 192/255, 192/255, .5)))
            
            else:

                if i%2==0:
                    self.t_input.append(TextInput(hint_text= 'Roll:'+str(int(i/14+1)), background_color=(0, 128/255, 128/255, .8)))    

                else:
                    self.t_input.append(TextInput(hint_text= 'Roll:'+str(int(i/14+1)), background_color=(1, 1, 1, 1)))

            self.s_grid3.add_widget(self.t_input[i])


        self.s_box.add_widget(self.s_grid3)

        #.........................................................................................1: Part 3.4.........................................................................................#

        self.s_grid4=GridLayout(cols=3, size_hint_x=.27)

        for i in range(2):
            self.input=Label()
            self.s_grid4.add_widget(self.input)
        
        self.p_input=Button(text='By Marks', on_press=self.position)
        self.s_grid4.add_widget(self.p_input)

        self.input=Button(text='Total Marks', color=(1, 1, 1), bold=True,  background_color=(0, 128/255, 0, .5), on_press=self.totals)
        self.s_grid4.add_widget(self.input)
            
        self.input=Button(text='G.P.A', color=(1, 1, 1), bold=True,  background_color=(0, 128/255, 0, .7), on_press=self.gpa)
        self.s_grid4.add_widget(self.input)

        self.input=Button(text='Position', color=(1, 1, 1), bold=True,  background_color=(128/255, 0, 0, .6))
        self.s_grid4.add_widget(self.input)

        self.b_input=[]
        self.to_input=[]
        self.k=0
        self.l=0

        for i in range(3*15):
            if i%3==0:
                self.b_input.append(Button(background_color=(0, 128/255, 0, .7)))
                self.s_grid4.add_widget(self.b_input[self.k])
                self.k+=1

            elif i%3==1:
                self.to_input.append(Button(background_color=(0, 128/255, 0,  1)))
                self.s_grid4.add_widget(self.to_input[self.l])
                self.l+=1
            
            else:
                self.input=Button(background_color=(128/255, 0, 0, 1))
                self.s_grid4.add_widget(self.input)
            
    
        self.s_box.add_widget(self.s_grid4)
        
        self.box.add_widget(self.s_box)
        
        #.........................................................................................1: Part 4.........................................................................................#
        
        self.grid=GridLayout(rows=1,  size_hint=(1, .08), padding=10, spacing=560)

        self.input=Label()
        self.grid.add_widget(self.input)

        self.input=Label(text='Page-1', bold=True)
        self.grid.add_widget(self.input)

        self.input=Button(text='Next')
        self.input.bind(on_press=self.screen_transition)
        self.grid.add_widget(self.input)

        self.box.add_widget(self.grid)
        
        self.add_widget(self.box)

    #.........................................................................................1: Part 5.........................................................................................#

    def screen_transition(self, *args):
        self.manager.current='second'

    #.........................................................................................1: Part 6.........................................................................................#

    def totals(self, *args):

        for j in range(15):

            self.total_mark=0

            for i in range(j*14, (j+1)*14):

                self.mark=self.t_input[i].text
                
                if self.mark.isdigit():
                    self.total_mark+=int(self.mark)
                
                else:
                    self.total_mark+=0

            self.b_input[j].text=str(self.total_mark)

    #.........................................................................................1: Part 7.........................................................................................#

    def gpa(self, *args):

        self.sub=self.sub_input.text
                    
        if self.sub.isdigit():
            self.totalsubs=int(self.sub)
                    
        else:
            self.totalsubs=14

        self .TotalGPA=[]

        for i in range(14):
            self.mark=self.total_input[i].text
                
            if self.mark.isdigit():
                self.totalgpa=int(self.mark)
                
            else:
                self.totalgpa=100

            self.TotalGPA.append(self.totalgpa)

        
        self.TotalMarks=[]
        
        for j in range(15):
        
            for i in range(j*14, (j+1)*14):

                self.mark=self.t_input[i].text
                    
                if self.mark.isdigit():
                    self.totalmark=int(self.mark)
                    
                else:
                    self.totalmark=0
                
                self.TotalMarks.append(self.totalmark)
        

        for j in range(15):

            self.finalGPA=0
            self.pass_count=0

            for i in range(j*14, (j+1)*14):

                self.per_gpa=self.TotalMarks[i]/self. TotalGPA[i%14]

                if i%14!=13:

                    if self.per_gpa>=0.8:
                        self.finalGPA+=5
                        self.pass_count+=1

                    elif self.per_gpa>=0.7:
                        self.finalGPA+=4
                        self.pass_count+=1
                    
                    elif self.per_gpa>=0.6:
                        self.finalGPA+=3.5
                        self.pass_count+=1

                    elif self.per_gpa>=0.5:
                        self.finalGPA+=3
                        self.pass_count+=1
                    
                    elif self.per_gpa>=0.4:
                        self.finalGPA+=2
                        self.pass_count+=1

                    elif self.per_gpa>=0.33:
                        self.finalGPA+=1
                        self.pass_count+=1
                    
                    else:
                        self.finalGPA+=0
                
                else:

                    if self.per_gpa>=0.8:
                        self.finalGPA+=3

                    elif self.per_gpa>=0.7:
                        self.finalGPA+=2
                    
                    elif self.per_gpa>=0.6:
                        self.finalGPA+=1.5

                    elif self.per_gpa>=0.5:
                        self.finalGPA+=1

            self.t_GPA=min(5.00, self.finalGPA/self.totalsubs)
                
            if self.pass_count==self.totalsubs:
                self.to_input[j].text="{:.2f}".format(self.t_GPA)
                self.to_input[j].color=(1, 1, 1)
            
            else:
                self.to_input[j].text="0.00 ("+str(self.totalsubs-self.pass_count)+")"
                self.to_input[j].color=(1, 0, 0)    
    
    #.........................................................................................1: Part 8.........................................................................................#

    def position(self, *args):

        if self.p_input.text=='By Marks':
            self.p_input.text='By GPA'
        
        else:
            self.p_input.text='By Marks'


class SecondPage(Screen):
    def __init__(self, **kwargs):
        super(SecondPage, self).__init__(**kwargs)
        self.first_page=FirstPage()

        self.box=BoxLayout(orientation='vertical')

        #.........................................................................................1: Part 2.........................................................................................#

        self.b_grid=GridLayout(rows=1,  size_hint=(1, .07), padding=10, spacing=380)

        #.........................................................................................1: Part 2.1.........................................................................................#

        self.grid=GridLayout(cols=2)

        self.input=Button(text='Class: ')
        self.grid.add_widget(self.input)

        self.input=TextInput()
        self.grid.add_widget(self.input)

        self.b_grid.add_widget(self.grid)

        #.........................................................................................1: Part 2.2.........................................................................................#

        self.grid=GridLayout(cols=2)

        self.input=Button(text='Section: ')
        self.grid.add_widget(self.input)

        self.input=TextInput()
        self.grid.add_widget(self.input)

        self.b_grid.add_widget(self.grid)

        #.........................................................................................1: Part 2.3.........................................................................................#

        self.grid=GridLayout(cols=2)

        self.input=Button(text='Total Subjects: ')
        self.grid.add_widget(self.input)

        self.sub_input=TextInput()
        self.grid.add_widget(self.sub_input)

        self.b_grid.add_widget(self.grid)

        self.box.add_widget(self.b_grid)

        #.........................................................................................2: Part 3.........................................................................................#

        self.s_box=BoxLayout()

        #.........................................................................................2: Part 3.1.........................................................................................#

        self.s_grid1=GridLayout(cols=1, size_hint_x=.07)

        self.input=Label()
        self.s_grid1.add_widget(self.input)

        self.input=Button(text='Roll', color=(1, 1, 1), bold=True,  background_color=(0, 128/255, 0, .5))
        self.s_grid1.add_widget(self.input)

        for i in range(18):
            
            self.input=Button(text=str(i+16), background_color=(0, 128/255, 0, .7))
            self.s_grid1.add_widget(self.input)

        self.s_box.add_widget(self.s_grid1)

        #.........................................................................................2: Part 3.2........................................................................................#

        self.s_grid2=GridLayout(cols=1, size_hint_x=.25)

        self.input=Button(text='Get Previous Data')
        self.s_grid2.add_widget(self.input)
            
        self.input=Button(text='Name', color=(1, 1, 1), bold=True,  background_color=(0, 128/255, 0, 1))
        self.s_grid2.add_widget(self.input)

        for i in range(18):

            self.input=TextInput(background_color=(0, 128/255, 0, .6))
            self.s_grid2.add_widget(self.input)

        self.s_box.add_widget(self.s_grid2)

        #.........................................................................................2: Part 3.3.........................................................................................#

        self.s_grid3=GridLayout(cols=14)

        for i in range(14):

            if i%14==13:
                self.input=TextInput(hint_text="Optional", foreground_color=(1, 1, 1), background_color=(192/255, 192/255, 192/255, .1))

            else:
                if i%2==0:
                    self.input=TextInput(hint_text="Subj"+str(i+1), foreground_color=(1, 1, 1), background_color=(0, 128/255, 128/255, .2))
                    
                else:
                    self.input=TextInput(hint_text="Subj"+str(i+1), foreground_color=(1, 1, 1), background_color=(128/255, 128/255, 128/255, .4))

            self.s_grid3.add_widget(self.input)

        self .total_input=[]
        
        

        for i in range(14):

            if i%14==13:
                self.total_input.append(TextInput(hint_text='Total', foreground_color=(1, 1, 1), background_color=(192/255, 192/255, 192/255, .3)))
                
            
            else:

                if i%2==0:
                    self.total_input.append(TextInput(hint_text='Total', foreground_color=(1, 1, 1), background_color=(0, 128/255, 128/255, .4)))
                

                else:
                    self.total_input.append(TextInput(hint_text='Total', foreground_color=(1, 1, 1), background_color=(128/255, 128/255, 128/255, 1)))
                    

            self.s_grid3.add_widget(self.total_input[i])

        self.t_input=[]

        for i in range(18*14):

            if i%14==13:
                self.t_input.append(TextInput(hint_text= 'Roll:'+str(int(i/14+16)), background_color=(192/255, 192/255, 192/255, .5)))
            
            else:

                if i%2==0:
                    self.t_input.append(TextInput(hint_text= 'Roll:'+str(int(i/14+16)), background_color=(0, 128/255, 128/255, .8)))    

                else:
                    self.t_input.append(TextInput(hint_text= 'Roll:'+str(int(i/14+16)), background_color=(1, 1, 1, 1)))

            self.s_grid3.add_widget(self.t_input[i])


        self.s_box.add_widget(self.s_grid3)

        #.........................................................................................2: Part 3.4.........................................................................................#

        self.s_grid4=GridLayout(cols=3, size_hint_x=.27)

        for i in range(2):
            self.input=Label()
            self.s_grid4.add_widget(self.input)

        self.p_input=Button(text='By Marks', on_press=self.position)
        self.s_grid4.add_widget(self.p_input)

        self.input=Button(text='Total Marks', color=(1, 1, 1), bold=True,  background_color=(0, 128/255, 0, .5), on_press=self.totals)
        self.s_grid4.add_widget(self.input)
            
        self.input=Button(text='G.P.A', color=(1, 1, 1), bold=True,  background_color=(0, 128/255, 0, .7), on_press=self.gpa)
        self.s_grid4.add_widget(self.input)

        self.input=Button(text='Position', color=(1, 1, 1), bold=True,  background_color=(128/255, 0, 0, .6))
        self.s_grid4.add_widget(self.input)

        self.b_input=[]
        self.to_input=[]
        self.k=0
        self.l=0

        for i in range(3*18):
            if i%3==0:
                self.b_input.append(Button(background_color=(0, 128/255, 0, .7)))
                self.s_grid4.add_widget(self.b_input[self.k])
                self.k+=1

            elif i%3==1:
                self.to_input.append(Button(background_color=(0, 128/255, 0,  1)))
                self.s_grid4.add_widget(self.to_input[self.l])
                self.l+=1
            
            else:
                self.input=Button(background_color=(128/255, 0, 0, 1))
                self.s_grid4.add_widget(self.input)
            
    
        self.s_box.add_widget(self.s_grid4)
        
        self.box.add_widget(self.s_box)
        
        #.........................................................................................2: Part 4.........................................................................................#
        
        self.grid=GridLayout(rows=1,  size_hint=(1, .07), padding=10, spacing=560)

        self.input=Button(text='Previous')
        self.input.bind(on_press=self.screen_transition)
        self.grid.add_widget(self.input)

        self.input=Label(text='Page-2', bold=True)
        self.grid.add_widget(self.input)

        self.input=Button(text='Next')
        self.grid.add_widget(self.input)

        self.box.add_widget(self.grid)
        
        self.add_widget(self.box)

    #.........................................................................................2: Part 5.........................................................................................#

    def screen_transition(self, *args):
        self.manager.current='first'

    #.........................................................................................2: Part 6.........................................................................................#

    def totals(self, *args):

        for j in range(18):

            self.total_mark=0

            for i in range(j*14, (j+1)*14):

                self.mark=self.t_input[i].text
                
                if self.mark.isdigit():
                    self.total_mark+=int(self.mark)
                
                else:
                    self.total_mark+=0

            self.b_input[j].text=str(self.total_mark)

    #.........................................................................................2: Part 7.........................................................................................#

    def gpa(self, *args):

        self.sub=self.sub_input.text
                    
        if self.sub.isdigit():
            self.totalsubs=int(self.sub)
                    
        else:
            self.totalsubs=14

        self .TotalGPA=[]

        for i in range(14):
            self.mark=self.total_input[i].text
                
            if self.mark.isdigit():
                self.totalgpa=int(self.mark)
                
            else:
                self.totalgpa=100

            self.TotalGPA.append(self.totalgpa)

        
        self.TotalMarks=[]
        
        for j in range(18):
        
            for i in range(j*14, (j+1)*14):

                self.mark=self.t_input[i].text
                    
                if self.mark.isdigit():
                    self.totalmark=int(self.mark)
                    
                else:
                    self.totalmark=0
                
                self.TotalMarks.append(self.totalmark)
        

        for j in range(18):

            self.finalGPA=0
            self.pass_count=0

            for i in range(j*14, (j+1)*14):

                self.per_gpa=self.TotalMarks[i]/self. TotalGPA[i%14]

                if i%14!=13:

                    if self.per_gpa>=0.8:
                        self.finalGPA+=5
                        self.pass_count+=1

                    elif self.per_gpa>=0.7:
                        self.finalGPA+=4
                        self.pass_count+=1
                    
                    elif self.per_gpa>=0.6:
                        self.finalGPA+=3.5
                        self.pass_count+=1

                    elif self.per_gpa>=0.5:
                        self.finalGPA+=3
                        self.pass_count+=1
                    
                    elif self.per_gpa>=0.4:
                        self.finalGPA+=2
                        self.pass_count+=1

                    elif self.per_gpa>=0.33:
                        self.finalGPA+=1
                        self.pass_count+=1
                    
                    else:
                        self.finalGPA+=0
                
                else:

                    if self.per_gpa>=0.8:
                        self.finalGPA+=3

                    elif self.per_gpa>=0.7:
                        self.finalGPA+=2
                    
                    elif self.per_gpa>=0.6:
                        self.finalGPA+=1.5

                    elif self.per_gpa>=0.5:
                        self.finalGPA+=1

            self.t_GPA=min(5.00, self.finalGPA/self.totalsubs)
                
            if self.pass_count==self.totalsubs:
                self.to_input[j].text="{:.2f}".format(self.t_GPA)
                self.to_input[j].color=(1, 1, 1)
            
            else:
                self.to_input[j].text="0.00 ("+str(self.totalsubs-self.pass_count)+")"
                self.to_input[j].color=(1, 0, 0)

    #.........................................................................................1: Part 8.........................................................................................#

    def position(self, *args):

        if self.p_input.text=='By Marks':
            self.p_input.text='By GPA'
        
        else:
            self.p_input.text='By Marks'

class App(MDApp):

    def build(self):
        self.theme_cls.theme_style='Dark'

        screen_manager=ScreenManagement(transition=FadeTransition())
        
        screen_manager.add_widget(FirstPage(name='first'))
        screen_manager.add_widget(SecondPage(name='second'))
        
        return screen_manager

App().run()