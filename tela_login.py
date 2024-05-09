from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex
from kivy.uix.progressbar import ProgressBar
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image,  AsyncImage
from kivy.core.window import Window

Window.size = (900,500)

class FloatApp(App):
    def build(self):
        Window.clearcolor=('d0417e')
        
        flo = FloatLayout()
        icon_login = AsyncImage(
            source='https://cdn-icons-png.flaticon.com/512/5550/5550463.png',
            pos=(590, 630),
            size_hint= (.4, .3))
        flo.add_widget(icon_login)
        
        self.t1 = TextInput(text = 'Login', size_hint=(.2, .1), pos=(770, 500))
        flo.add_widget(self.t1)

        self.t2 = TextInput(
         text = 'Senha' , multiline=True, size_hint=(.2, .1), pos=(770, 350))
        flo.add_widget(self.t2)

        b1 = Button(
            text='Entrar', size_hint = (.2, 0.1),
            pos_hint = {'center_x':.5, 'center_y':.07},
            on_press = self.entrar
        )
        b2 = Button(
            text='Cadastrar', size_hint = (.2, .1),
            pos_hint = {'center_x':.5, 'center_y':.20},
            on_press = self.cadastrar
        )
        
        self.label_cadastrar = Label(
            pos_hint = {'center_x': .50, 'center_y': .30}, 
            color = [1,1,1,1]
        )

        self.label_entrar = Label(
            pos_hint = {'center_x': .50, 'center_y': .30}, 
            color = [1,1,1,1]
        )
        
        flo.add_widget(b1)
        flo.add_widget(b2)
        flo.add_widget(self.label_cadastrar)
        flo.add_widget(self.label_entrar)
        
        return flo

    def cadastrar(self, instance):
        login = self.t1.text
        mensagem = f'O Login {login} foi cadastrado!'
        self.label_cadastrar.text = mensagem
    
    def entrar(self, instance):
        login = self.t1.text
        mensagem = f'O login {login} entrou no sistema!'
        self.label_cadastrar.text = mensagem

      
FloatApp().run()