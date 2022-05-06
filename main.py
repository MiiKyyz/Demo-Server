from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.animation import Animation
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
import random
import server
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.label import MDLabel
from kivymd.uix.snackbar import Snackbar
from kivy.utils import platform
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconLeftWidget



class Main_Server_Gemys(Widget):
    time = 0
    balls_pos = []
    balls_color = []
    NUM_BALL_SNOW = 50
    people_active = []
    people_connected = {}
    Users_connected = {}

    numver = 0

    connect = False
    def __init__(self, **kwargs):
        super(Main_Server_Gemys, self).__init__(**kwargs)

        self.people_connected = server.Gemys_Server.list_of_people_connected
        self.Users_connected = server.Gemys_Server.list_of_people_connected

        self.balls()
        self.anim(None)
        self.people_active = server.Gemys_Server.list_of_ip

    miky = 0




    old = 0
    def addy(self, m):
        self.miky += 1
        self.apa = False
        #print(f'test: {self.miky}, {self.people_connected}, new')

        if len(self.people_connected) != self.old:
            if self.people_connected:

                print(f'lista: {self.people_connected}')
                for name, ip in self.people_connected.items():
                    print(name)
                    print(ip)
                    miky = ThreeLineAvatarIconListItem(text=f'New User',secondary_text=f"name: {name}",tertiary_text=f"{ip[0]}")

                    self.ids.list_users.add_widget(miky)

                self.old += 1
                self.people_connected = {}

            else:
                pass


        elif len(self.people_connected) == self.old:
            pass











    def timer_funct(self, instance):

        self.ids.people.text = f'Users:{len(self.people_active)}'



    def balls(self):
        for i in range(self.NUM_BALL_SNOW):
            X = random.randint(0,1500)
            Y =  random.randint(0,800)

            with self.canvas.before:
                self.color = Color(3/255, 252/255, 94/255, 1)  # set the colour

                # Seting the size and position of canvas
                self.rect = RoundedRectangle(pos=(X, Y),
                                      size=(50,
                                            50), radius=[50])
                self.balls_pos.append(self.rect)
                self.balls_color.append(self.color)



    def anim(self,k):



        for i in self.balls_pos:
            X = random.randint(0, 1500)
            Y = random.randint(0, 800)
            balls_pos = Animation(pos=(X, Y), duration=5)
            balls_pos.start(i)




        for i in self.balls_color:
            R = random.randint(0, 255)
            G = random.randint(0, 255)
            B = random.randint(0, 255)
            balls_color = Animation(rgb=(R/255, G/255, B/255, 1), duration=5)
            balls_color.start(i)
    def on_kv_post(self, base_widget):
        Clock.schedule_interval(self.addy, 0.1)
        Clock.schedule_interval(self.anim, 5)
        Clock.schedule_interval(self.timer_funct, 0.5)
class Server(MDApp):

    def build(self):
        return Main_Server_Gemys()



if __name__ == '__main__':
    Server().run()