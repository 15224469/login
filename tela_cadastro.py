from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.label import Label

class Cadastro(FloatLayout):
    def __init__(self, **kwargs):
        super(Cadastro, self).__init__(**kwargs)
        self.orientation='horizontal'
        self.spacing=5
        self.padding=[20, 10]
        Window.clearcolor = get_color_from_hex('d0417e') 

        self.label = Label(
            text= 'CADASTRO:', 
            font_size = 40, 
            font_name = 'Georgia',
            size_hint_y=None,
            pos_hint={'x': .013, "y": .8}
            )
        self.add_widget(self.label)

        self.nome = TextInput(
            hint_text="Digite Seu Nome Completo: ",
            size_hint=[.4, .1],
            multiline=False,
            pos_hint= {'x': .3, "y": .7},
            padding_y= [10, 10],
            padding_x= [10, 10],
            background_color=get_color_from_hex('ffdde8'),  
            background_normal='',  
            border=(1, 1, 1, 1)  
        )
        self.add_widget(self.nome)

        self.email = TextInput(
            hint_text="Digite um E-mail Válido: ",
            size_hint=[.4, .1],
            multiline=False,
            pos_hint= {'x': .3, "y": .5},
            padding_y= [10, 10],
            padding_x= [10, 10],
            background_color=get_color_from_hex('ffdde8'),  
            background_normal='',  
            border=(1, 1, 1, 1)  
        )
        self.add_widget(self.email)

        self.celular = TextInput(
            hint_text="Digite Seu Número de telefone: ",
            size_hint=[.4, .1],
            multiline=False,
            pos_hint= {'x': .3, "y": .3},
            padding_y= [10, 10],
            padding_x= [10, 10],
            background_color=get_color_from_hex('ffdde8'),  
            background_normal='',  
            border=(1, 1, 1, 1)  
        )
        self.add_widget(self.celular)

        self.senha = TextInput(
            hint_text="Senha: ",
            password=True,
            size_hint=(.4, .1),
            multiline=False,
            pos_hint= {'x': .3, "y": .1},
            padding_y= [10, 10],
            padding_x= [10, 10],
            background_color=get_color_from_hex('ffdde8'),  
            background_normal='',
            border=(1, 1, 1, 1)  
        )
        self.add_widget(self.senha)

        self.button = Button(
            size_hint = (.1, .05),
            pos_hint = {'x': .6, 'y':.13} ,
            text = 'Ver Senha',
            background_color = get_color_from_hex('ffdde8'),  
            background_normal='', 
            on_press = self.togglevisibility 
        )

        self.button2 = Button(
            size_hint = (.1, .05),
            pos_hint = {'x': .45, 'y':.04} ,
            text = 'Cadastrar',
            background_color = ('ffdde8')
              )
        self.add_widget(self.button2)

        self.add_widget(self.button)

    def togglevisibility(self, instance):
        if self.senha.password == True:
            self.senha.password = False
            self.button.text = 'Hide'   
        else:
            self.senha.password = True
            self.button.text = 'Show'   





class TelaCadastro(App):
    def build(self):
        return Cadastro()

TelaCadastro().run()