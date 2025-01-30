from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from modules.logic_tab import FocusSwitchingTextInput
from telas.login_cadastro.funcoes_login import validate_login, go_to_register, show_popup

class LoginPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.username = FocusSwitchingTextInput(hint_text="Usuário")
        self.password = FocusSwitchingTextInput(hint_text="Senha", password=True)
        self.login_button = Button(text="Entrar", on_press=self.login_validate)
        self.register_button = Button(text="Cadastrar", on_press=self.login_to_go_register)

        layout.add_widget(Label(text="Login"))
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(self.login_button)
        layout.add_widget(self.register_button)

        self.add_widget(layout)
        
    def login_validate(self, instance):
        validate_login(self, instance)
        
    def login_to_go_register(self, instance):
        go_to_register(self, instance)

    