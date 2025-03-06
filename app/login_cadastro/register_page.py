from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from modules.logic_tab import FocusSwitchingTextInput
from app.login_cadastro.funcoes_register import *

class RegisterPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.username = FocusSwitchingTextInput(hint_text="Novo Usuário", size_hint_y=0.06)
        self.password = FocusSwitchingTextInput(hint_text="Nova Senha",size_hint_y = 0.06 , password=True)
        self.identidade_OAB = FocusSwitchingTextInput(hint_text="Identidade OAB", size_hint_y=0.06)
        self.register_button = Button(text="Registrar", size_hint=(0.18, 0.04), pos_hint={"x": 0.41}, on_press=self.user_register)
        self.back_button = Button(text="Voltar ao Login", size_hint=(0.18, 0.04), pos_hint={"x": 0.41}, on_press=self.back_to_login)

        layout.add_widget(Label(text="Cadastro", font_name="Roboto", font_size=30, size_hint_y=0.20))
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
