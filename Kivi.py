class MainWindow(Screen):
   def __init__(self, name, **kw):
      super().__init__(name=name, **kw)
   def on_shop_screen(self):
    self.manager.current = "shop"

   def click(self):
      self.ids.karas.size_hint =(0.9, 0.9)


#::::       '''''

class ClickerApp(App):
   def build(self):
      sm = ScreenManager()
      sm.add_widget(MainWindow(name='main'))
      sm.add_widget(MainWindow(name='shop'))
      return sm

class LoginApp(App):
   def __init__(self, name, **kw):
      super().__init__(name=name, **kw)
   def on_main_screen(self, *args):
      self.manager.current = 'main'