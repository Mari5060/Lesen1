import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager

def write_info(data):
    with open('dataa.json', 'w', encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False)

class MainWindow(Screen):
   def __init__(self, name, **kw):
       super().__init__(name=name, **kw)
   def on_shop_screen(self):
       self.manager.current = "shop"



   def on_enter(self, *args):
       data = read_info()
       self.ids.score_lbl.text = "Грошей від продаж: " + str(data["score"])

   def click(self):
       data = read_info()
       data["score"] += data["power"]
       write_info(data)
       self.ids.score_lbl.text = "Грошей від продаж: " + str(data["score"])
       self.ids.karas.size_hint =(0.9, 0.9)



#::::       '''''

class ClickerApp(App):
   def build(self):
      sm = ScreenManager()
      sm.add_widget(MainWindow(name='main'))
      sm.add_widget(ShopScreen(name='shop'))
      return sm

class ShopScreen(Screen):
    def on_main_screen(self):
        self.manager.current = "main"

    def buy(self, price, power):
        data = read_info()
        if data['score'] >= price:
            data['power'] += power
            data['score'] -= price
            write_info(data)
        else:
            print('Не клює... Іди продавай шо є')


def read_info():
    try:
        with open('dataa.json','r',encoding='utf-8') as file:
            data = json.load(file)
    except:
        data = {
            'score': 0,
            'power': 1
        }
    return data

print(read_info())
class LoginApp(Screen):
   def __init__(self, name, **kw):
      super().__init__(name=name, **kw)
   def on_main_screen(self, *args):
      self.manager.current = 'main'


ClickerApp().run()
