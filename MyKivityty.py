from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        line1 = BoxLayout(orientation="vertical")
        line2 = BoxLayout(orientation='horizontal')

        lbl = Label(text="Напиши логін:")
        lbl2 = Label(text="Напиши пароль:")



        line1.add_widget(lbl)
        line2.add_widget(lbl2)
        line1.add_widget(line2)

        return line1




MyApp().run()









