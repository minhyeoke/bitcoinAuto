from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import requests
import json

class KivyApp(App):
     firebase_url= "https://kivycrudproject-1cdfd-default-rtdb.firebaseio.com/.json"
     def build(self):
         box_layout = BoxLayout()
         button = Button(text="Create Patch")
         button.bind(on_press=self.create_patch)
         box_layout.add_widget(button)
         return box_layout

     def create_patch(self, *args):
         print("BUTTON CLICKED")
         json_data = {"url":"google.com","age":"15 years old"}
         res=requests.patch(url=self.firebase_url, json=json.loads(json_data))
         print(res)
if __name__=='__main__':
    KivyApp().run()
