from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.padding = 10
        layout.spacing = 10

        self.input = TextInput(hint_text="Escribe tu usuario", multiline=False)
        self.input.font_size = 24
        self.input2 = TextInput(hint_text="Escribe tu contraseña", multiline=False, password=True)
        self.input2.font_size = 24

        btn = Button(text="Login")

        btn.bind(on_press=self.login)

        layout.add_widget(self.input)
        layout.add_widget(self.input2)
        layout.add_widget(btn)

        return layout

    def login(self, instance):
        if self.input.text == "diegito1024" and self.input2.text == "123456":
            self.input.text = "Login exitoso"

MyApp().run()