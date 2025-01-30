from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from modules.logic_tab import FocusSwitchingTextInput
from telas.login_cadastro.funcoes_register import *

class RegisterPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.username = FocusSwitchingTextInput(hint_text="Novo Usuário")
        self.password = FocusSwitchingTextInput(hint_text="Nova Senha", password=True)
        self.identidade_OAB = FocusSwitchingTextInput(hint_text="Identidade OAB")
        self.register_button = Button(text="Registrar", on_press=self.user_register)
        self.back_button = Button(text="Voltar ao Login", on_press=self.back_to_login)

        layout.add_widget(Label(text="Cadastro"))
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(self.identidade_OAB)
        layout.add_widget(self.register_button)
        layout.add_widget(self.back_button)

        self.add_widget(layout)
        
    def user_register(self, instance):
        register_user(self, instance)
    
    def back_to_login(self, instance):
        go_to_login(self, instance)
